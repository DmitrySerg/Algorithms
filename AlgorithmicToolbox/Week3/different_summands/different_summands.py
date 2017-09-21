# Uses python3
import sys

def optimal_summands(n):
    l = 1
    summands = []
    while n>0:
        if n <= 2*l:
            summands.append(n)
            break
        else:
            summands.append(l)
            n -= l
            l += 1
    return summands



if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
