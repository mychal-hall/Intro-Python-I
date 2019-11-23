# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(n):
    if n % 2 == 0:
        print("True")
    elif n % 2 is not 0:
        print("False")

is_even(3)
is_even(4)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def even_check(num):
    if num % 2 == 0:
        print("Even!")
    elif num % 2 is not 0:
        print("Odd!")

even_check(num)