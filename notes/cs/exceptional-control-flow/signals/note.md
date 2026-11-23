---
title: "Signals"
sources: [cmu15213-15, cmu15213lab-5]
requires: [cs/exceptional-control-flow/process-control]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 15 "Exceptional Control Flow: Signals and Nonlocal Jumps" and the Shell Lab handout, in our own wording; proofs written out in steps. -->

::: {#def-signal .definition name="Signal"}

A *signal* is a small message that notifies a process that an event of some type has occurred. It is identified by a small integer and carries no other data. The kernel sends signals on behalf of hardware exceptions and kernel events, and processes can ask the kernel to send them to other processes.

| number | name | default action | event |
|---|---|---|---|
| 2 | `SIGINT` | terminate | user typed Ctrl-C |
| 9 | `SIGKILL` | terminate | kill the process (cannot be caught or ignored) |
| 11 | `SIGSEGV` | terminate | invalid memory reference |
| 14 | `SIGALRM` | terminate | timer set by `alarm` expired |
| 17 | `SIGCHLD` | ignore | a child stopped or terminated |
| 20 | `SIGTSTP` | stop | user typed Ctrl-Z |

:::

::: {#def-pending-blocked .definition name="Sending, receiving, pending and blocked signals"}

A signal is *sent* (delivered) when the kernel updates some state in the destination's context, and *received* when the destination reacts to it: it ignores it, terminates, stops, or runs a *signal handler*. A signal that has been sent but not yet received is *pending*. For each process the kernel keeps a *pending* bit vector and a *blocked* bit vector (the *signal mask*), one bit per signal type. Sending signal $k$ sets bit $k$ of `pending`; receiving it clears the bit. A blocked signal can become pending but is not received until it is unblocked.

:::

::: {#prp-signals-not-queued .proposition name="Signals are not queued"}

At any moment a process has at most one pending signal of each type. If a signal of type $k$ is sent while one of type $k$ is already pending, the second one is discarded.

:::

::: {.proof}
1. The pending set is a bit vector with one bit per type.

2. Sending a type-$k$ signal sets bit $k$; if it is already $1$, the state does not change, so the second signal leaves no trace.

3. Hence the number of received type-$k$ signals can be smaller than the number sent, and a handler must not count signals to count events.
:::

::: {#fig-signals-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=east] at (-0.1,1.0) {\texttt{pending}};
\node[lab, anchor=east] at (-0.1,0.3) {\texttt{blocked}};
\foreach \k in {1,...,8} { \draw[cell frame] (\k*0.55-0.55,0.75) rectangle (\k*0.55,1.25); \draw[cell frame] (\k*0.55-0.55,0.05) rectangle (\k*0.55,0.55); \node[tick] at (\k*0.55-0.275,1.45) {\k}; }
\draw[hl cell] (1.1,0.75) rectangle (1.65,1.25); \node[tick] at (1.375,1.0) {1};
\draw[hl cell] (3.85,0.75) rectangle (4.4,1.25); \node[tick] at (4.125,1.0) {1};
\draw[regionA] (3.85,0.05) rectangle (4.4,0.55); \node[tick] at (4.125,0.3) {1};
\node[lab, anchor=west] at (4.8,1.0) {$\texttt{pnb}=\texttt{pending}\ \&\ \mathord{\sim}\texttt{blocked}$};
\node[lab, anchor=west] at (4.8,0.3) {signal 3 is received, signal 8 waits};
\end{tikzpicture}
\end{center}
```

Two pending signals, $3$ and $8$; signal $8$ is blocked, so on the next return to user mode only signal $3$ is received

:::

::: {#def-signal-receiving .definition name="When signals are received"}

When the kernel is about to return to user mode in process $p$ (after a system call, an interrupt or a context switch), it computes $\mathit{pnb}=\mathit{pending}\,\&\,\mathord{\sim}\mathit{blocked}$. If $\mathit{pnb}=0$ it returns to the next instruction of $p$. Otherwise it picks the lowest nonzero bit $k$, forces $p$ to receive signal $k$ (run its handler or take the default action), and repeats for the other bits before passing control back to $p$.

:::

::: {#def-process-groups-kill .definition name="Process groups and sending signals"}

Every process belongs to a *process group*, identified by a positive integer; a child starts in its parent's group, and `setpgid(pid, pgid)` changes it. `kill(pid, sig)` sends `sig` to process `pid`, or, if `pid` $<0$, to every process in group $|{\tt pid}|$. A shell puts each job into its own group; Ctrl-C at the keyboard makes the kernel send `SIGINT` to every process in the foreground group, and Ctrl-Z sends `SIGTSTP`.

:::

::: {#fig-signals-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (sh) at (3,2) {shell\\pid 10, pgid 10};
\node[box] (fg) at (0,0.4) {foreground job\\pid 20, pgid 20};
\node[box] (b1) at (3.6,0.4) {background job 1\\pgid 32};
\node[box] (b2) at (7.0,0.4) {background job 2\\pgid 40};
\node[box] (c1) at (-1.2,-1.2) {child\\pid 21};
\node[box] (c2) at (1.2,-1.2) {child\\pid 22};
\draw[->] (sh) -- (fg); \draw[->] (sh) -- (b1); \draw[->] (sh) -- (b2);
\draw[->] (fg) -- (c1); \draw[->] (fg) -- (c2);
\draw[draw=accent] (-2.2,-1.9) rectangle (2.2,1.0);
\node[tick, anchor=west] at (-2.1,1.25) {foreground process group 20: Ctrl-C sends \texttt{SIGINT} to all of it};
\end{tikzpicture}
\end{center}
```

A shell with one foreground job and two background jobs, each in its own process group; keyboard signals go to the whole foreground group

:::

::: {#def-signal-handler .definition name="Installing a handler"}

`signal(signum, handler)` (or the more precise `sigaction`) changes the action for `signum`: `SIG_IGN` ignores it, `SIG_DFL` restores the default, and the address of a function `void handler(int sig)` installs a *handler*, which is called when the process receives the signal. When the handler returns, control resumes where the process was interrupted. `SIGKILL` and `SIGSTOP` cannot be caught or ignored.

:::

::: {#exm-sigint-handler .example name="Catching Ctrl-C"}

```c
void sigint_handler(int sig) {
    const char msg[] = "So you think you can stop me?\n";
    write(STDOUT_FILENO, msg, sizeof msg - 1);   /* async-signal-safe output */
    _exit(0);
}

int main(void) {
    signal(SIGINT, sigint_handler);
    pause();                                      /* wait for a signal */
    return 0;
}
```

The handler runs *concurrently* with `main`, as a separate logical flow that interrupts it; this is why it uses `write` rather than `printf` (@def-async-signal-safe).

:::

::: {#fig-signals-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (0,2) -- (0,1.2); \node[tick, anchor=east] at (-0.1,1.6) {main program};
\node[dot] at (0,1.2) {}; \node[tick, anchor=east] at (-0.1,1.2) {$I_{\text{curr}}$};
\draw[->, draw=accent] (0.05,1.2) to[out=0,in=180] node[edge label, midway] {signal received} (2.5,0.9);
\draw[emph, draw=accent] (2.5,0.9) -- (2.5,0.1); \node[tick, anchor=west] at (2.6,0.5) {handler};
\draw[->, dashed] (2.45,0.1) to[out=180,in=0] node[edge label, midway] {handler returns} (0.05,-0.2);
\draw[emph] (0,-0.2) -- (0,-0.9); \node[tick, anchor=east] at (-0.1,-0.2) {$I_{\text{next}}$};
\end{tikzpicture}
\end{center}
```

A handler is a separate flow: it interrupts the main program between two instructions and returns to the next one

:::
