::: {.solution for="prob-blocked-transpose-code" status="draft"}
```{.c}
static long cache_tag[32], misses;           /* simulated cache: tag per set, -1 = empty */

static void touch(long addr) {
    long blk = addr >> 5, set = blk & 31, tag = blk >> 5;
    if (cache_tag[set] != tag) { misses++; cache_tag[set] = tag; }
}
static int get_a(const int *A, int n, int i, int j) { touch(4L * (i * n + j)); return A[i * n + j]; }
static void set_b(int *B, int n, int i, int j, int v) { touch(4096 + 4L * (i * n + j)); B[i * n + j] = v; }

void transpose(int n, const int *A, int *B) {
    const int bs = 8;                         /* 8 ints = one 32-byte cache block */
    for (int ii = 0; ii < n; ii += bs)
        for (int jj = 0; jj < n; jj += bs)
            for (int i = ii; i < ii + bs && i < n; i++)
                for (int j = jj; j < jj + bs && j < n; j++)
                    set_b(B, n, j, i, get_a(A, n, i, j));
}
```

1. Work tile by tile with $8\times8$ tiles. One row of a tile of $A$ is exactly one $32$-byte cache block, so reading it along its row costs one miss.
2. The tile of $B$ that receives it has $8$ rows, which are $32$ ints $=128$ bytes apart, so they map to $8$ different sets of the $32$-set cache and can all stay cached while the tile is processed: each of the $8$ blocks of the $B$ tile is loaded about once per tile instead of once per element.
3. A tile therefore costs about $16$ misses, and there are $16$ tiles, around $256$; the diagonal tiles add some more because there the rows of $A$ and $B$ fall into the same sets and evict each other. The simulation gives $340$ misses for $n=32$.
4. The conditions `i < n` and `j < n` clip the last tiles, so any $n$ works.
:::
