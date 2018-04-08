# Sarah Scholz 10/02/2018
# Collatz Conjecture
# Exercise: "single Python script that starts with an integer and repeatedly applies the Collatz function (divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement. At each iteration, the current value of the integer should be printed to the screen. "
# More info on the conjecture:https://en.wikipedia.org/wiki/Collatz_conjecture

n = int(input("Please enter a positive integer: "))
print ("The Collatz Conjecture for the number", n, "works as follows:")

while (n != 1):
    if (n % 2 == 0):
        n = n // 2
        print (n)
    else:
        n = n * 3 + 1
        print (n)
print ("Yay, you arrived at", n)
