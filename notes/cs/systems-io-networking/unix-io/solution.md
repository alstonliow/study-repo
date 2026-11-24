::: {.solution for="prob-robust-read-code" status="draft"}
```{.c}
#include <unistd.h>
#include <errno.h>

ssize_t readn(int fd, void *buf, size_t n) {
    size_t left = n;
    char *p = buf;
    while (left > 0) {
        ssize_t r = read(fd, p, left);
        if (r < 0) {
            if (errno == EINTR)
                continue;               /* interrupted by a handler: try again */
            return -1;
        }
        if (r == 0)
            break;                      /* EOF */
        left -= (size_t)r;
        p += r;
    }
    return (ssize_t)(n - left);
}

ssize_t read_line(int fd, char *buf, size_t maxlen) {
    size_t i = 0;
    while (i + 1 < maxlen) {
        char c;
        ssize_t r = read(fd, &c, 1);
        if (r < 0) {
            if (errno == EINTR)
                continue;
            return -1;
        }
        if (r == 0)
            break;                      /* EOF: return what we have */
        buf[i++] = c;
        if (c == '\n')
            break;                      /* stop right after the newline */
    }
    if (maxlen > 0)
        buf[i] = '\0';
    return (ssize_t)i;
}
```

`readn` follows @def-robust-read: the loop keeps the bytes read so far at the front of `buf` and stops only at $n$ bytes, EOF or a real error (@prp-readn-correct). `read_line` reads single bytes so that it never consumes part of the next line; a buffered version (@def-buffered-reading) would keep the extra bytes in its buffer for the next call instead. The truncation test shows that the rest of an over-long line is returned by the next call.
:::
