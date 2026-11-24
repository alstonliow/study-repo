---
title: "HTTP and Web Servers"
sources: [cmu15213-22, cmu15213lab-7]
requires: [cs/systems-io-networking/sockets-interface, cs/systems-io-networking/file-sharing-and-redirection]
status: draft
---

<!-- Added 2026-11-24 from CMU 15-213 (Fall 2015), Lecture 22 "Network Programming: Part II" (Web basics, HTTP, a tiny Web server, CGI, proxies) and the Proxy Lab handout (part I: a sequential proxy), in our own wording; the example transaction is our own. -->

The Web is a client-server application (@def-client-server-model): browsers are clients, and Web servers return *content* to them over connections, using a simple text protocol.

::: {#def-web-content .definition name="Web content and URLs"}

Web *content* is a sequence of bytes with a *MIME type*, such as `text/html`, `text/plain`, `image/png` or `application/json`. A server provides content in two ways:

- *static content* is a file on the server, returned as it is;
- *dynamic content* is produced by running a program on the server and returning its output.

Every piece of content is named by a *URL* (universal resource locator) such as `http://www.example.edu:8080/cgi-bin/adder?15213&18213`. The prefix `http://www.example.edu:8080` tells the client which server to contact (port $80$ if none is given); the suffix, the *URI*, tells the server which file to return or which program to run, and for a program the arguments after `?`, separated by `&`.

:::

::: {#fig-http-and-web-servers-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[tick, anchor=west] (a) at (0,0) {\texttt{http://}};
\node[tick, anchor=west] (b) at (a.east) {\texttt{www.example.edu}};
\node[tick, anchor=west] (c) at (b.east) {\texttt{:8080}};
\node[tick, anchor=west] (d) at (c.east) {\texttt{/cgi-bin/adder}};
\node[tick, anchor=west] (e) at (d.east) {\texttt{?15213\&18213}};
\draw[decorate, decoration={brace}] ([yshift=3pt]a.north west) -- ([yshift=3pt]a.north east) node[midway, above=3pt, tick] {protocol};
\draw[decorate, decoration={brace}] ([yshift=3pt]b.north west) -- ([yshift=3pt]b.north east) node[midway, above=3pt, tick] {host};
\draw[decorate, decoration={brace}] ([yshift=3pt]c.north west) -- ([yshift=3pt]c.north east) node[midway, above=3pt, tick] {port};
\draw[decorate, decoration={brace, mirror}] ([yshift=-3pt]d.south west) -- ([yshift=-3pt]d.south east) node[midway, below=3pt, tick] {program};
\draw[decorate, decoration={brace, mirror}] ([yshift=-3pt]e.south west) -- ([yshift=-3pt]e.south east) node[midway, below=3pt, tick] {arguments};
\draw[decorate, decoration={brace, mirror}] ([yshift=-18pt]d.south west) -- ([yshift=-18pt]e.south east) node[midway, below=3pt, tick] {URI};
\end{tikzpicture}
\end{center}
```

The parts of a URL. The client uses host and port to connect; the server interprets the URI

:::

::: {#def-http-request .definition name="HTTP requests and responses"}

*HTTP* (HyperText Transfer Protocol) messages are text lines, each ending in a carriage return and line feed `\r\n`.

- A *request* is a *request line* `method URI version`, such as `GET /index.html HTTP/1.1`, followed by zero or more *request headers* `name: value`, and an empty line. The method `GET` asks for content; the header `Host:` names the server host, which lets one server serve several domains and lets proxies find the origin server.
- A *response* is a *response line* `version status-code status-message`, such as `HTTP/1.0 200 OK`, followed by *response headers*, an empty line, and the *response body*. Common codes are `200` (OK), `301` (moved permanently), `400` (bad request), `403` (forbidden) and `404` (not found). The headers `Content-Type` (the MIME type) and `Content-Length` (the size of the body in bytes) tell the client how to interpret and where to stop reading the body.

:::

::: {#exm-http-transaction .example name="An HTTP transaction by hand"}

With `telnet www.example.edu 80` (@sec-cs-systems-io-networking-sockets-interface) one can type a request and read the response. The lines the client sends are marked `>`, the server's `<`:

```text
> GET /index.html HTTP/1.1
> Host: www.example.edu
>
< HTTP/1.1 200 OK
< Content-Type: text/html
< Content-Length: 54
<
< <html><body><p>Welcome to example.edu</p></body></html>
```

The empty line after `Host:` ends the request, and the empty line after the headers separates them from the $54$ bytes of the body.

:::

::: {#fig-http-and-web-servers-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.5cm]
\draw[regionA] (0,0.4) rectangle (6.4,-2.9); \node[lab, anchor=south] at (3.2,0.4) {request};
\node[tick, anchor=west] at (0.1,0) {\texttt{GET /index.html HTTP/1.1}};
\node[tick, anchor=west] at (0.1,-1) {\texttt{Host: www.example.edu}};
\node[tick, anchor=west] at (0.1,-2) {\texttt{\textbackslash r\textbackslash n}};
\node[tick, anchor=west] at (6.6,0) {request line};
\node[tick, anchor=west] at (6.6,-1) {headers};
\node[tick, anchor=west] at (6.6,-2) {empty line ends the request};
\draw[regionC] (0,-4.2) rectangle (6.4,-8.9); \node[lab, anchor=south] at (3.2,-4.2) {response};
\node[tick, anchor=west] at (0.1,-4.6) {\texttt{HTTP/1.1 200 OK}};
\node[tick, anchor=west] at (0.1,-5.6) {\texttt{Content-Type: text/html}};
\node[tick, anchor=west] at (0.1,-6.6) {\texttt{Content-Length: 54}};
\node[tick, anchor=west] at (0.1,-7.6) {\texttt{\textbackslash r\textbackslash n}};
\draw[hl cell] (0.1,-8.75) rectangle (6.3,-8.05); \node[tick] at (3.2,-8.4) {54 bytes of HTML};
\node[tick, anchor=west] at (6.6,-4.6) {response line};
\node[tick, anchor=west] at (6.6,-6.1) {headers};
\node[tick, anchor=west] at (6.6,-7.6) {empty line};
\node[tick, anchor=west] at (6.6,-8.4) {body};
\end{tikzpicture}
\end{center}
```

The structure of an HTTP request and response. Every line ends in `\r\n`; an empty line ends the headers

:::

::: {#def-tiny-web-server .definition name="A tiny Web server"}

A minimal iterative Web server repeats: accept a connection (@def-listening-connected); read the request line and headers; split the URI into a file name and arguments; then

- for *static content*, check that the file exists and is readable, send a response line and headers with the content type (derived from the file name's extension) and length, then the file's bytes;
- for *dynamic content*, check that the program exists and is executable and run it as below;

and close the connected descriptor. Errors are answered with a response such as `404 Not Found` with a short HTML body explaining the error.

:::

::: {#fig-http-and-web-servers-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.9cm]
\node[box] (a) at (0,0) {\texttt{accept}};
\node[box] (r) at (0,-1) {read request line and headers};
\node[box] (p) at (0,-2) {parse URI};
\node[hl box] (s) at (-3,-3.2) {static: send headers and file};
\node[hl box] (d) at (3,-3.2) {dynamic: \texttt{fork}, run program};
\node[box] (c) at (0,-4.4) {\texttt{close(connfd)}};
\draw[->] (a) -- (r); \draw[->] (r) -- (p);
\draw[->] (p) -- node[edge label, left] {file} (s); \draw[->] (p) -- node[edge label, right] {\texttt{cgi-bin}} (d);
\draw[->] (s) -- (c); \draw[->] (d) -- (c);
\draw[->] (c.west) -- ++(-4.6,0) |- (a.west);
\end{tikzpicture}
\end{center}
```

The main loop of a tiny Web server: each request is answered with a file or with a program's output

:::

::: {#def-cgi .definition name="CGI: serving dynamic content"}

The *Common Gateway Interface* (CGI) fixes how a server passes a request to a program and gets its output back:

1. the server `fork`s a child (@def-fork);
2. the child stores the arguments in the environment variable `QUERY_STRING` (for `GET`, the part of the URI after `?`);
3. the child redirects its standard output to the connected descriptor with `dup2(connfd, STDOUT_FILENO)` (@def-dup2);
4. the child `execve`s the program (@def-execve), which reads its arguments with `getenv("QUERY_STRING")` and prints the response headers `Content-Type` and `Content-Length`, an empty line, and the body; everything it prints goes straight to the client.

The server sends the response line first, then the program supplies the rest; the server then reaps the child.

:::

::: {#fig-http-and-web-servers-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (cl) at (0,0) {client};
\node[box] (sv) at (7.2,0) {server};
\node[hl box] (ch) at (7.2,-2.0) {child: \texttt{adder}};
\draw[->, emph] (cl) -- node[edge label, above] {\texttt{GET /cgi-bin/adder?15213\&18213}} (sv);
\draw[->] (sv) -- node[edge label, right] {\texttt{fork}, \texttt{execve}} (ch);
\node[tick, anchor=west] at (8.6,-1.8) {\texttt{QUERY\_STRING=15213\&18213}};
\node[tick, anchor=west] at (8.6,-2.25) {\texttt{stdout} $\to$ \texttt{connfd}};
\draw[->, draw=accent, emph] (ch.west) -- node[edge label, above, pos=0.55] {output: \dots\ $15213+18213=33426$} (0,-2.0) -- (cl.south);
\end{tikzpicture}
\end{center}
```

Serving dynamic content with CGI: the server passes the arguments in the environment, and the child's standard output is the connection itself

:::

::: {#exm-adder-cgi .example name="An adder CGI program"}

```c
int main(void) {
    char body[256];
    const char *q = getenv("QUERY_STRING");     /* e.g. "15213&18213" */
    long a = 0, b = 0;
    if (q != NULL)
        sscanf(q, "%ld&%ld", &a, &b);
    int n = snprintf(body, sizeof body,
                     "<p>%ld + %ld = %ld</p>\r\n", a, b, a + b);
    printf("Content-Type: text/html\r\n");
    printf("Content-Length: %d\r\n\r\n", n);
    printf("%s", body);
    fflush(stdout);
    return 0;
}
```

For the URL of @def-web-content the client receives `<p>15213 + 18213 = 33426</p>`. The program knows nothing about sockets: it reads an environment variable and writes to standard output.

:::

::: {#def-web-proxy .definition name="Web proxy"}

A *proxy* is an intermediary between a client and an *origin server*. To the client it acts as a server: it accepts the client's request, whose URI is a full URL (`GET http://www.example.edu/index.html HTTP/1.1`). To the origin server it acts as a client: it connects to the host and port named in the URL, sends its own request with only the path as URI, and forwards the response back to the client. Proxies serve as firewalls, anonymizers (the server sees the proxy's address), filters, and *caches*: a proxy that stores recently fetched objects can answer a repeated request without contacting the server.

:::

::: {#fig-http-and-web-servers-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (c) at (0,0) {client};
\node[hl box] (p) at (4.5,0) {proxy};
\node[box] (s) at (9,0) {origin server};
\draw[regionB] (3.7,-1.5) rectangle (5.3,-0.8); \node[tick] at (4.5,-1.15) {cache};
\draw[->, emph] (c.15) -- node[edge label, above] {1. request (full URL)} (p.165);
\draw[->, emph] (p.15) -- node[edge label, above] {2. request (path)} (s.165);
\draw[->, emph, draw=accent] (s.195) -- node[edge label, below] {3. response} (p.345);
\draw[->, emph, draw=accent] (p.195) -- node[edge label, below] {4. response} (c.345);
\draw[<->] (p) -- (4.5,-0.8);
\end{tikzpicture}
\end{center}
```

A proxy is a server to the client and a client to the origin server; it can keep copies of responses in a cache

:::

::: {#exm-proxy-request .example name="What a proxy sends on"}

A browser configured to use a proxy sends

```text
GET http://www.example.edu:8080/docs/a.html HTTP/1.1
Host: www.example.edu:8080
Accept: text/html
Connection: keep-alive
```

A simple HTTP/1.0 proxy opens a connection to `www.example.edu` on port $8080$ and sends

```text
GET /docs/a.html HTTP/1.0
Host: www.example.edu:8080
Accept: text/html
Connection: close
Proxy-Connection: close
```

It keeps the client's `Host` header, forwards other headers unchanged, downgrades the version, and asks for `Connection: close`, so that the server closes the connection after one response and the proxy knows where the response ends. @prob-parse-uri-code and @prob-proxy-request-code implement the two steps.

:::

::: {#rmk-http-and-web-servers-1 name="Robustness"}

A server reads input that any client in the world can send. It must survive malformed requests, clients that close the connection early (a `write` to a closed connection raises `SIGPIPE`, whose default action terminates the server, so servers ignore it and check `write`'s result for the error `EPIPE`) and over-long lines (read with a length limit, as `read_line` in @prob-robust-read-code does). A bug here is not a crash of one program but a hole in a public service (@def-buffer-overflow).

:::
