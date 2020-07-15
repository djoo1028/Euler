'''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,

we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''
# default value
i = 1
c = 0

# define a input value is prime number or not
def is_prime(num):
    # 1 is not prime number
    if num <= 1:
        return False
    i = 2
    while i < num:
        # if it is divisible before the num then it is not prime number
        if num % i == 0:
            return False
        i += 1
    return True

# get the n-th prime number
# c is n-th location. I can break the while loop as I set the c value
while True:
    if is_prime(i):
        c += 1
        print('{0} : {1}'.format(c,i))
    if c == 10001:
        break
    i += 1
