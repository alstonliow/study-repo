::: {#prob-how-many-bits-code .problem .coding origin="adapted" source="res-cmu-15213-labs-data-lab" tags="bit-manipulation,twos-complement"}
Write `how_many_bits(x)`, which returns the smallest width $w$ such that $x$ is representable in $w$-bit two's complement, that is, $TMin_w\le x\le TMax_w$ (@def-twos-complement-encoding). For example $12$ needs $5$ bits ($01100$), $-5$ needs $4$ ($1011$), and both $0$ and $-1$ need $1$. Use only `! ~ & ^ | + << >>`, no control flow and no loops; about 90 operators are enough.

```{.c .starter}
int how_many_bits(int x) {
    return 0;
}
```

```{.c .tests}
void test_examples(void) {
    assert(how_many_bits(12) == 5);
    assert(how_many_bits(298) == 10);
    assert(how_many_bits(-5) == 4);
    assert(how_many_bits(0) == 1);
    assert(how_many_bits(-1) == 1);
}

void test_extremes(void) {
    assert(how_many_bits(INT_MIN) == 32);
    assert(how_many_bits(INT_MAX) == 32);
    assert(how_many_bits(1) == 2);
    assert(how_many_bits(-2) == 2);
}

static int slow_bits(long long x) {
    for (int w = 1; w <= 32; w++)
        if (-(1LL << (w - 1)) <= x && x <= (1LL << (w - 1)) - 1) return w;
    return -1;
}

void test_against_definition(void) {
    unsigned s = 7;
    for (int i = 0; i < 2000; i++) {
        s = s * 1103515245u + 12345u;
        int x = (int) s >> (s % 31);
        assert(how_many_bits(x) == slow_bits(x));
    }
}
```
:::
