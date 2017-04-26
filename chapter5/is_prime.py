# Author: Jorge Rodriguez
# Date: February 21, 2017

# create function is_prime(n) which takes a parameter to find prime numbers

def is_prime(n):
    # if statement to check for n equality with 1
    if n == 1:
        print('1 is special')
        return False
    # for loop
    for x in range(2, n):
        if n % 2 == 0:
            print("{} equals {} x {}".format(n, x, n // x))
            return False
    else:
        print(n, "is a prime number")
        return True

number1 = int(input('Enter a number to start your range: '))
number2 = int(input('Enter a number to end your range(should be higher than your first number): '))

for n in range(number1, number2):
    is_prime(n)
