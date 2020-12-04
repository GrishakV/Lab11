#!/usr/bin/env python3
# -*- config: utf-8 -*-


def r_factorial(n):
    if n == 0:
        return 1
    else:
        return n * r_factorial(n - 1)


def r_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return r_fib(n - 2) + r_fib(n - 1)


def i_factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


def i_fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


if __name__ == '__main__':

    import timeit

    rec_fib = r_fib(10)
    rec_factorial = r_factorial(10)
    iterative_fib = i_fib(10)
    iterative_factorial = i_factorial(10)

    print(
        f'Результат работы рекурсивной функции чисел Фибоначчи(10) = {rec_fib}. '
        f'Время выполнения: {timeit.timeit("rec_fib", setup="from __main__ import rec_fib")} \n',
        f'Результат работы итеративной функции чисел Фибоначчи(10) = {iterative_fib}. '
        f'Время выполнения: {timeit.timeit("iterative_fib", setup="from __main__ import iterative_fib")} \n',
        f'Результат работы рекурсивной функции факториала(10) = {rec_factorial}. '
        f'Время выполнения: {timeit.timeit("rec_factorial", setup="from __main__ import rec_factorial")} \n',
        f'Результат работы итеративной функции факториала(10) = {iterative_factorial}. '
        f'Время выполнения: '
        f'{timeit.timeit("iterative_factorial", setup="from __main__ import iterative_factorial")} \n',
        )

