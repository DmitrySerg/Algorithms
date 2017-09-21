#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    while len(a)!=0:
        maxDigit = 0
        for digit in a:
            first_pair = digit + str(maxDigit) 
            second_pair = str(maxDigit) + digit
            if int(first_pair) > int(second_pair):
                maxDigit = int(digit)            
        res += str(maxDigit)
        a.remove(str(maxDigit))
    return int(res)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
