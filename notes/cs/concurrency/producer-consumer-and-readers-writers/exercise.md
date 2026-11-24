::: {#prob-bounded-buffer-code .problem .coding origin="adapted" source="res-cmu-15213-labs-proxy-lab" tags="threads,producer-consumer,pthreads"}
A prethreaded proxy (@def-prethreaded-server) passes connected descriptors from its main thread to worker threads through a bounded buffer. Implement the buffer with one Pthreads mutex and two condition variables (@sec-cs-concurrency-producer-consumer-and-readers-writers describes them; POSIX semaphores are not available on every system):

- `sbuf_init(sp, n)` sets up an empty buffer of capacity $n\ge1$, allocating the array on the heap;
- `sbuf_insert(sp, item)` waits while the buffer is full, then appends `item`;
- `sbuf_remove(sp)` waits while the buffer is empty, then removes and returns the oldest item;
- `sbuf_deinit(sp)` frees the array.

Items must come out in the order they went in, and any number of threads may call `sbuf_insert` and `sbuf_remove` concurrently.

```{.c .starter}
#include <pthread.h>

typedef struct {
    int *buf;                   /* the items */
    int n;                      /* capacity */
    int front;                  /* buf[front % n] is the oldest item */
    int rear;                   /* buf[rear % n] is the next free slot */
    pthread_mutex_t mutex;
    pthread_cond_t notfull;
    pthread_cond_t notempty;
} sbuf_t;

void sbuf_init(sbuf_t *sp, int n) {
}

void sbuf_deinit(sbuf_t *sp) {
}

void sbuf_insert(sbuf_t *sp, int item) {
}

int sbuf_remove(sbuf_t *sp) {
    return 0;
}
```

```{.c .tests}
#include <time.h>

#define PER_PRODUCER 20000

static sbuf_t shared;
static long consumed_sum[4];

static void *producer(void *arg) {
    long id = (long)arg;
    for (int i = 1; i <= PER_PRODUCER; i++)
        sbuf_insert(&shared, (int)(id * 100000 + i));
    return NULL;
}

static void *consumer(void *arg) {
    long id = (long)arg;
    long sum = 0;
    for (int i = 0; i < PER_PRODUCER; i++)
        sum += sbuf_remove(&shared);
    consumed_sum[id] = sum;
    return NULL;
}

void test_fifo_single_thread(void) {
    sbuf_t b;
    sbuf_init(&b, 3);
    sbuf_insert(&b, 7);
    sbuf_insert(&b, 8);
    assert(sbuf_remove(&b) == 7);
    sbuf_insert(&b, 9);
    sbuf_insert(&b, 10);              /* wraps around the array */
    assert(sbuf_remove(&b) == 8);
    assert(sbuf_remove(&b) == 9);
    assert(sbuf_remove(&b) == 10);
    sbuf_deinit(&b);
}

static sbuf_t tiny;
static void *slow_consumer(void *arg) {
    struct timespec pause = {0, 20000000};   /* 20 ms */
    nanosleep(&pause, NULL);
    for (int i = 0; i < 5; i++)
        assert(sbuf_remove(&tiny) == i);
    return NULL;
}

void test_producer_blocks_when_full(void) {
    pthread_t t;
    sbuf_init(&tiny, 1);
    pthread_create(&t, NULL, slow_consumer, NULL);
    for (int i = 0; i < 5; i++)
        sbuf_insert(&tiny, i);            /* must wait for the consumer */
    pthread_join(t, NULL);
    sbuf_deinit(&tiny);
}

void test_many_threads(void) {
    pthread_t p[4], c[4];
    sbuf_init(&shared, 8);
    for (long i = 0; i < 4; i++) {
        pthread_create(&c[i], NULL, consumer, (void *)i);
        pthread_create(&p[i], NULL, producer, (void *)i);
    }
    for (int i = 0; i < 4; i++) {
        pthread_join(p[i], NULL);
        pthread_join(c[i], NULL);
    }
    long total = 0, want = 0;
    for (long id = 0; id < 4; id++) {
        total += consumed_sum[id];
        for (int i = 1; i <= PER_PRODUCER; i++)
            want += id * 100000 + i;
    }
    assert(total == want);                /* every item removed exactly once */
    sbuf_deinit(&shared);
}
```
:::

::: {#prob-web-cache-code .problem .coding origin="adapted" source="res-cmu-15213-labs-proxy-lab" tags="threads,readers-writers,caching,pthreads"}
A concurrent proxy keeps recently fetched Web objects in a cache shared by all its threads. Implement such a cache, protected by a Pthreads readers-writers lock (@exm-readers-first) so that several threads can look up objects at the same time, with the following rules (scaled-down versions of the lab's limits):

- `cache_init(c)` sets up an empty cache; `cache_free(c)` frees everything;
- `cache_insert(c, key, data, size)` copies an object of `size` bytes under the string `key`. Objects larger than `MAX_OBJECT_SIZE` are not cached; inserting an existing key replaces its object. While the total size of the cached objects would exceed `MAX_CACHE_SIZE`, the least recently used object is evicted first;
- `cache_lookup(c, key, out)` copies the object into `out` and returns its size if `key` is cached, otherwise returns $-1$. A lookup counts as a use, as does an insertion.

Only object bytes count toward `MAX_CACHE_SIZE`, not keys or bookkeeping, and `total` must always equal the sum of the cached sizes; the entries form the linked list `head`. Lookups must take the lock in read mode, so a lookup that updates the recency information has to do so without a write lock (for example under a separate small mutex).

```{.c .starter}
#include <pthread.h>

#define MAX_CACHE_SIZE 1000
#define MAX_OBJECT_SIZE 300

typedef struct entry {
    char *key;
    char *data;
    int size;
    unsigned long last_used;          /* larger = used more recently */
    struct entry *next;
} entry_t;

typedef struct {
    entry_t *head;
    int total;                        /* bytes of object data cached */
    unsigned long clock;              /* source of last_used values */
    pthread_rwlock_t lock;            /* readers: lookups; writer: insert */
    pthread_mutex_t clock_lock;       /* protects clock and last_used */
} cache_t;

void cache_init(cache_t *c) {
}

void cache_free(cache_t *c) {
}

int cache_lookup(cache_t *c, const char *key, char *out) {
    return -1;
}

void cache_insert(cache_t *c, const char *key, const char *data, int size) {
}
```

```{.c .tests}
static char obj[MAX_OBJECT_SIZE + 1];

static void fill(char ch, int n) { memset(obj, ch, (size_t)n); }

void test_insert_lookup(void) {
    cache_t c;
    char out[MAX_OBJECT_SIZE];
    cache_init(&c);
    assert(cache_lookup(&c, "http://a/", out) == -1);
    fill('a', 100);
    cache_insert(&c, "http://a/", obj, 100);
    assert(cache_lookup(&c, "http://a/", out) == 100);
    assert(out[0] == 'a' && out[99] == 'a');
    assert(c.total == 100);
    fill('b', 50);
    cache_insert(&c, "http://a/", obj, 50);          /* replace */
    assert(cache_lookup(&c, "http://a/", out) == 50 && out[0] == 'b');
    assert(c.total == 50);
    fill('x', MAX_OBJECT_SIZE + 1);
    cache_insert(&c, "http://big/", obj, MAX_OBJECT_SIZE + 1);
    assert(cache_lookup(&c, "http://big/", out) == -1);  /* too large */
    cache_free(&c);
}

void test_lru_eviction(void) {
    cache_t c;
    char out[MAX_OBJECT_SIZE];
    cache_init(&c);
    const char *keys[] = {"k0", "k1", "k2", "k3"};
    for (int i = 0; i < 4; i++) {                    /* 4 x 250 = 1000 bytes: all fit */
        fill((char)('0' + i), 250);
        cache_insert(&c, keys[i], obj, 250);
    }
    assert(c.total == 1000);
    assert(cache_lookup(&c, "k0", out) == 250);      /* k0 now most recent; k1 least */
    fill('5', 200);
    cache_insert(&c, "k5", obj, 200);                /* evicts k1 only */
    assert(cache_lookup(&c, "k1", out) == -1);
    assert(cache_lookup(&c, "k0", out) == 250);
    assert(cache_lookup(&c, "k2", out) == 250);
    assert(cache_lookup(&c, "k3", out) == 250);
    assert(cache_lookup(&c, "k5", out) == 200 && out[0] == '5');
    assert(c.total == 950);
    fill('6', 300);
    cache_insert(&c, "k6", obj, 300);                /* evicts k0 (least recent now) */
    assert(cache_lookup(&c, "k0", out) == -1);
    assert(c.total <= MAX_CACHE_SIZE);
    cache_free(&c);
}

static cache_t shared_cache;

static void *worker(void *arg) {
    long id = (long)arg;
    char key[32], data[MAX_OBJECT_SIZE], out[MAX_OBJECT_SIZE];
    for (int i = 0; i < 2000; i++) {
        int k = (int)((id * 7 + i) % 12);
        snprintf(key, sizeof key, "http://h/%d", k);
        int size = 40 + k * 10;
        int got = cache_lookup(&shared_cache, key, out);
        if (got >= 0) {
            assert(got == size);                     /* never a torn or wrong object */
            for (int j = 0; j < size; j++)
                assert(out[j] == (char)('A' + k));
        } else {
            memset(data, 'A' + k, (size_t)size);
            cache_insert(&shared_cache, key, data, size);
        }
    }
    return NULL;
}

void test_concurrent(void) {
    pthread_t t[6];
    cache_init(&shared_cache);
    for (long i = 0; i < 6; i++)
        pthread_create(&t[i], NULL, worker, (void *)i);
    for (int i = 0; i < 6; i++)
        pthread_join(t[i], NULL);
    assert(shared_cache.total <= MAX_CACHE_SIZE);
    int sum = 0;
    for (entry_t *e = shared_cache.head; e != NULL; e = e->next)
        sum += e->size;
    assert(sum == shared_cache.total);
    cache_free(&shared_cache);
}
```
:::
