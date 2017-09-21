# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    prices = [value/weight for value, weight in zip(values, weights)]

    weights = [w for _,w in sorted(zip(prices,weights), reverse=True)]
    values = [v for _,v in sorted(zip(prices,values), reverse=True)]
    prices = sorted(prices, reverse=True)
    
    for i in range(n):
        if capacity == 0:
            return value
        a = min(weights[i], capacity)
        value += a * prices[i]
        capacity -= a    
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
