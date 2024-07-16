# Collatz-Problem - Ansatz von Fin
import sys


def collatz(n):
    original_n = n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    return original_n, True


if __name__ == '__main__':
    for i in range(1, sys.maxsize):
        print(collatz(i))
