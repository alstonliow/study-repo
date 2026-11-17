::: {.problem #prob-cs70hw-2-q4 origin="external" source="cs70hw-2-q4"}
**Nothing Can Be Better Than Something.** In the stable matching problem, suppose that some jobs and candidates have hard requirements and might not be able to just settle for anything. In other words, in addition to the preference orderings they have, they prefer being unmatched to being matched with some of the lower-ranked entities (in their own preference list). We will use the term entity to refer to a candidate/job. A matching could ultimately have to be partial, i.e., some entities would and should remain unmatched.

Consequently, the notion of stability here should be adjusted a little bit to capture the autonomy of both jobs to unilaterally fire employees and employees to just walk away. A matching is stable if

- there is no matched entity who prefers being unmatched over being with their current partner;
- there is no matched/filled job and unmatched candidate that would both prefer to be matched with each other over their current status;
- similarly, there is no unmatched job and matched candidate that would both prefer to be matched with each other over their current status;
- there is no matched job and matched candidate that would both prefer to be matched with each other over their current partners; and
- there is no unmatched job and unmatched candidate that would both prefer to be with each other over being unmatched.

(a) Prove that a stable pairing still exists in the case where we allow unmatched entities.

(HINT: You can approach this by introducing imaginary/virtual entities that jobs/candidates "match" if they are unmatched. How should you adjust the preference lists of jobs/candidates, including those of the newly introduced imaginary ones for this to work?)

(b) As you saw in the lecture, we may have different stable matchings. But interestingly, if an entity remains unmatched in one stable matching, it/she must remain unmatched in any other stable matching as well. Prove this fact by contradiction.

*Note (these notes):* Solution (a) uses an algorithm instead of the virtual entities suggested by the hint; both approaches work.
:::

::: {.problem #prob-cs70hw-2-q5 origin="external" source="cs70hw-2-q5"}
**The Ranking List.** Let's study the stable matching problem a little bit quantitavely. Here we define the following notation: on day $j$, let $P_j(M)$ be the rank of the job that applicant $M$ proposes to (where the first application on her list has rank 1 and the last has rank $n$). Also, let $R_j(W)$ be the total number of applicants that job $W$ has rejected up through day $j - 1$ (i.e. not including the proposals on day $j$). Answer the following questions using the notation above.

(a) Prove or disprove the following claim: $\sum_M P_j(M) - \sum_W R_j(W)$ is independent of $j$. If it is true, also give the value of $\sum_M P_j(M) - \sum_W R_j(W)$. The notation, $\sum_M$ and $\sum_W$, simply means that we are summing over all applicants and all jobs.

(b) Prove or disprove the following claim: one of the applicants or jobs must be matched to something that is ranked in the top half of their preference list. You may assume that $n$ is even.

*Note (these notes):* In this problem the applicants propose to the jobs, the opposite of the notes; the results hold with the roles exchanged.
:::
