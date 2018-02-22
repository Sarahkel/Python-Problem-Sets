# Sarah Scholz 22/02/2018
# Euler Problem 5 "Smallest multiple" - https://projecteuler.net/problem=5
# Previous attempts took too long until I found this tip to increment by 2520 every time:
# https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution

i = 2520
n = 1

while n != 2:
    if (i%11 + i%12 + i%13 + i%14 +i%15 + i%16 + i%17 + i%18 + i%19 + i%20 == 0):
        print (i)
        break
    else:
        i = i + 2520
