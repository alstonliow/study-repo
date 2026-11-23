<!-- Solutions marked status="draft" on Sipser problems were written by Claude in our own words;
     18.404J publishes no problem-set solutions and the book's Selected Solutions were not read.
     Owner to review, then remove status. -->

::: {.solution for="prob-sipser3e-6-q1" status="draft"}
A Python program that prints itself:

```python
s = 's = %r\nprint(s %% s)'
print(s % s)
```

1. *The two parts.* The first line plays the role of part $A$ in the proof of the recursion theorem: it stores a description of the rest of the program as data, the string `s`. The second line plays the role of part $B$: it builds the whole program from that description.

2. *Why it works.* `%r` inserts the quoted form of `s`, which reproduces the first line, and `%%` becomes `%`. So `s % s` is exactly the source text, and the program prints it.
:::
