::: {.problem #prob-cs221hw-6-q1 origin="external" source="cs221hw-6-q1"}
Let's consider a simple scenario which we can model using a Bayesian network. You are walking to CS221 lecture and, on the way, you notice the grass on the Stanford Oval is wet. You reason that this could be because either it rained (rare in beautiful and sunny Palo Alto), or the sprinklers were on. Letting your mind wander from the lecture, you decide to sit down and figure out what happened here by applying your knowledge of Bayesian networks.

We use three binary variables: $\text{Rain} = 1$ if it rained and $\text{Rain} = 0$ if it did not, $\text{Sprinkler} = 1$ if the sprinklers were on and $0$ if they were off, and $\text{WetGrass} = 1$ if the grass is wet and $0$ if it is dry. Assume that the sprinklers run independently of the weather: whether they were on does not depend on whether it rained.

(a) List the edges in the Bayesian network that is a causal model for why the grass on the Oval is wet. Use the variables $\text{Rain}$, $\text{Sprinkler}$, and $\text{WetGrass}$.

*Expected:* A list of edges in the Bayesian network, in the format of $\text{variable1} \rightarrow \text{variable2}$.

(b) Express the joint probability $\mathbb{P}(\text{Rain} = r, \text{Sprinkler} = s, \text{WetGrass} = w)$ in terms of local conditional probabilities.

*Expected:* An expression for the joint probability in terms of the local conditional probabilities (not a numerical value).

(c) Express $\mathbb{P}(\text{WetGrass} = 1)$, the probability that the grass is wet, in terms of local conditional probabilities.

*Expected:* An expression for $\mathbb{P}(\text{WetGrass} = 1)$ in terms of the local conditional probabilities (not a numerical value). You may write it as a sum over the values $r$ and $s$ of $\text{Rain}$ and $\text{Sprinkler}$.

(d) Assume $p(\text{Rain} = 1) = 0.2$, $p(\text{Sprinkler} = 1) = 0.5$, and the following local conditional probabilities that the grass is wet:

  $r$   $s$   $p(\text{WetGrass} = 1 \mid \text{Rain} = r, \text{Sprinkler} = s)$
  ------- ------- ---------------------------------------------------------------------------
  $1$   $1$   $0.9$
  $1$   $0$   $0.8$
  $0$   $1$   $0.7$
  $0$   $0$   $0.0$

What is $\mathbb{P}(\text{Rain} = 1, \text{Sprinkler} = 1, \text{WetGrass} = 0)$, the probability that it rained and the sprinklers were on, but the grass is not wet?

*Expected:* A numerical answer with brief calculations shown.

(e) Mark the following claims about this Bayesian network, with the probabilities from 1d, as true or false:

a.  $\text{Rain}$ and $\text{Sprinkler}$ are independent.
b.  $\text{Rain}$ and $\text{Sprinkler}$ are conditionally independent given $\text{WetGrass}$.
c.  $\mathbb{P}(\text{Rain} = 1 \mid \text{WetGrass} = 1) > \mathbb{P}(\text{Rain} = 1 \mid \text{WetGrass} = 1, \text{Sprinkler} = 1)$.

*Expected:* T/F for each claim. No justification needed.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::
