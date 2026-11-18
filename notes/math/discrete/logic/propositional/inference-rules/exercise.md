::: {.problem #prob-cs221hw-7-q7 origin="external" source="cs221hw-7-q7"}
Two important properties in logic-based systems are soundness and completeness. A system is sound if everything that is provable (derivable) is in fact true whereas a system is complete if everything that is true has a proof (derivation).

- **Definition of Soundness:** A set of inference rules $Rules$ is sound if: $\{f: KB \vdash f\} \subseteq \{f: KB \vDash f\}$
- **Definition of Completeness:** A set of inference rules $Rules$ is complete if: $\{f: KB \vdash f\} \supseteq \{f: KB \vDash f\}$

(a) A hospital uses an LLM to query electronic health records. The hospital policy says that a use case is permitted when all the following conditions are met:

1.  the affected patients have consented: $\mathrm{Consented}(x)$
2.  the use case is classified as *Beneficial* or *Neutral*: $\mathrm{Beneficial}(x) \lor \mathrm{Neutral}(x)$
3.  the use case is not both *Harmful* and *HighRisk*: $\neg(\mathrm{Harmful}(x) \land \mathrm{HighRisk}(x))$

An intern plans to implement a logic-based policy checker for the LLM. We can define the policy checker as *sound* relative to the hospital's policy if every use case it allows is permitted by the policy, and define it as *complete* if it allows every use case permitted by the policy.

The intern implemented the following policy checker: $$\mathrm{Permitted}(x) \Longleftrightarrow \mathrm{Consented}(x) \land \mathrm{Beneficial}(x) \land \neg(\mathrm{Harmful}(x) \land \mathrm{HighRisk}(x)).$$

Consider the following 2 cases:

- ***Case1*:** A clinician wants to publish a case report. The patient provided consent, and the report could benefit other clinicians, but it contains personally identifiable information that could expose the patient to serious privacy risk. $$\mathrm{Consented}(\mathit{Case1}),\ \mathrm{Beneficial}(\mathit{Case1}),\ \mathrm{Harmful}(\mathit{Case1}),\ \mathrm{HighRisk}(\mathit{Case1}).$$
- ***Case2*:** A graduate student wants to conduct exploratory research on anonymized patient health records, and the patients consented. No concrete benefit has been confirmed, but no significant harm or serious risk has been identified. $$\begin{aligned} &\mathrm{Consented}(\mathit{Case2}),\ \neg\mathrm{Beneficial}(\mathit{Case2}),\ \mathrm{Neutral}(\mathit{Case2}),\\ &\neg\mathrm{Harmful}(\mathit{Case2}),\ \neg\mathrm{HighRisk}(\mathit{Case2}). \end{aligned}$$

(a.i) Is the policy checker *sound*? Is it *complete*? Explain by comparing the checker's formula to the hospital's policy, and say which of the two defined cases the checker and the policy disagree on.

*Expected:* 2-3 sentences determining soundness and completeness by comparing the checker's formula to the hospital's policy, and identifying which defined case the checker and the policy disagree on.

Imagine you are choosing between two proof-based systems. System A is sound but not complete. System B is complete but not sound. Assume the only difference between System A and System B is the difference between soundness and completeness.

(b) You want to deploy one of these systems in a safety-critical setting, where acting on a false conclusion has severe consequences. Which system would you choose and why?

*Expected:* 2-3 sentences explaining your choice, tying in the definitions of soundness and completeness. You may use either natural language or mathematical notation in your answer.

(c) Imagine you are in a setting where you have a separate verifier system that can validate hypotheses (e.g., a human in the loop that inspects the hypotheses). You want to capture as much true information as possible in this setting. Which system would you choose and why?

*Expected:* 2-3 sentences explaining your choice, tying in the definitions of soundness and completeness. You may use either natural language or mathematical notation in your answer.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::
