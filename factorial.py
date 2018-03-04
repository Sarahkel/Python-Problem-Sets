# Sarah Scholz 04/03/2018
# Function to find factorial of a given number

def factorial(x):
    f = 1
    for i in range (1, x + 1):
        f = i * f
    return f

print("The factorial of 5 is", factorial(5))
print("The factorial of 7 is", factorial(7))
print("The factorial of 10 is", factorial(10))