# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    m1, m2 = l, l
    
    for i in range(l + 1, r + 1):
        if a[i] == x:
            m2 += 1
            a[i], a[m2] = a[m2], a[i] 
        elif a[i] < x:    
            m1 += 1
            m2 += 1 
            a[i], a[m2] = a[m2], a[i]
            a[m1 - 1], a[m2] = a[m2], a[m1 - 1]
    return m1, m2

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
