# Uses python3
import sys

def get_fibonacci_modulo_m(n, m):
    if n <= 1:
        return n
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current%m, previous%m + current
    return current % m

def get_pisano_period(m):
    a = 0
    b = 1
    c = a + b
    for i in range(0, m*m):
        c = (a + b) % m
        a = b
        b = c
        if (a == 0) & (b == 1):
            return i + 1

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n
    else:   
        smaller_fibonacci_n = n%get_pisano_period(m)
        return get_fibonacci_modulo_m(smaller_fibonacci_n, m)

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
