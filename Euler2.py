# Sarah Scholz 20/02/2018
# Euler Problem 2: "Even Fibonacci numbers" - https://projecteuler.net/problem=2
# Adapted from Ian McLoughlin - https://github.com/ianmcloughlin/python-fib/blob/master/fib.py

sum = 0
i = 0
j = 1

while i < 4000000:
    if i % 2 ==0:
        sum = sum + i
    i, j = j, i + j

print("the sum of all even fibonacci numbers below 4000000 is",sum)
