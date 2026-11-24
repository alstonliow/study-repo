::: {.solution for="prob-parse-uri-code" status="draft"}
```{.c}
#include <ctype.h>

#define MAXLINE 256

/* Does s start with p, ignoring case? */
static int starts_icase(const char *s, const char *p) {
    for (; *p; s++, p++)
        if (tolower((unsigned char)*s) != tolower((unsigned char)*p))
            return 0;
    return 1;
}

/* Copy n bytes of s into dst (capacity cap) with a terminating '\0'; 0 if it fits, else -1. */
static int copy_part(char *dst, size_t cap, const char *s, size_t n) {
    if (n + 1 > cap)
        return -1;
    memcpy(dst, s, n);
    dst[n] = '\0';
    return 0;
}

int parse_uri(const char *uri, char *host, char *port, char *path) {
    const char *prefix = "http://";
    size_t plen = strlen(prefix);
    if (!starts_icase(uri, prefix))
        return -1;
    const char *h = uri + plen;
    size_t hlen = strcspn(h, ":/");               /* host ends at ':', '/' or the end */
    if (hlen == 0 || copy_part(host, MAXLINE, h, hlen) < 0)
        return -1;
    const char *rest = h + hlen;
    if (*rest == ':') {
        const char *p = rest + 1;
        size_t n = 0;
        while (isdigit((unsigned char)p[n]))
            n++;
        if (n == 0 || n > 5 || (p[n] != '/' && p[n] != '\0'))
            return -1;
        copy_part(port, 6, p, n);
        rest = p + n;
    } else {
        strcpy(port, "80");
    }
    if (*rest == '\0')
        return copy_part(path, MAXLINE, "/", 1);
    return copy_part(path, MAXLINE, rest, strlen(rest));
}
```

The URL is split at the first `:` or `/` after the scheme, so a colon later in the path is not taken for a port. Every copy goes through `copy_part`, which checks the length before writing; a URL from the network can be arbitrarily long (@sec-cs-systems-io-networking-http-and-web-servers), and an unchecked `strcpy` into `host` would be a buffer overflow.
:::

::: {.solution for="prob-proxy-request-code" status="draft"}
```{.c}
#include <ctype.h>

#define USER_AGENT "Mozilla/5.0 (X11; Linux x86_64; rv:10.0.3) Gecko/20120305 Firefox/10.0.3"

/* Does s start with p, ignoring case? */
static int starts_icase(const char *s, const char *p) {
    for (; *p; s++, p++)
        if (tolower((unsigned char)*s) != tolower((unsigned char)*p))
            return 0;
    return 1;
}

/* Does the header line start with name followed by ':' (any case)? */
static int is_header(const char *line, const char *name) {
    return starts_icase(line, name) && line[strlen(name)] == ':';
}

/* Append a formatted piece to out at *len; -1 if it does not fit. */
static int append(char *out, size_t size, size_t *len, const char *a, const char *b, const char *c) {
    int n = snprintf(out + *len, size - *len, "%s%s%s\r\n", a, b, c);
    if (n < 0 || (size_t)n >= size - *len)
        return -1;
    *len += (size_t)n;
    return 0;
}

int build_request(const char *host, const char *port, const char *path,
                  const char **headers, int nheaders, char *out, size_t size) {
    size_t len = 0;
    const char *client_host = NULL;
    if (size == 0)
        return -1;
    out[0] = '\0';
    for (int i = 0; i < nheaders; i++)
        if (is_header(headers[i], "Host")) {
            client_host = headers[i];
            break;
        }
    if (append(out, size, &len, "GET ", path, " HTTP/1.0") < 0)
        return -1;
    if (client_host != NULL) {
        if (append(out, size, &len, client_host, "", "") < 0)
            return -1;
    } else if (strcmp(port, "80") == 0) {
        if (append(out, size, &len, "Host: ", host, "") < 0)
            return -1;
    } else {
        char hp[512];
        snprintf(hp, sizeof hp, "%s:%s", host, port);
        if (append(out, size, &len, "Host: ", hp, "") < 0)
            return -1;
    }
    if (append(out, size, &len, "User-Agent: ", USER_AGENT, "") < 0 ||
        append(out, size, &len, "Connection: close", "", "") < 0 ||
        append(out, size, &len, "Proxy-Connection: close", "", "") < 0)
        return -1;
    for (int i = 0; i < nheaders; i++) {
        const char *h = headers[i];
        if (is_header(h, "Host") || is_header(h, "User-Agent") ||
            is_header(h, "Connection") || is_header(h, "Proxy-Connection"))
            continue;                           /* replaced or already sent */
        if (append(out, size, &len, h, "", "") < 0)
            return -1;
    }
    if (append(out, size, &len, "", "", "") < 0)   /* the empty line */
        return -1;
    return (int)len;
}
```

`is_header` requires the colon right after the name, so `Hostname-Hint:` is not mistaken for `Host:`. Each line is written with `snprintf` bounded by the space left; `snprintf` returns the length it *would* have written, so a result of at least the remaining space means the request does not fit.
:::
