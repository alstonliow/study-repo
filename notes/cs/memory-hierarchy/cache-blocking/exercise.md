::: {#prob-blocked-transpose-code .problem .coding origin="adapted" source="res-cmu-15213-labs-cache-lab" tags="caches,blocking"}
Write `transpose(n, A, B)`, which sets $B[j][i]=A[i][j]$ for the $n\times n$ row-major `int` matrices `A` and `B`, with few cache misses (@exm-blocked-transpose). Read `A` only through `get_a(A, n, i, j)` and write `B` only through `set_b(B, n, i, j, v)` (which stores `B[i][j] = v`): these helpers also run every access through a simulated direct-mapped cache of $1$ KiB with $32$-byte blocks, in which `A` starts at address $0$ and `B` at address $4096$. The tests require at most $400$ misses for $n=32$ (a row-by-row loop has $1180$) and a correct result for every $n$, including sizes that are not multiples of your block size.

```{.c .starter}
static long cache_tag[32], misses;           /* simulated cache: tag per set, -1 = empty */

static void touch(long addr) {
    long blk = addr >> 5, set = blk & 31, tag = blk >> 5;
    if (cache_tag[set] != tag) { misses++; cache_tag[set] = tag; }
}
static int get_a(const int *A, int n, int i, int j) { touch(4L * (i * n + j)); return A[i * n + j]; }
static void set_b(int *B, int n, int i, int j, int v) { touch(4096 + 4L * (i * n + j)); B[i * n + j] = v; }

void transpose(int n, const int *A, int *B) {
}
```

```{.c .tests}
static void reset(void) { for (int s = 0; s < 32; s++) cache_tag[s] = -1; misses = 0; }

static void check(int n) {
    int *A = malloc(sizeof(int) * n * n), *B = calloc((size_t) n * n, sizeof(int));
    for (int k = 0; k < n * n; k++) A[k] = k * 7 + 1;
    reset();
    transpose(n, A, B);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            assert(B[j * n + i] == A[i * n + j]);
    free(A); free(B);
}

void test_correct_32(void) { check(32); }
void test_correct_odd_sizes(void) { check(1); check(5); check(13); check(61); }

void test_few_misses_32(void) {
    check(32);
    assert(misses <= 400);
}
```
:::
