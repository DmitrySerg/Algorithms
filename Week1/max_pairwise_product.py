# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)


result = 0
max_1 = -1
index_1 = None
max_2 = -1
index_2 = None
# find first max value and its index
for element in range(len(a)):
    if a[element] >= max_1:
        max_1 = a[element]
        index_1 = element
for element in range(len(a)):
    if a[element] >= max_2:
        if element != index_1:
            max_2 = a[element]
            index_2 = element
            
result = max_1 * max_2

print(result)
