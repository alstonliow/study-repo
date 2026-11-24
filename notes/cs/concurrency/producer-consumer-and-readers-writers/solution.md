::: {.solution for="prob-bounded-buffer-code" status="draft"}
```{.c}
#include <pthread.h>

typedef struct {
    int *buf;
    int n;
    int front;
    int rear;
    pthread_mutex_t mutex;
    pthread_cond_t notfull;
    pthread_cond_t notempty;
} sbuf_t;

void sbuf_init(sbuf_t *sp, int n) {
    sp->buf = calloc((size_t)n, sizeof(int));
    sp->n = n;
    sp->front = sp->rear = 0;               /* empty: front == rear */
    pthread_mutex_init(&sp->mutex, NULL);
    pthread_cond_init(&sp->notfull, NULL);
    pthread_cond_init(&sp->notempty, NULL);
}

void sbuf_deinit(sbuf_t *sp) {
    free(sp->buf);
    pthread_mutex_destroy(&sp->mutex);
    pthread_cond_destroy(&sp->notfull);
    pthread_cond_destroy(&sp->notempty);
}

void sbuf_insert(sbuf_t *sp, int item) {
    pthread_mutex_lock(&sp->mutex);
    while (sp->rear - sp->front == sp->n)   /* full: wait for a free slot */
        pthread_cond_wait(&sp->notfull, &sp->mutex);
    sp->buf[sp->rear % sp->n] = item;
    sp->rear++;
    pthread_cond_signal(&sp->notempty);     /* one more item */
    pthread_mutex_unlock(&sp->mutex);
}

int sbuf_remove(sbuf_t *sp) {
    pthread_mutex_lock(&sp->mutex);
    while (sp->rear == sp->front)           /* empty: wait for an item */
        pthread_cond_wait(&sp->notempty, &sp->mutex);
    int item = sp->buf[sp->front % sp->n];
    sp->front++;
    pthread_cond_signal(&sp->notfull);      /* one more free slot */
    pthread_mutex_unlock(&sp->mutex);
    return item;
}
```

The mutex plays the role of the semaphore `mutex` of @def-sbuf, and the two conditions "not full" and "not empty" replace the counting semaphores `slots` and `items`: instead of counting, a thread re-checks the state under the mutex in a `while` loop, because another thread may have taken the slot or item between the signal and the wake-up. The counters `front` and `rear` only grow, so `rear - front` is the number of items; an `int` lasts for about two billion insertions, enough here (a long-running server would reduce both by multiples of `n`).
:::

::: {.solution for="prob-web-cache-code" status="draft"}
```{.c}
#include <pthread.h>

#define MAX_CACHE_SIZE 1000
#define MAX_OBJECT_SIZE 300

typedef struct entry {
    char *key;
    char *data;
    int size;
    unsigned long last_used;
    struct entry *next;
} entry_t;

typedef struct {
    entry_t *head;
    int total;
    unsigned long clock;
    pthread_rwlock_t lock;
    pthread_mutex_t clock_lock;
} cache_t;

void cache_init(cache_t *c) {
    c->head = NULL;
    c->total = 0;
    c->clock = 0;
    pthread_rwlock_init(&c->lock, NULL);
    pthread_mutex_init(&c->clock_lock, NULL);
}

static void free_entry(entry_t *e) {
    free(e->key);
    free(e->data);
    free(e);
}

void cache_free(cache_t *c) {
    entry_t *e = c->head;
    while (e != NULL) {
        entry_t *next = e->next;
        free_entry(e);
        e = next;
    }
    c->head = NULL;
    c->total = 0;
    pthread_rwlock_destroy(&c->lock);
    pthread_mutex_destroy(&c->clock_lock);
}

/* Mark e as just used. Called with the lock held in either mode. */
static void touch(cache_t *c, entry_t *e) {
    pthread_mutex_lock(&c->clock_lock);
    e->last_used = ++c->clock;
    pthread_mutex_unlock(&c->clock_lock);
}

/* Unlink and free *link. Requires the write lock. */
static void remove_at(cache_t *c, entry_t **link) {
    entry_t *e = *link;
    *link = e->next;
    c->total -= e->size;
    free_entry(e);
}

int cache_lookup(cache_t *c, const char *key, char *out) {
    int size = -1;
    pthread_rwlock_rdlock(&c->lock);           /* many lookups at once */
    for (entry_t *e = c->head; e != NULL; e = e->next)
        if (strcmp(e->key, key) == 0) {
            memcpy(out, e->data, (size_t)e->size);
            size = e->size;
            touch(c, e);
            break;
        }
    pthread_rwlock_unlock(&c->lock);
    return size;
}

void cache_insert(cache_t *c, const char *key, const char *data, int size) {
    if (size < 0 || size > MAX_OBJECT_SIZE)
        return;
    entry_t *e = malloc(sizeof *e);
    e->key = malloc(strlen(key) + 1);
    strcpy(e->key, key);
    e->data = malloc(size > 0 ? (size_t)size : 1);
    memcpy(e->data, data, (size_t)size);
    e->size = size;

    pthread_rwlock_wrlock(&c->lock);           /* exclusive */
    for (entry_t **link = &c->head; *link != NULL; link = &(*link)->next)
        if (strcmp((*link)->key, key) == 0) {  /* replace an old copy */
            remove_at(c, link);
            break;
        }
    while (c->total + size > MAX_CACHE_SIZE) { /* evict least recently used */
        entry_t **victim = &c->head;
        for (entry_t **link = &c->head; *link != NULL; link = &(*link)->next)
            if ((*link)->last_used < (*victim)->last_used)
                victim = link;
        remove_at(c, victim);
    }
    touch(c, e);
    e->next = c->head;
    c->head = e;
    c->total += size;
    pthread_rwlock_unlock(&c->lock);
}
```

Lookups hold the readers-writers lock in read mode, so any number of them run at once; the list itself is changed only under the write lock. The recency stamp is the one thing a reader writes, so it has its own small mutex: two readers stamping the same entry, or reading the clock, never race. Under the write lock no reader runs, so the eviction scan reads `last_used` safely. The new object is copied before the write lock is taken, which keeps the exclusive section short. The loop `while (total + size > MAX_CACHE_SIZE)` terminates because the list is non-empty whenever `total > 0`, and `size` alone never exceeds the limit.
:::
