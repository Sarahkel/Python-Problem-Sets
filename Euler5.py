# Sarah Scholz 22/02/2018
# Euler Problem 5 "Smallest multiple" - https://projecteuler.net/problem=5
# Previous attempts took too long until I found this tip to increment by 2520 every time:
# https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution

# Smallest common multiple of the numbers 1 - 10 is 2520
# The smallest common multiple of the numbers 1-20 has to be dividable by 2520. 
# Therefore, there is no need for the program to scan every number but only the multiples of 2520.



i = 2520
n = 1 # variable to keep the while loop running 

while n != 2: # impossible criteria to ensure the loop runs until an answer is found
    if (i%11 + i%12 + i%13 + i%14 +i%15 + i%16 + i%17 + i%18 + i%19 + i%20 == 0):
        print (i)
        break
    else:
        i = i + 2520

# The Exercise requested the use of for and range
# However I could not come up with a solution that was as sleek and intuitive as the above.
