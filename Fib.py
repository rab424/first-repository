#Robert's Fibonacci Program
"""
This is a simple program that asks the user how many numbers in the fibonacci sequence they would like to see.
"""

def fib():
    a, b, i = 0, 1, 0
    n = int(input("Please enter how many numbers you would like the fibonacci sequence to go to.\n"))
    print("The first %d numbers in the fibonacci sequence are:" % (n))
    while i < n:
        print(a, end=" ")
        a, b = b, a+b
        i += 1
    print()


fib()
