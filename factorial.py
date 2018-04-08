# Sarah Scholz 04/03/2018
# Function to find factorial of a given number
# Factorial is the product of all positive integers less than or equal to n

def factorial(x):
    f = 1
    for i in range (1, x + 1): # +1 to ensure the function counts inclusive x
        f = i * f # f is multiplied repeatedly by all positive integers less than or equal to n
    return f

print("The factorial of 5 is", factorial(5))
print("The factorial of 7 is", factorial(7))
print("The factorial of 10 is", factorial(10))
