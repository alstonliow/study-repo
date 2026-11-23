::: {.solution for="prob-cache-simulator-code" status="draft"}
```{.c}
typedef struct { int valid; unsigned long tag; long last_used; } line_t;

void simulate(int s, int E, int b, const unsigned long *addrs, int n,
              int *hits, int *misses, int *evictions) {
    long S = 1L << s, clock = 0;
    line_t *cache = calloc((size_t) (S * E), sizeof(line_t));   /* all lines invalid */
    *hits = *misses = *evictions = 0;
    for (int k = 0; k < n; k++) {
        unsigned long set = (addrs[k] >> b) & (unsigned long) (S - 1);
        unsigned long tag = addrs[k] >> (s + b);
        line_t *lines = cache + set * E, *victim = &lines[0];
        int found = 0;
        clock++;
        for (int i = 0; i < E; i++) {
            if (lines[i].valid && lines[i].tag == tag) {          /* hit */
                lines[i].last_used = clock; (*hits)++; found = 1; break;
            }
            if (!lines[i].valid) { if (victim->valid) victim = &lines[i]; }
            else if (victim->valid && lines[i].last_used < victim->last_used) victim = &lines[i];
        }
        if (found) continue;
        (*misses)++;
        if (victim->valid) (*evictions)++;
        victim->valid = 1; victim->tag = tag; victim->last_used = clock;
    }
    free(cache);
}
```

1. Only the valid bit, the tag and a timestamp of the last use are kept per line; the cache is one array of $S\cdot E$ such lines, set $i$ occupying lines $iE,\dots,iE+E-1$.
2. For each address, the set index is bits $b,\dots,b+s-1$ and the tag is everything above them (@def-cache-parameters).
3. Scanning the set either finds a valid line with the right tag (a hit, whose timestamp is refreshed) or chooses where the block goes: an invalid line if any, otherwise the valid line with the oldest timestamp, which is the least recently used one.
4. A miss into a valid line is an eviction. A global counter increased at every access serves as the clock, so timestamps are distinct and LRU is exact.
:::
