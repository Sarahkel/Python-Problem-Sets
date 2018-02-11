# Sarah Scholz 10/02/2018
# Collatz Conjecture

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


