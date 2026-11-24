---
title: "Networks and the Global IP Internet"
sources: [cmu15213-21]
requires: [cs/data-representation/byte-ordering]
status: draft
---

<!-- Added 2026-11-24 from CMU 15-213 (Fall 2015), Lecture 21 "Network Programming: Part I" (client-server model, networks, internet protocols, IP addresses, DNS, connections), in our own wording; the addresses in the examples are our own. -->

Network applications are built from one model, the client-server transaction, on top of a layered system of networks. To a host, a network is just another I/O device: data arrives at and leaves from a network adapter, and the kernel exposes it to programs through file descriptors.

::: {#def-client-server-model .definition name="Client-server model"}

A network application consists of one *server* process, which manages some *resource*, and one or more *client* processes. A *transaction* has four steps:

1. the client sends a *request* to the server;
2. the server interprets the request and manipulates its resource;
3. the server sends a *response* to the client;
4. the client processes the response.

Clients and servers are processes, not machines: one host can run many of each.

:::

::: {#fig-network-basics-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (c) at (0,0) {client\\process};
\node[box] (s) at (6,0) {server\\process};
\node[hl box] (r) at (9,0) {resource};
\draw[->, emph] (c.20) -- node[edge label, above] {1. request} (s.160);
\draw[->, emph, draw=accent] (s.200) -- node[edge label, below] {3. response} (c.340);
\draw[<->] (s) -- (r);
\node[tick] at (7.6,0.75) {2. handle request};
\node[tick] at (0,-1.1) {4. handle response};
\end{tikzpicture}
\end{center}
```

One client-server transaction. The arrows are messages over the network; steps 2 and 4 are local computation

:::

::: {#def-network-hierarchy .definition name="LANs, bridges, routers, internets"}

Networks form a hierarchy by geographical extent.

- An *Ethernet segment* connects hosts by wires to a *hub* in one room or floor. Each Ethernet adapter has a unique 48-bit address, and hosts send bits in chunks called *frames*; every host on the segment sees every frame, and only the destination reads it.
- *Bridges* join segments into a *bridged Ethernet*, a *local area network* (LAN), spanning a building or campus; a bridge learns which hosts are reachable through which port and forwards frames only where needed.
- *Routers* connect several possibly incompatible LANs and *wide area networks* (WANs) into an *internet* (lower case): a network of networks. The *Internet* (upper case) is the global one, based on the TCP/IP protocols.

:::

::: {#fig-network-basics-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (-1.3,-0.5) rectangle (4.3,2.7); \node[tick] at (1.5,-0.75) {LAN 1 (bridged Ethernet)};
\draw[regionC] (6.0,0.6) rectangle (8.6,2.7); \node[tick] at (7.3,0.35) {LAN 2};
\node[hl box] (h1) at (0,1.2) {hub}; \node[hl box] (h2) at (3,1.2) {hub};
\foreach \x in {-0.8,0,0.8} { \node[dot] at (\x,2.3) {}; \draw (\x,2.15) -- (h1); }
\foreach \x in {2.2,3,3.8} { \node[dot] at (\x,2.3) {}; \draw (\x,2.15) -- (h2); }
\node[box] (b) at (1.5,0) {bridge}; \draw (h1) -- (b); \draw (h2) -- (b);
\foreach \x in {6.5,7.3,8.1} { \node[dot] at (\x,2.3) {}; \draw (\x,2.15) -- (7.3,1.2); }
\node[box] at (7.3,1.2) {hub};
\node[hl box] (r1) at (2.6,-1.6) {router}; \node[hl box] (r2) at (7.3,-1.6) {router};
\draw (b) -- (r1); \draw (7.3,0.9) -- (r2);
\draw[emph] (r1) -- node[edge label, below] {WAN} (r2);
\node[tick] at (5.0,-2.4) {hosts (dots), hubs, bridges and routers form an internet};
\end{tikzpicture}
\end{center}
```

A small internet: hosts connect to hubs, a bridge joins two segments into one LAN, and routers connect the LANs through a wide area network

:::

::: {#def-internet-protocol .definition name="Internet protocol"}

An internet connects networks built with different, incompatible technologies. Protocol software running on every host and router hides the differences by providing

- a *naming scheme*: a uniform format of host addresses, each host getting at least one *internet address* that identifies it uniquely;
- a *delivery mechanism*: a uniform way to bundle data into *packets*, each a *header* (packet size, source and destination addresses) followed by a *payload* of data bytes.

A packet crosses each LAN *encapsulated* in that LAN's own frame: a router removes the frame header of the incoming LAN and adds the frame header of the outgoing one, leaving the internet packet inside unchanged.

:::

::: {#fig-network-basics-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.75cm]
\node[lab, anchor=east] at (-0.2,3) {host A};
\draw[regionC] (3.2,2.7) rectangle (6.0,3.3); \node[tick] at (4.6,3) {data};
\node[lab, anchor=east] at (-0.2,2) {protocol software};
\draw[hl cell] (1.8,1.7) rectangle (3.2,2.3); \node[tick] at (2.5,2) {PH};
\draw[regionC] (3.2,1.7) rectangle (6.0,2.3); \node[tick] at (4.6,2) {data};
\node[lab, anchor=east] at (-0.2,1) {LAN 1 frame};
\draw[cell frame] (0.4,0.7) rectangle (1.8,1.3); \node[tick] at (1.1,1) {FH1};
\draw[hl cell] (1.8,0.7) rectangle (3.2,1.3); \node[tick] at (2.5,1) {PH};
\draw[regionC] (3.2,0.7) rectangle (6.0,1.3); \node[tick] at (4.6,1) {data};
\node[lab, anchor=east] at (-0.2,0) {router: LAN 2 frame};
\draw[cell frame, draw=accent] (0.4,-0.3) rectangle (1.8,0.3); \node[tick] at (1.1,0) {FH2};
\draw[hl cell] (1.8,-0.3) rectangle (3.2,0.3); \node[tick] at (2.5,0) {PH};
\draw[regionC] (3.2,-0.3) rectangle (6.0,0.3); \node[tick] at (4.6,0) {data};
\node[lab, anchor=east] at (-0.2,-1) {host B};
\draw[regionC] (3.2,-1.3) rectangle (6.0,-0.7); \node[tick] at (4.6,-1) {data};
\node[tick, anchor=west] at (6.3,2) {add internet packet header};
\node[tick, anchor=west] at (6.3,1) {add LAN 1 frame header};
\node[tick, anchor=west] at (6.3,0) {swap frame header};
\node[tick, anchor=west] at (6.3,-1) {strip both headers};
\end{tikzpicture}
\end{center}
```

Encapsulation: host A's data travels inside an internet packet (header PH), which travels inside a frame of each LAN in turn (headers FH1, FH2); the router replaces only the frame header

:::

::: {#def-ip-address .definition name="IP address"}

An *IPv4 address* is an unsigned $32$-bit integer, stored in network byte order, which is big endian (@def-endianness), whatever the host's own order. It is written in *dotted-decimal notation*: the four bytes in decimal, separated by dots, most significant first. (IPv6 uses $128$-bit addresses; the programming interface below handles both.)

:::

::: {#exm-dotted-decimal .example name="Converting an IP address"}

The address `0x8002C2F2` has bytes `0x80`, `0x02`, `0xC2`, `0xF2`, that is $128$, $2$, $194$, $242$, so it is written `128.2.194.242`. Conversely `127.0.0.1` is
$$127\cdot2^{24}+0\cdot2^{16}+0\cdot2^{8}+1=\texttt{0x7F000001},$$
the *loopback* address, which always refers to the local host. On a little-endian machine the four bytes of `128.2.194.242` lie in memory in the order `80 02 C2 F2`, the reverse of the host's own layout of the integer `0x8002C2F2`, which is why a conversion such as `htonl` is needed.

:::

::: {#fig-network-basics-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \i/\h/\d in {0/80/128,1/02/2,2/C2/194,3/F2/242} {
  \draw[cell frame] (\i*1.6,0) rectangle (\i*1.6+1.6,0.6); \node[tick] at (\i*1.6+0.8,0.3) {\texttt{0x\h}};
  \draw[hl cell] (\i*1.6,-1.2) rectangle (\i*1.6+1.6,-0.6); \node[tick] at (\i*1.6+0.8,-0.9) {\d};
  \draw[map] (\i*1.6+0.8,-0.05) -- (\i*1.6+0.8,-0.55);
}
\node[lab] at (3.2,-1.6) {\texttt{128.2.194.242}};
\node[lab, anchor=east] at (-0.2,0.3) {32-bit integer};
\node[lab, anchor=east] at (-0.2,-0.9) {dotted decimal};
\node[tick] at (0.8,0.85) {most significant byte};
\end{tikzpicture}
\end{center}
```

Dotted-decimal notation writes each byte of the address in decimal, from the most significant byte down

:::

::: {#def-dns .definition name="Domain names and DNS"}

People use *domain names* such as `www.example.edu` instead of IP addresses. Domain names form a tree: the unnamed root, then first-level domains (`com`, `edu`, `org`, country codes), second-level domains assigned to organisations (`example.edu`), and below them names the organisation chooses. The *Domain Name System* (DNS) is a worldwide distributed database that maps domain names to IP addresses. The mapping can be one-to-one, many-to-one (several names for one address), one-to-many (one name for several addresses, often for load balancing), or a valid name may map to no address at all.

:::

::: {#fig-network-basics-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex, label={[tick]above:unnamed root}] (root) at (0,0) {};
\foreach \n/\x in {com/-3,edu/0,org/2.2,uk/4} { \node[box] (\n) at (\x,-1.2) {\texttt{\n}}; \draw (root) -- (\n); }
\node[box] (ex) at (-1.1,-2.4) {\texttt{example}}; \node[box] (mit) at (1.1,-2.4) {\texttt{mit}};
\draw (edu) -- (ex); \draw (edu) -- (mit);
\node[box] (www) at (-2.3,-3.6) {\texttt{www}}; \node[box] (cs) at (0,-3.6) {\texttt{cs}};
\draw (ex) -- (www); \draw (ex) -- (cs);
\node[hl box] (mail) at (0,-4.8) {\texttt{mail}}; \draw (cs) -- (mail);
\node[tick, anchor=west] at (0.7,-4.8) {\texttt{mail.cs.example.edu}};
\node[tick, anchor=east] at (-3.6,-1.2) {first level};
\node[tick, anchor=east] at (-2.2,-2.4) {second level};
\end{tikzpicture}
\end{center}
```

Part of the domain name tree; a name is read from a leaf up to the root

:::

::: {#def-internet-connection .definition name="Connections and ports"}

Clients and servers communicate over *connections*, which are

- *point-to-point*: they join a pair of processes;
- *full duplex*: data can flow in both directions at once;
- *reliable*: the bytes sent arrive, in the order sent.

An endpoint of a connection is a *socket*, identified by its *socket address* `address:port`, a 32-bit IP address and a 16-bit *port* number. A client's port is an *ephemeral port*, assigned automatically by the kernel when it connects; a server listens on a *well-known port* tied to its service, such as $80$ for the Web, $25$ for e-mail and $22$ for ssh. A connection is identified by its *socket pair*
$$(\textit{client address}:\textit{client port},\ \textit{server address}:\textit{server port}).$$

:::

::: {#fig-network-basics-6}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (-0.2,-0.7) rectangle (3.0,1.4); \node[lab] at (1.4,1.15) {client host};
\node[tick] at (1.4,0.75) {\texttt{128.2.194.242}};
\node[hl box] (cs) at (1.4,0.2) {socket \texttt{:51213}};
\draw[regionC] (6.6,-0.7) rectangle (10.4,1.4); \node[lab] at (8.5,1.15) {server host};
\node[tick] at (8.5,0.75) {\texttt{208.216.181.15}};
\node[hl box] (ss) at (8.5,0.2) {socket \texttt{:80}};
\draw[<->, emph, draw=accent] (cs) -- node[edge label, above] {connection} (ss);
\node[tick] at (5.0,-1.1) {socket pair (\texttt{128.2.194.242:51213}, \texttt{208.216.181.15:80})};
\node[tick] at (1.4,-0.4) {ephemeral port};
\node[tick] at (8.5,-0.4) {well-known port (Web)};
\end{tikzpicture}
\end{center}
```

A connection is identified by the socket addresses of its two endpoints

:::

::: {#fig-network-basics-7}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.9cm]
\foreach \x/\n in {0/client,6/server} {
  \draw[regionA] (\x-1.4,2.6) rectangle (\x+1.4,3.4); \node[lab] at (\x,3) {\n};
  \draw[box] (\x-1.4,1.7) rectangle (\x+1.4,2.3); \node[tick] at (\x,2) {sockets interface};
  \draw[hl box] (\x-1.4,0.8) rectangle (\x+1.4,1.4); \node[tick] at (\x,1.1) {TCP/IP (kernel)};
  \draw[regionC] (\x-1.4,-0.1) rectangle (\x+1.4,0.5); \node[tick] at (\x,0.2) {network adapter};
  \draw[->] (\x,2.6) -- (\x,2.3); \draw[->] (\x,1.7) -- (\x,1.4); \draw[->] (\x,0.8) -- (\x,0.5);
}
\draw[emph] (0,-0.1) -- (0,-0.6) -- (6,-0.6) -- (6,-0.1); \node[tick] at (3,-0.85) {global IP Internet};
\node[tick, anchor=west] at (7.6,2) {system calls};
\node[tick, anchor=west] at (7.6,1.1) {kernel code};
\node[tick, anchor=west] at (7.6,0.2) {hardware};
\end{tikzpicture}
\end{center}
```

Hardware and software organisation of an Internet application: programs use the sockets interface; the kernel implements TCP/IP and drives the network adapter

:::

::: {#rmk-network-basics-1 name="Tools"}

`hostname -i` prints the local host's address, `nslookup name` queries DNS for a domain name, and `ping`, `traceroute` test reachability and show the routers on the way. They show the properties of the DNS mapping directly: a popular site's name usually returns several addresses, and `localhost` always returns `127.0.0.1`.

:::
