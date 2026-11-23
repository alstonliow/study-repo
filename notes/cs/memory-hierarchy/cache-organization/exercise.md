::: {#prob-cache-simulator-code .problem .coding origin="adapted" source="res-cmu-15213-labs-cache-lab" tags="caches,simulation"}
Write a cache simulator (@def-cache-parameters, @def-cache-lookup). `simulate(s, E, b, addrs, n, &hits, &misses, &evictions)` runs the $n$ byte addresses `addrs[0..n-1]` through an initially empty cache with $2^s$ sets, $E$ lines per set and $2^b$-byte blocks, using LRU replacement, and stores the number of hits, misses and evictions. Addresses are 64-bit; each access touches one byte, so it involves exactly one block. Support $s+b\le 20$ and $E\le 16$; allocate what you need with `malloc` and free it before returning.

```{.c .starter}
void simulate(int s, int E, int b, const unsigned long *addrs, int n,
              int *hits, int *misses, int *evictions) {
    *hits = *misses = *evictions = 0;
}
```

```{.c .tests}
static void run(int s, int E, int b, const unsigned long *a, int n, int h, int m, int e) {
    int hits = -1, misses = -1, evictions = -1;
    simulate(s, E, b, a, n, &hits, &misses, &evictions);
    assert(hits == h && misses == m && evictions == e);
}

void test_direct_mapped_example(void) {
    unsigned long a[] = {0, 4, 1, 16, 0, 36, 20, 4};
    run(2, 1, 2, a, 8, 1, 7, 5);
}

void test_two_way_example(void) {
    unsigned long a[] = {0, 4, 1, 16, 0, 36, 20, 4};
    run(1, 2, 2, a, 8, 2, 6, 2);
}

void test_lru_not_fifo(void) {
    /* one set, two lines: 0 is reused, so 2 must evict block 1, and 0 hits again */
    unsigned long a[] = {0x00, 0x10, 0x00, 0x20, 0x00};
    run(0, 2, 4, a, 5, 2, 3, 1);
}

void test_fully_associative_capacity(void) {
    /* 4 lines, cycling through 5 blocks: every access misses under LRU */
    unsigned long a[10];
    for (int i = 0; i < 10; i++) a[i] = (unsigned long) (i % 5) * 64;
    run(0, 4, 6, a, 10, 0, 10, 6);
}

void test_large_addresses(void) {
    unsigned long a[] = {0x7fff00001000ul, 0x7fff00001008ul, 0x00001000ul, 0x7fff00001010ul};
    run(4, 1, 4, a, 4, 1, 3, 1);
}
```
:::
