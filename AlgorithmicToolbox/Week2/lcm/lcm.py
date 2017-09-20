# Uses python3
import sys

def Euclid_gcd(a, b):
    if b == 0:
        return a
    else:
        a = a%b
    return Euclid_gcd(b, a)


def lcm(a, b):
    gcd = Euclid_gcd(a, b)
    lcm = a * b // gcd
    return lcm

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

