::: {#prob-byte-swap-code .problem .coding origin="adapted" source="res-cmu-15213-labs-data-lab" tags="bit-manipulation,bytes"}
Bytes of an `int` are numbered $0$ (least significant) to $3$ (most significant). Write `get_byte(x, n)`, which returns byte $n$ of $x$ as a value in $0,\dots,255$, and `byte_swap(x, n, m)`, which returns $x$ with bytes $n$ and $m$ exchanged. Use only `! ~ & ^ | + << >>` and no control flow. For example `byte_swap(0x12345678, 1, 3)` is `0x56341278`; swapping all bytes this way converts between little-endian and big-endian order (@def-endianness).

```{.c .starter}
int get_byte(int x, int n) {
    return 0;
}

int byte_swap(int x, int n, int m) {
    return 0;
}
```

```{.c .tests}
void test_get_byte(void) {
    assert(get_byte(0x12345678, 0) == 0x78);
    assert(get_byte(0x12345678, 3) == 0x12);
    assert(get_byte((int) 0x80FF0000u, 3) == 0x80);
    assert(get_byte((int) 0x80FF0000u, 2) == 0xFF);
}

void test_byte_swap(void) {
    assert(byte_swap(0x12345678, 1, 3) == 0x56341278);
    assert(byte_swap((int) 0xDEADBEEFu, 0, 2) == (int) 0xDEEFBEADu);
    assert(byte_swap(0x12345678, 2, 2) == 0x12345678);
}

void test_reverse_bytes(void) {
    int x = byte_swap(byte_swap(0x11223344, 0, 3), 1, 2);
    assert(x == 0x44332211);
}
```
:::
