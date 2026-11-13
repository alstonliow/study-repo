<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-propositional-18 origin="external" source="fit1058-cn-4.21-q18"}
You have an unlimited supply of 2-input AND gates; outputs can feed other
gates. Show how to put AND gates together to compute the conjunction of
$x_1,\dots,x_8$. How many AND gates do you need?

If each gate takes time $t$ once both inputs are available, and all inputs
are available at time 0, how long does your circuit take? Try to minimise the
total time.
:::

::: {.problem #prob-propositional-19 origin="external" source="fit1058-cn-4.21-q19"}
Prove, by induction on $n$, that the conjunction of $2^n$ inputs can be
computed in time $nt$ by a suitable combination of AND gates. Hence prove
that the conjunction of $m$ arguments can be computed in time
$\lceil\log_2 m\rceil t$.
:::

::: {.problem #prob-propositional-22 origin="external" source="fit1058-cn-4.21-q22"}
Is the operation set $\{\oplus,\neg\}$ universal? Justify your answer.
:::

::: {.problem #prob-propositional-23 origin="external" source="fit1058-cn-4.21-q23"}
Prove or disprove: there exists a universal operation set containing just a
single operation (of at most two arguments). What type of proof did you use?
:::

::: {.problem #prob-propositional-24 origin="external" source="fit1058-cn-4.21-q24"}
Computer circuits actually perform the very same Boolean logic
that we have studied using *logic gates* (§ 4.4$\alpha$).
The idea is that you have one or more wires coming into a gate,
and usually one output wire. If an input wire has current flowing
through, the variable it represents is set to *True*, and
if not, then *False*. The logic gate then takes those
signals and gives off an output signal if the result should be
*True*, and no signal if the result is *False*.
Below are the most common logic gates seen in circuits.

The AND, OR, and NOT gates function the same as what we have seen
previously. If both signals of an AND gate are on, it will output
a signal. For OR, only one input signal is required to be on, and
for NOT, there will only be an output signal if the input signal
is off (*False*).

XOR is “EXCLUSIVE OR”, which outputs a signal only if $a$ or $b$
are on, but not both. NAND, NOR, and XNOR are simply the
inversions of AND, OR, and XOR respectively (i.e. NAND is “not
both”, NOR is “neither”, and XNOR is “both or neither”). These
gates can also be connected in series, like in the example below,
which is equivalent to the logical expression $(\neg a \vee \neg
    b)$.

```{=latex}
\begin{center}
    \begin{circuitikz}
        \draw (0,1) node[not port] (n1) {};
        \draw (0,-1) node[not port] (n2) {};
        \draw (2,0) node[nor port, number inputs=2] (g) {};
        \draw (n1.out) -| (g.in 1);
        \draw (n2.out) -| (g.in 2);
        \draw (n1.in) ++(-0.6,0) node[left]{$a$} -- (n1.in);
        \draw (n2.in) ++(-0.6,0) node[left]{$b$} -- (n2.in);
        \draw (g.out) -- ++(0.6,0);
    \end{circuitikz}
    \end{center}
```

(a) What single logic gate is the above circuit equivalent
    to?

(b) We saw in § 4.20, that $\{\vee, \wedge, \neg\}$ is a
    universal set of operations, meaning that any logical
    expression can be expressed with only these operations.
    How would you express the function of an XOR gate as a
    Boolean expression using only these operations?

(c) Draw a circuit diagram which performs the same
    functionality as an XOR gate using only AND, OR, and NOT
    gates.

(d) Do we even need three types of gates? Given that
    $\{\wedge, \vee, \neg\}$ is a universal set of operations,
    use De Morgan’s Law to prove that $\{\wedge, \neg\}$ and
    $\{\vee, \neg\}$ are also universal sets of operations.
    (Hint: Can you express $\vee$ with the other two
    operators?)

(e) Draw a circuit diagram that performs an OR operation
    using only AND and NOT gates, and also one which performs
    AND using only OR and NOT gates.

(f) Can you perform the function of a NOT gate, or an AND
    gate, with only NAND gates? What does this tell you about
    NAND gates?
:::
