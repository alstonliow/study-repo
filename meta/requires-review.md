# requires review (2026-11-15)

Draft by Claude: direct prerequisites only, no cycles, nothing implied by another entry,
never a later topic in course order. Old values are the migrated ones. Tell Claude what to
change; delete this file after the review (it is not meant to be committed).

| Note | Old requires | New requires | Reason |
|---|---|---|---|
| sets/sets-and-elements | sets/cardinality-and-standard-sets | — | first topic |
| sets/cardinality-and-standard-sets | — | sets/sets-and-elements | size and standard sets of a set |
| sets/subsets | — | sets/sets-and-elements | subset compares two sets |
| sets/power-set | — | sets/subsets, sets/cardinality-and-standard-sets | set of all subsets; counts them |
| sets/set-operations | — | sets/subsets | operations defined via membership and subsets |
| sets/symmetric-difference | — | sets/set-operations | built from difference and union |
| sets/cartesian-product | sets/cardinality-and-standard-sets | sets/cardinality-and-standard-sets | ordered pairs; |A x B| |
| sets/partitions | relations/equivalence-relations | sets/set-operations | disjoint union that covers the set |
| functions/definitions | functions/injections-surjections-bijections | sets/cartesian-product | a function is a set of ordered pairs |
| functions/special-functions | functions/definitions, functions/inverse-functions | functions/definitions | examples and restrictions of functions |
| functions/injections-surjections-bijections | — | functions/definitions | properties of a function |
| functions/inverse-functions | — | functions/injections-surjections-bijections | inverse exists iff bijection |
| functions/composition | functions/injections-surjections-bijections, functions/inverse-functions | functions/inverse-functions | composition with inverses; preserves injections |
| functions/cryptosystems | functions/composition | functions/composition | composing encryption functions |
| functions/counting | functions/injections-surjections-bijections | functions/injections-surjections-bijections | counts functions, injections, bijections |
| relations/binary-relations | functions/inverse-functions, functions/special-functions, relations/combining | functions/definitions | relations generalise functions (subsets of A x B) |
| relations/properties | — | relations/binary-relations | reflexive, symmetric, transitive, ... |
| relations/combining | functions/composition | relations/properties, functions/composition | composition and transitive closure |
| relations/equivalence-relations | — | relations/properties, sets/partitions | classes form a partition |
| relations/counting | sets/cartesian-product, sets/power-set | relations/binary-relations, sets/power-set | relations are subsets of A x B: 2^(mn) |
| proof/theorems-and-proofs | sets/subsets | sets/power-set | first example proves a power-set fact |
| proof/finding-proofs | proof/contradiction, proof/induction, proof/techniques, proof/theorems-and-proofs, sets/subsets | proof/theorems-and-proofs | strategies for writing proofs |
| proof/techniques | proof/finding-proofs | proof/finding-proofs | manipulation, construction, cases |
| proof/contradiction | — | proof/finding-proofs | another proof type |
| proof/induction | proof/induction-examples, sets/set-operations, proof/contradiction | proof/contradiction, sets/set-operations | well-ordering argument by contradiction; De Morgan example |
| proof/induction-examples | — | proof/induction | more induction proofs |
| proof/induction-extended-example | relations/binary-relations | proof/induction-examples, relations/binary-relations, functions/injections-surjections-bijections | injections inside a relation, by induction |
| logic/propositional/propositions | — | — | first logic topic |
| logic/propositional/connectives | logic/propositional/implication-and-equivalence, sets/set-operations | logic/propositional/propositions | combine propositions |
| logic/propositional/de-morgans-laws | logic/propositional/connectives, logic/propositional/tautologies, sets/set-operations | logic/propositional/connectives | negating and/or |
| logic/propositional/implication-and-equivalence | sets/subsets, sets/symmetric-difference | logic/propositional/connectives | more connectives |
| logic/propositional/tautologies | — | logic/propositional/implication-and-equivalence | equivalence of expressions |
| logic/propositional/laws-of-boolean-algebra | — | logic/propositional/tautologies, logic/propositional/de-morgans-laws | list of equivalences |
| logic/propositional/normal-forms | — | logic/propositional/laws-of-boolean-algebra | rewriting into DNF/CNF |
| logic/propositional/representing-statements | — | logic/propositional/normal-forms | encode statements in CNF |
| logic/propositional/universal-sets-of-operations | logic/propositional/normal-forms | logic/propositional/normal-forms | universality via DNF/CNF |
| logic/predicate/predicates | functions/special-functions, relations/binary-relations, relations/counting | logic/propositional/connectives, relations/binary-relations | truth-valued functions and relations |
| logic/predicate/quantifiers | logic/propositional/laws-of-boolean-algebra, sets/subsets | logic/predicate/predicates | quantify a predicate |
| logic/predicate/multiple-quantifiers | — | logic/predicate/quantifiers | nested quantifiers |
| logic/predicate/logic-with-quantifiers | logic/predicate/multiple-quantifiers, logic/predicate/quantifiers | logic/predicate/multiple-quantifiers, logic/propositional/laws-of-boolean-algebra | rules combine quantifiers with Boolean laws |
| sequences/basic-sequences | sequences/sums-and-series, sets/cartesian-product, sets/sets-and-elements | functions/definitions | a sequence is a function on N |
| sequences/solving-recurrences | sequences/sums-and-series | sequences/basic-sequences, proof/induction | formulas proved by induction |
| sequences/fibonacci | — | sequences/solving-recurrences | a recurrence and its formula |
| sequences/limits | logic/predicate/multiple-quantifiers, proof/induction-examples | sequences/basic-sequences, logic/predicate/multiple-quantifiers, proof/induction-examples | epsilon-N definition; Bernoulli's inequality |
| sequences/big-o | logic/propositional/representing-statements, sequences/sums-and-series | sequences/limits | growth beyond limits |
| sequences/sums-and-series | proof/induction-examples, sequences/limits | sequences/limits | infinite series need limits; sums by induction |
| number-theory/divisibility-and-primes | number-theory/coprimality, number-theory/diffie-hellman | proof/induction | prime factorisation by induction |
| number-theory/remainders-and-parity | — | number-theory/divisibility-and-primes | division with remainder |
| number-theory/gcd-and-euclidean-algorithm | number-theory/coprimality, number-theory/divisibility-and-primes | number-theory/remainders-and-parity | Euclid uses remainders |
| number-theory/extended-euclidean-algorithm | number-theory/divisibility-and-primes, number-theory/remainders-and-parity | number-theory/gcd-and-euclidean-algorithm | extends Euclid |
| number-theory/coprimality | number-theory/divisibility-and-primes, number-theory/extended-euclidean-algorithm | number-theory/extended-euclidean-algorithm | Bezout characterisation |
| number-theory/modular-arithmetic | number-theory/coprimality, number-theory/modular-exponentiation | number-theory/coprimality, relations/equivalence-relations | congruence is an equivalence; inverses need coprimality |
| number-theory/euler-totient | number-theory/modular-arithmetic | number-theory/modular-arithmetic | counts units mod n |
| number-theory/modular-exponentiation | number-theory/coprimality, number-theory/euler-totient, number-theory/modular-arithmetic | number-theory/euler-totient | Euler's theorem |
| number-theory/primitive-roots | number-theory/coprimality, number-theory/diffie-hellman, number-theory/modular-exponentiation | number-theory/modular-exponentiation | orders of powers |
| number-theory/diffie-hellman | number-theory/modular-exponentiation, number-theory/primitive-roots, sequences/big-o | number-theory/primitive-roots | uses a primitive root |
| counting/sum-and-product-rules | — | sets/set-operations, functions/injections-surjections-bijections | disjoint unions, products (via bijections), bijection rule |
| counting/inclusion-exclusion | counting/combinations | counting/sum-and-product-rules, proof/induction | general formula proved by induction |
| counting/derangements | counting/inclusion-exclusion, counting/sum-and-product-rules | counting/inclusion-exclusion, functions/counting | counts bijections without fixed points |
| counting/selection | counting/sum-and-product-rules | counting/sum-and-product-rules, functions/counting | ordered selection counts functions/injections |
| counting/combinations | counting/selection, counting/sum-and-product-rules | counting/selection, sets/power-set | binomial coefficients |
| counting/stars-and-bars | counting/combinations, counting/selection, counting/sum-and-product-rules | counting/combinations | reduces to binomial coefficients |
| probability/sample-spaces | sequences/sums-and-series | counting/sum-and-product-rules, sequences/sums-and-series | equally likely outcomes; infinite spaces |
| probability/events | counting/inclusion-exclusion | probability/sample-spaces, counting/inclusion-exclusion | inclusion-exclusion for probabilities |
| probability/conditional-probability | — | probability/events | probability of events given events |
| probability/bayes-theorem | sets/partitions | probability/conditional-probability, sets/partitions | law of total probability over a partition |
| probability/random-variables | probability/conditional-probability | probability/conditional-probability | functions on outcomes; independence |
| probability/expectation-and-variance | — | probability/random-variables | summaries of a random variable |
| probability/standard-distributions | counting/combinations, sequences/sums-and-series | probability/expectation-and-variance, counting/combinations | binomial etc.; their mean and variance |
| probability/coupon-collector | sequences/sums-and-series | probability/standard-distributions | geometric waiting times |
| graph/basic-definitions | graph/connectivity | sets/set-operations | a graph is a pair of sets |
| graph/representing-graphs | functions/special-functions, graph/basic-definitions, relations/binary-relations | graph/basic-definitions, relations/binary-relations | matrices, lists; graphs as relations |
| graph/special-graphs | graph/degree | graph/basic-definitions | named families of graphs |
| graph/degree | graph/basic-definitions | graph/special-graphs | degrees, with special graphs as examples |
| graph/walks-paths-cycles | — | graph/basic-definitions | moving around a graph |
| graph/connectivity | graph/basic-definitions, relations/equivalence-relations | graph/walks-paths-cycles, relations/equivalence-relations | components are equivalence classes |
| graph/bipartite-graphs | graph/walks-paths-cycles | graph/walks-paths-cycles | odd cycles |
| graph/euler-and-hamilton | graph/degree, graph/walks-paths-cycles | graph/connectivity, graph/degree | Euler tours need connectivity and even degrees |
| graph/trees | — | graph/connectivity | minimal connected graphs |
| graph/forests-and-spanning-trees | graph/walks-paths-cycles | graph/trees | collections of trees |
| graph/planarity | — | graph/trees, graph/degree | Euler's formula from trees; edge bounds from degrees |
| graph/games-on-graphs | — | graph/forests-and-spanning-trees | spanning trees decide the game |
