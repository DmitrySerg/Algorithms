# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        numbers = [0, 1]
        for i in range(n-1):
            numbers.append(numbers[-1]+numbers[-2])
    	return numbers[-1]

n = int(input())
print(calc_fib(n))


def calc_fib(n):
    if (n <= 1):
        return n
    else:
        a, b = 0, 1
        for i in range(n-1):
            b, a = b + a, b
        return b

n = int(input())
print(calc_fib(n))