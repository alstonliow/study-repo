::: {#prob-implicit-allocator-code .problem .coding origin="adapted" source="res-cmu-15213-labs-malloc-lab" level="hard" tags="malloc,free-lists,coalescing"}
Write a small allocator with an implicit free list, boundary tags, first fit, splitting and immediate coalescing (@def-implicit-free-list, @thm-constant-time-coalescing), managing the fixed array `heap` of $2^{16}$ bytes instead of memory from `sbrk`.

- `mm_init()` sets up an empty heap; the tests call it first.
- `mm_malloc(n)` returns a pointer to at least $n\ge1$ bytes, aligned to $16$ bytes, inside `heap`, not overlapping any other allocated payload; it returns `NULL` if no free block is large enough (and for $n=0$).
- `mm_free(p)` frees a block returned by `mm_malloc`; `mm_free(NULL)` does nothing.

Freed memory must be reusable: after everything is freed, one request for almost the whole heap must succeed again.

```{.c .starter}
static _Alignas(16) unsigned char heap[1 << 16];

void mm_init(void) {
}

void *mm_malloc(size_t n) {
    return NULL;
}

void mm_free(void *p) {
}
```

```{.c .tests}
static int inside(void *p, size_t n) {
    return (unsigned char *) p >= heap && (unsigned char *) p + n <= heap + sizeof heap;
}

void test_alignment_and_bounds(void) {
    mm_init();
    for (size_t n = 1; n < 200; n += 7) {
        void *p = mm_malloc(n);
        assert(p && inside(p, n) && ((uintptr_t) p % 16) == 0);
    }
}

void test_no_overlap(void) {
    unsigned char *ps[50]; mm_init();
    for (int i = 0; i < 50; i++) { ps[i] = mm_malloc(10 + 13 * i); assert(ps[i]); memset(ps[i], i, 10 + 13 * i); }
    for (int i = 0; i < 50; i++)
        for (int k = 0; k < 10 + 13 * i; k++) assert(ps[i][k] == i);
}

void test_reuse_after_free(void) {
    mm_init();
    void *a = mm_malloc(1000), *b = mm_malloc(1000), *c = mm_malloc(1000);
    assert(a && b && c);
    mm_free(b);
    void *d = mm_malloc(900);
    assert(d == b);                                  /* first fit reuses b's block */
    mm_free(a); mm_free(d); mm_free(c);
    void *big = mm_malloc(60000);                    /* needs all blocks coalesced */
    assert(big && inside(big, 60000));
}

void test_exhaustion(void) {
    mm_init();
    assert(mm_malloc(0) == NULL);
    assert(mm_malloc(1 << 17) == NULL);
    int count = 0;
    while (mm_malloc(1000)) count++;
    assert(count >= 60 && count <= 65);
    mm_free(NULL);
}
```
:::
