::: {.solution for="prob-implicit-allocator-code" status="draft"}
```{.c}
static _Alignas(16) unsigned char heap[1 << 16];

#define WSIZE 8                                   /* header/footer word */
#define GET(p) (*(size_t *) (p))
#define PUT(p, v) (*(size_t *) (p) = (v))
#define SIZE(p) (GET(p) & ~(size_t) 0xF)
#define ALLOC(p) (GET(p) & 1)
#define HDR(bp) ((unsigned char *) (bp) - WSIZE)
#define FTR(bp) ((unsigned char *) (bp) + SIZE(HDR(bp)) - 2 * WSIZE)
#define NEXT(bp) ((unsigned char *) (bp) + SIZE(HDR(bp)))
#define PREV(bp) ((unsigned char *) (bp) - SIZE((unsigned char *) (bp) - 2 * WSIZE))

static void mark(unsigned char *bp, size_t size, size_t alloc) {
    PUT(HDR(bp), size | alloc);
    PUT(FTR(bp), size | alloc);
}

void mm_init(void) {
    size_t n = sizeof heap;
    PUT(heap + 8, 16 | 1); PUT(heap + 16, 16 | 1);      /* prologue: header, footer */
    mark(heap + 32, n - 32, 0);                         /* one free block */
    PUT(heap + n - WSIZE, 0 | 1);                       /* epilogue header */
}

static unsigned char *coalesce(unsigned char *bp) {
    size_t size = SIZE(HDR(bp));
    if (!ALLOC(HDR(NEXT(bp)))) size += SIZE(HDR(NEXT(bp)));
    if (!ALLOC(HDR(PREV(bp)))) { bp = PREV(bp); size += SIZE(HDR(bp)); }
    mark(bp, size, 0);
    return bp;
}

void *mm_malloc(size_t n) {
    if (n == 0 || n > sizeof heap) return NULL;
    size_t need = (n + 2 * WSIZE + 15) & ~(size_t) 15;     /* header + footer, 16-aligned */
    for (unsigned char *bp = heap + 32; SIZE(HDR(bp)) > 0; bp = NEXT(bp)) {
        size_t size = SIZE(HDR(bp));
        if (ALLOC(HDR(bp)) || size < need) continue;
        if (size - need >= 32) {                            /* split */
            mark(bp, need, 1);
            mark(NEXT(bp), size - need, 0);
        } else {
            mark(bp, size, 1);
        }
        return bp;
    }
    return NULL;
}

void mm_free(void *p) {
    if (!p) return;
    mark(p, SIZE(HDR(p)), 0);
    coalesce(p);
}
```

1. **Layout.** Words are 8 bytes and payloads must be 16-aligned, so every block size is a multiple of 16 and its header sits 8 bytes before a 16-aligned payload. The heap starts with a padding word, then a *prologue* block of 16 bytes (header and footer, marked allocated), then the blocks, and ends with an *epilogue* header of size $0$ marked allocated. Prologue and epilogue are permanent allocated neighbours, so coalescing never has to test whether it is at an edge of the heap.
2. **Headers and footers.** `mark` writes the size with the allocated bit in the low bit into both tags; the low four bits of a size are always $0$. `NEXT` adds the block's size; `PREV` reads the previous block's footer, the word just before the header (@def-boundary-tags).
3. **Allocation.** A request of $n$ bytes needs $n+16$ bytes rounded up to a multiple of $16$. First fit walks the implicit list until the epilogue. A block with at least $32$ spare bytes, the minimum block (header, footer and an aligned payload), is split; otherwise the whole block is used (@def-splitting).
4. **Freeing.** The block is marked free and merged with a free next block and then with a free previous block, the four cases of @thm-constant-time-coalescing in two tests. So no two free blocks are ever adjacent, and after every block is freed the heap is again one free block.
:::
