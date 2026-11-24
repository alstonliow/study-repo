::: {#prob-robust-read-code .problem .coding origin="adapted" source="res-cmu-15213-labs-proxy-lab" tags="unix-io,short-counts,sockets"}
A proxy reads HTTP requests from a socket, where `read` may return short counts (@def-short-count). Write two functions that work on any descriptor:

- `readn(fd, buf, n)` reads exactly $n$ bytes into `buf`, calling `read` as often as needed; it returns $n$, or fewer only if end of file comes first, or $-1$ on an error. A call interrupted by a signal (`errno == EINTR`) is repeated.
- `read_line(fd, buf, maxlen)` reads one text line: it stores bytes up to and including the first `'\n'`, but at most `maxlen - 1` bytes, then a terminating `'\0'`. It returns the number of bytes stored (not counting `'\0'`), $0$ if end of file comes before any byte, or $-1$ on an error. It must not read past the newline, so that the next call starts with the next line (read one byte at a time).

```{.c .starter}
#include <unistd.h>
#include <errno.h>

ssize_t readn(int fd, void *buf, size_t n) {
    return -1;
}

ssize_t read_line(int fd, char *buf, size_t maxlen) {
    return -1;
}
```

```{.c .tests}
#include <sys/wait.h>
#include <time.h>

/* A pipe whose writer (a child process) sends the pieces with pauses, so reads see short counts. */
static int slow_pipe(const char **pieces, int k) {
    int p[2];
    assert(pipe(p) == 0);
    if (fork() == 0) {
        close(p[0]);
        struct timespec pause = {0, 2000000};   /* 2 ms */
        for (int i = 0; i < k; i++) {
            write(p[1], pieces[i], strlen(pieces[i]));
            nanosleep(&pause, NULL);
        }
        _exit(0);
    }
    close(p[1]);
    return p[0];
}

void test_readn(void) {
    const char *pieces[] = {"abc", "defg", "hij"};
    int fd = slow_pipe(pieces, 3);
    char buf[16] = {0};
    assert(readn(fd, buf, 8) == 8);
    assert(memcmp(buf, "abcdefgh", 8) == 0);
    assert(readn(fd, buf, 8) == 2);          /* only "ij" before EOF */
    assert(memcmp(buf, "ij", 2) == 0);
    assert(readn(fd, buf, 8) == 0);
    close(fd);
    wait(NULL);
}

void test_read_line(void) {
    const char *pieces[] = {"GET http://ex", "ample.com/ HTTP/1.1\r\n", "Host: example.com\r\n\r\n", "tail"};
    int fd = slow_pipe(pieces, 4);
    char buf[64];
    assert(read_line(fd, buf, sizeof buf) == 34);
    assert(strcmp(buf, "GET http://example.com/ HTTP/1.1\r\n") == 0);
    assert(read_line(fd, buf, sizeof buf) == 19);
    assert(strcmp(buf, "Host: example.com\r\n") == 0);
    assert(read_line(fd, buf, sizeof buf) == 2);
    assert(strcmp(buf, "\r\n") == 0);
    assert(read_line(fd, buf, 3) == 2);      /* truncated to maxlen - 1 */
    assert(strcmp(buf, "ta") == 0);
    assert(read_line(fd, buf, sizeof buf) == 2);   /* last line has no newline */
    assert(strcmp(buf, "il") == 0);
    assert(read_line(fd, buf, sizeof buf) == 0);
    close(fd);
    wait(NULL);
}

void test_bad_descriptor(void) {
    char buf[4];
    assert(readn(-1, buf, 4) == -1);
    assert(read_line(-1, buf, 4) == -1);
}
```
:::
