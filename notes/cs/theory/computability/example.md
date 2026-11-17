<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 12 (source key cs70-12, in note.md); the second example is our own. -->

::: {#exm-quine-construction .example name="Building a self-printing instruction" level="easy"}
Treat English instructions as programs.

1. The instruction "Copy the next line: ⟨Copy the next line:⟩" outputs only one line, *Copy the next line:*, so it is not its own output.

2. "Copy the next line twice: ⟨Copy the next line twice:⟩" outputs that line twice, but without the brackets the second time.

3. "Copy the next line twice, the second time in brackets: ⟨Copy the next line twice, the second time in brackets:⟩" outputs exactly its own two lines.

The pattern is a program made of an instruction $s$ together with a quoted copy of $s$, where $s$ says: print the quoted text, then print it again in quotes. In a pseudocode where $(\mathrm{Q}\ \text{"}s\text{"})$ runs $\mathrm{Q}$ on the string $s$, define $\mathrm{Quine}(s)$ to output $(s\ \text{"}s\text{"})$. Then $(\mathrm{Quine}\ \text{"Quine"})$ outputs $(\mathrm{Quine}\ \text{"Quine"})$, which is the instruction itself.
:::

::: {#exm-prints-something-undecidable .example name="Does a program ever print anything?" level="medium"}
No program decides, for every program $P$ and input $x$, whether $P$ prints at least one symbol when run on $x$.

1. Suppose, for contradiction, that a program $\mathrm{TestPrints}$ does this.

2. Given $P$ and $x$, let $P''$ be the program that, on any input, runs $P$ on $x$ with every print instruction removed, and then prints "done". This change to the text of $P$ is mechanical.

3. $P''$ prints something if and only if the run of $P$ on $x$ ends, that is, if and only if $P$ halts on $x$.

4. So "build $P''$, then return $\mathrm{TestPrints}(P'',0)$" decides the halting problem, contradicting @thm-halting-undecidable. This is a reduction (@def-reduction).
:::
