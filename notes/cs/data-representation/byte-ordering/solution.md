::: {.solution for="prob-byte-swap-code" status="draft"}
```{.c}
int get_byte(int x, int n) {
    return (x >> (n << 3)) & 0xFF;
}

int byte_swap(int x, int n, int m) {
    int sn = n << 3, sm = m << 3;
    unsigned u = x;                              /* unsigned: shifts into bit 31 are defined */
    unsigned bn = (u >> sn) & 0xFF, bm = (u >> sm) & 0xFF;
    unsigned clear = ~((0xFFu << sn) | (0xFFu << sm));
    return (int) ((u & clear) | (bn << sm) | (bm << sn));
}
```

1. Byte $n$ occupies bits $8n,\dots,8n+7$; `n << 3` is $8n$. Shifting right by $8n$ brings it to the bottom, and the mask `0xFF` removes everything above, including the copies of the sign bit an arithmetic shift brings in.
2. To swap, read both bytes, clear their two positions with a mask, and write each byte into the other's position. When $n=m$ both writes put the same byte back.
3. The work is done on an `unsigned` copy because shifting a $1$ into the sign bit of a signed `int` is undefined in C; converting back to `int` gives the intended bit pattern (@def-signed-unsigned-casts).
:::
