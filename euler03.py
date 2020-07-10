'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''


def largestPrime(x):

    for i in range(2,x+1): # 1 is not prime number so it has to start from 2 and to include X. range end at x+1
        # Find divisor of x
        if x % i == 0:
            print(i) # check divisor
            x = int(x/i) # change x because if we do not change it. We will get elements of multiplier.
        else:
            pass

x = int(input())
largestPrime(x)
