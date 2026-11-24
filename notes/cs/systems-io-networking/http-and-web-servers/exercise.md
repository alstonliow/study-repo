::: {#prob-parse-uri-code .problem .coding origin="adapted" source="res-cmu-15213-labs-proxy-lab" tags="http,proxy,strings"}
A proxy receives request lines whose URI is a full URL (@def-web-proxy). Write `parse_uri(uri, host, port, path)`, which splits an absolute URL of the form `http://host[:port][path]` into its parts:

- `host` receives the host name (non-empty, ending at `:`, `/` or the end of the string);
- `port` receives the digits after `:` (at least one, at most five, all decimal digits), or `"80"` if there is no `:`;
- `path` receives everything from the first `/` after the host on, or `"/"` if there is none.

The scheme `http://` is matched without regard to case. The function returns $0$ on success and $-1$ if the URL is malformed (another scheme, an empty host, an empty or non-numeric port, a port of more than five digits) or if a part does not fit its buffer: `host` and `path` hold `MAXLINE` bytes and `port` holds $6$, each including the terminating `'\0'`.

```{.c .starter}
#include <ctype.h>

#define MAXLINE 256

int parse_uri(const char *uri, char *host, char *port, char *path) {
    return -1;
}
```

```{.c .tests}
static void ok(const char *uri, const char *h, const char *p, const char *pa) {
    char host[MAXLINE], port[6], path[MAXLINE];
    assert(parse_uri(uri, host, port, path) == 0);
    assert(strcmp(host, h) == 0);
    assert(strcmp(port, p) == 0);
    assert(strcmp(path, pa) == 0);
}

static void bad(const char *uri) {
    char host[MAXLINE], port[6], path[MAXLINE];
    assert(parse_uri(uri, host, port, path) == -1);
}

void test_basic(void) {
    ok("http://www.example.edu/hub/index.html", "www.example.edu", "80", "/hub/index.html");
    ok("http://www.example.edu:8080/hub/index.html", "www.example.edu", "8080", "/hub/index.html");
    ok("http://localhost:15213", "localhost", "15213", "/");
    ok("http://example.com", "example.com", "80", "/");
    ok("HTTP://Example.com/", "Example.com", "80", "/");
}

void test_query_and_colons_in_path(void) {
    ok("http://h.org/cgi-bin/adder?15213&18213", "h.org", "80", "/cgi-bin/adder?15213&18213");
    ok("http://h.org:81/a:b/c", "h.org", "81", "/a:b/c");
}

void test_malformed(void) {
    bad("https://example.com/");
    bad("ftp://example.com/");
    bad("example.com/index.html");
    bad("http:///index.html");
    bad("http://:80/");
    bad("http://example.com:/x");
    bad("http://example.com:8o/x");
    bad("http://example.com:123456/x");
}

void test_too_long(void) {
    char uri[2 * MAXLINE + 20];
    strcpy(uri, "http://");
    memset(uri + 7, 'a', MAXLINE);            /* a host of MAXLINE characters */
    strcpy(uri + 7 + MAXLINE, "/x");
    bad(uri);
    strcpy(uri, "http://h/");
    memset(uri + 9, 'b', MAXLINE);            /* a path of MAXLINE + 1 characters */
    uri[9 + MAXLINE] = '\0';
    bad(uri);
}
```
:::

::: {#prob-proxy-request-code .problem .coding origin="adapted" source="res-cmu-15213-labs-proxy-lab" tags="http,proxy,strings"}
After parsing the URL, a proxy builds the request it sends to the origin server (@exm-proxy-request). Write `build_request(host, port, path, headers, nheaders, out, size)`, where `headers` are the $n$ header lines the client sent (each without its `"\r\n"`), which writes into `out` the complete request, every line ending in `"\r\n"`, in this order:

1. the request line `GET path HTTP/1.0`;
2. the client's `Host` header unchanged if it sent one, otherwise `Host: host` when `port` is `"80"` and `Host: host:port` otherwise;
3. `User-Agent: ` followed by the string `USER_AGENT`;
4. `Connection: close` and then `Proxy-Connection: close`;
5. every other client header, unchanged and in the original order;
6. an empty line.

The client's own `User-Agent`, `Connection` and `Proxy-Connection` headers are dropped. Header names are compared without regard to case, and a line matches a name only if the name is followed directly by `:`. The function returns the length of the request, or $-1$ (with any contents in `out`) if it does not fit in `size` bytes including the terminating `'\0'`.

```{.c .starter}
#include <ctype.h>

#define USER_AGENT "Mozilla/5.0 (X11; Linux x86_64; rv:10.0.3) Gecko/20120305 Firefox/10.0.3"

int build_request(const char *host, const char *port, const char *path,
                  const char **headers, int nheaders, char *out, size_t size) {
    return -1;
}
```

```{.c .tests}
#define UA "User-Agent: " USER_AGENT "\r\n"
#define CLOSE "Connection: close\r\nProxy-Connection: close\r\n"

void test_no_client_headers(void) {
    char out[1024];
    const char *want = "GET /index.html HTTP/1.0\r\nHost: www.example.edu\r\n" UA CLOSE "\r\n";
    assert(build_request("www.example.edu", "80", "/index.html", NULL, 0, out, sizeof out) == (int)strlen(want));
    assert(strcmp(out, want) == 0);
}

void test_port_in_host_header(void) {
    char out[1024];
    const char *want = "GET / HTTP/1.0\r\nHost: localhost:15213\r\n" UA CLOSE "\r\n";
    assert(build_request("localhost", "15213", "/", NULL, 0, out, sizeof out) == (int)strlen(want));
    assert(strcmp(out, want) == 0);
}

void test_client_headers(void) {
    const char *hdr[] = {"Host: www.example.edu:8080", "Accept: text/html", "connection: keep-alive",
                         "User-Agent: curl/8.0", "PROXY-CONNECTION: keep-alive", "Accept-Language: en",
                         "Hostname-Hint: x"};
    char out[1024];
    const char *want = "GET /docs/a.html HTTP/1.0\r\nHost: www.example.edu:8080\r\n" UA CLOSE
                       "Accept: text/html\r\nAccept-Language: en\r\nHostname-Hint: x\r\n\r\n";
    assert(build_request("www.example.edu", "8080", "/docs/a.html", hdr, 7, out, sizeof out) == (int)strlen(want));
    assert(strcmp(out, want) == 0);
}

void test_too_small(void) {
    char out[64];
    assert(build_request("www.example.edu", "80", "/", NULL, 0, out, sizeof out) == -1);
    char exact[1024];
    int n = build_request("h", "80", "/", NULL, 0, exact, sizeof exact);
    assert(n > 0);
    assert(build_request("h", "80", "/", NULL, 0, exact, (size_t)n + 1) == n);
    assert(build_request("h", "80", "/", NULL, 0, exact, (size_t)n) == -1);
}
```
:::
