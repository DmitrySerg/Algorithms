# Uses python3
import sys

def Euclid_gcd(a, b):
    if b == 0:
        return a
    else:
        a = a%b
    return Euclid_gcd(b, a)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(Euclid_gcd(a, b))
