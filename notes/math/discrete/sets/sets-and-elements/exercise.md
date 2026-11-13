<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-sets-02 origin="external" source="fit1058-cn-1.16-q2"}
In C, `int monthNumber;` declares a variable of type `int`,
and `char monthName[10];` declares a string of at most 9 characters.
Let `Int` be the set of possible values for a variable of type
`int`, and `String` the set of possible values for a string of
at most 9 letters.

(a) The statement

        struct aNewType {
            int year;
            char monthName[10];
        } monthBothWays;

    creates a type for objects consisting of any int followed by any string.
    Using `Int`, `String` and a standard set operation, what
    set is represented by `aNewType`?

(b) The statement

        union anotherNewType {
            int year;
            char monthName[10];
        } monthEitherWay;

    creates a type for objects that can be either an int or a string (only
    one at a time). What set is represented by `anotherNewType`?
:::
