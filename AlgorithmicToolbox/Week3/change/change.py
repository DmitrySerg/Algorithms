# Uses python3
import sys

def get_change(m):
    n_tens = m//10
    m -= n_tens*10

    n_fives = m//5
    m -= n_fives*5

    n_ones = m
    m = n_tens + n_fives + n_ones
    
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
