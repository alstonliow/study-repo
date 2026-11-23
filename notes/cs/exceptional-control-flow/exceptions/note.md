---
title: "Exceptions and System Calls"
sources: [cmu15213-14]
requires: [cs/machine-level/procedures-and-the-stack]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 14 "Exceptional Control Flow: Exceptions and Processes", first part, in our own wording. -->

From power-on to shutdown a processor executes one instruction after another: its *control flow*. Jumps, calls and returns change that flow in response to the program's own state. Systems must also react to changes in *system* state: a packet arrives, a key is pressed, a division by zero happens, a child process ends. *Exceptional control flow* (ECF) is the set of mechanisms for this, at every level of the system.

::: {#def-exception .definition name="Exception"}

An *exception* is a transfer of control to the operating system *kernel* in response to an *event*, a change in the processor's state. When the event occurs, the processor stops the current instruction stream and makes an indirect call, through the *exception table*, to an *exception handler* in the kernel. After the handler finishes, control either returns to the instruction that was running ($I_{\text{curr}}$), returns to the next one ($I_{\text{next}}$), or the program is aborted.

:::

::: {#def-exception-table .definition name="Exception table"}

Each kind of event has an *exception number* $k$, assigned by the processor designers (division by zero, page fault, …) or by the kernel (system calls, external interrupts). At boot the kernel fills the *exception table*, an array whose entry $k$ is the address of the handler for exception $k$; a special register holds the table's start address.

:::

::: {#fig-exceptions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=south] at (1,1.7) {user code};
\draw[emph] (1,1.6) -- (1,0.4);
\node[dot] at (1,1.0) {}; \node[tick, anchor=east] at (0.9,1.0) {$I_{\text{curr}}$};
\node[tick, anchor=east] at (0.9,0.55) {$I_{\text{next}}$};
\node[lab, anchor=south] at (5.2,1.7) {exception handler (kernel)};
\draw[emph, draw=accent] (5.2,1.3) -- (5.2,-0.2);
\draw[->, draw=accent] (1.05,1.0) to[out=10,in=170] node[edge label, midway] {event: exception $k$} (5.15,1.3);
\draw[->, dashed] (5.15,-0.2) to[out=190,in=-20] node[edge label, midway] {return (optional)} (1.05,0.5);
\foreach \k [count=\i from 0] in {0,1,2,\dots} { \draw[cell frame] (8,1.3-\i*0.45) rectangle (9.4,1.72-\i*0.45); \node[tick] at (8.7,1.51-\i*0.45) {$\k$}; }
\node[tick] at (8.7,2.0) {exception table};
\draw[->] (8,1.06) -- (5.3,1.25);
\end{tikzpicture}
\end{center}
```

An exception: event $k$ makes the processor call the handler whose address is in entry $k$ of the exception table; the handler may return to the interrupted program

:::

::: {#def-exception-classes .definition name="Classes of exceptions"}

| class | cause | sync? | returns to |
|---|---|---|---|
| interrupt | signal from an I/O device or timer | asynchronous | $I_{\text{next}}$ |
| trap | intentional, an instruction such as `syscall` | synchronous | $I_{\text{next}}$ |
| fault | a possibly recoverable error, e.g. page fault | synchronous | $I_{\text{curr}}$ (re-executed) or abort |
| abort | an unrecoverable error, e.g. a hardware parity error | synchronous | never |

*Asynchronous* exceptions are caused by events outside the processor, independent of the current instruction; *synchronous* exceptions are caused by executing an instruction.

:::

::: {#def-system-call .definition name="System call"}

A *system call* is a trap that requests a kernel service: reading a file, creating a process, loading a program, ending the process. On x86-64 Linux, the program puts the call number in `%rax` and up to six arguments in `%rdi`, `%rsi`, `%rdx`, `%r10`, `%r8`, `%r9`, and executes `syscall`; the result comes back in `%rax`, a negative value in $[-4095,-1]$ meaning an error. The C library wraps each system call in a function (`read`, `fork`, `execve`, `_exit`, …).

:::

::: {#exm-open-syscall .example name="Opening a file"}

The C call `open(filename, options)` executes, inside the library wrapper,

```text
    movl    $2, %eax          system call number 2 is open
    syscall                   trap into the kernel
    cmpq    $-4095, %rax      a value in [-4095, -1] is -errno
    jae     __error_handler
```

The kernel opens the file and returns a descriptor (@def-file-descriptor) in `%rax`.

:::

::: {#exm-page-fault-and-segfault .example name="Faults"}

- A *page fault*: a program writes to a page that is not in main memory. The handler loads the page from disk (@def-page-fault) and returns to the faulting instruction, which now succeeds.
- An *invalid memory reference*: a program writes to an address that belongs to no valid area. The handler finds no page to load, sends the process the signal `SIGSEGV` (@def-signal), and the process ends with "segmentation fault".

:::

::: {#fig-exceptions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (1,1.8) {user code}; \node[lab] at (5,1.8) {kernel};
\node[box] (i) at (1,1.0) {\texttt{movl \%eax,0x8049d10}};
\node[box] (h) at (5,0.3) {page fault handler:\\copy page from disk};
\draw[->, draw=accent] (i.east) to[out=0,in=160] node[edge label, pos=0.4] {fault} (h.north west);
\draw[->, dashed] (h.west) to[out=180,in=-30] node[edge label, pos=0.5] {return to $I_{\text{curr}}$} (i.south);
\end{tikzpicture}
\end{center}
```

A page fault is handled and the faulting instruction runs again, this time successfully

:::

::: {#rmk-exceptions-1 name="ECF at every level"}

Exceptions are the hardware level. Above it, the kernel uses them to switch between *processes* (@def-process); the kernel and processes use *signals* to notify processes of events (@def-signal); and within a program, *nonlocal jumps* (`setjmp`/`longjmp`, @def-nonlocal-jump) and C++/Java exceptions transfer control out of nested calls. The notes of this branch go up these levels.

:::
