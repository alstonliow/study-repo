---
title: "Processes and Context Switches"
sources: [cmu15213-14, cmu15213r-14]
requires: [cs/exceptional-control-flow/exceptions]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 14 "Exceptional Control Flow: Exceptions and Processes", in our own wording. -->

::: {#def-process .definition name="Process"}

A *process* is an instance of a running program. It gives the program two illusions:

- a *logical control flow*: the program seems to have the processor to itself;
- a *private address space*: the program seems to have the memory to itself (@def-x86-64-linux-layout).

The state the kernel keeps for a process, its *context*, includes the registers, the program counter, the address space (page tables, @def-page-table), the open files (@def-descriptor-table) and kernel bookkeeping such as the process ID.

:::

::: {#def-concurrent-flows .definition name="Concurrent flows"}

Two processes (more generally, two logical flows) *run concurrently* if their executions overlap in time, that is, one starts before the other finishes; otherwise they run *sequentially*. Concurrency is about overlap in time, not about running at the same instant: on one core, concurrent flows take turns. Flows that run at the same instant on different cores run in *parallel*.

:::

::: {#fig-processes-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm]
\draw[->] (0,-0.4) -- (9,-0.4) node[lab, right] {time};
\foreach \n/\y in {A/2.0,B/1.2,C/0.4} { \node[lab, anchor=east] at (-0.2,\y) {process \n}; }
\draw[emph, draw=primary] (0.5,2.0) -- (2,2.0); \draw[emph, draw=primary] (4.5,2.0) -- (5.5,2.0);
\draw[emph, draw=accent] (2,1.2) -- (3.2,1.2);
\draw[emph, draw=primary] (3.2,0.4) -- (4.5,0.4); \draw[emph, draw=primary] (5.5,0.4) -- (7,0.4);
\foreach \x in {2,3.2,4.5,5.5} { \draw[faint, dashed] (\x,0.1) -- (\x,2.3); }
\node[tick, align=left, anchor=west] at (7.2,1.2) {A, B concurrent\\A, C concurrent\\B, C sequential};
\end{tikzpicture}
\end{center}
```

Three processes sharing one core. A and C overlap in time and run concurrently; B runs entirely between two pieces of A, so A and B are also concurrent, while B and C are sequential

:::

::: {#def-user-kernel-mode .definition name="User and kernel mode"}

The processor has a *mode bit*. In *kernel mode* a program may execute every instruction and access every memory location; in *user mode* it may not execute privileged instructions (halt the processor, change the mode bit, start I/O) or touch kernel memory. A process runs application code in user mode and enters kernel mode only through an exception: an interrupt, a fault, or a system call.

:::

::: {#def-context-switch .definition name="Context switch"}

The kernel decides when to stop the current process and resume another one (*scheduling*). It does so by a *context switch*: (1) save the context of the current process, (2) restore the saved context of the chosen process, (3) pass control to it. A context switch can happen only while the kernel runs on behalf of some process, for example during a system call that must wait for a disk, or in the handler of the periodic timer interrupt (every few milliseconds), which keeps one process from monopolising the processor.

:::

::: {#fig-processes-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (0,2.6) {process A}; \node[lab] at (3,2.6) {process B};
\draw[emph] (0,2.3) -- (0,1.7); \node[tick, anchor=east] at (-0.1,2.0) {user code};
\draw[emph, draw=accent] (0,1.7) -- (1.5,1.4); \node[tick, anchor=west] at (1.6,1.55) {kernel code: \texttt{read} traps, context switch};
\draw[emph] (3,1.4) -- (3,0.6); \node[tick, anchor=west] at (3.1,1.0) {user code};
\draw[emph, draw=accent] (3,0.6) -- (1.5,0.3); \node[tick, anchor=west] at (1.6,0.25) {kernel code: disk interrupt, context switch};
\draw[emph] (0,0.3) -- (0,-0.4); \node[tick, anchor=east] at (-0.1,-0.05) {user code (\texttt{read} returns)};
\draw[->] (5.9,2.3) -- (5.9,-0.4) node[midway, right, tick] {time};
\end{tikzpicture}
\end{center}
```

Process A calls `read`; while the disk works, the kernel switches to B; the disk's interrupt later lets the kernel switch back, and `read` returns in A

:::

::: {#def-error-handling .definition name="Error reporting by system calls"}

Unix system-level functions report an error by returning $-1$ and setting the global variable `errno` to a code; `strerror(errno)` describes it. Every call should be checked. A common style wraps each function in an upper-case version that prints a message and exits on error:

```c
pid_t Fork(void) {
    pid_t pid = fork();
    if (pid < 0) { fprintf(stderr, "fork error: %s\n", strerror(errno)); exit(1); }
    return pid;
}
```

:::

::: {#rmk-processes-1 name="Threads share the context"}

Several *threads* can run inside one process: each has its own logical flow (registers, program counter, stack) but they share the address space and the open files (@def-thread). A thread switch therefore saves and restores less than a process switch.

:::
