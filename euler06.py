'''
The sum of the squares of the first ten natural numbers is,

1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2=55^2=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

# This is the function for square of sum
# 1^2 + 2^2 +....+ 10^2
def squareOfSum(num):
    arr = [] # empty list
    sum_arr = 0 # return value
    for i in range(1, num+1): # for loop to fill empty list
        arr.append(i ** 2) # add squared numbers in the list
    sum_arr = sum(arr) # add all elements in the list
    return sum_arr

# this is the function for sum of square
# (1+2+3+...+10)^2
def sumOfSquare(num):
    arr2 = [] # empty list
    sum_arr2 = 0 # return value
    for i in range(1, num+1):
        arr2.append(i) # add elements in the list
        sum_arr2 = sum(arr2) # add all number which are in the list
        sum_arr2 = sum_arr2 ** 2 # squared the result
    return sum_arr2

x = int(input())
# squareOfSum(x)
# sumOfSquare(x)
print(sumOfSquare(x) - squareOfSum(x)) # subtrace square of sum from sum of squared number.