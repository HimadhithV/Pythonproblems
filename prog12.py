# Sum of numbers from 1 to n

def recursum(n):
    if n <= 1:
        return n
    else:
        return n+recursum(n-1)


n = 5
res = recursum(n)
print("Sum of digits in numbers from 1 to 5 =", res)
