'''
A palindromic number reads the same both ways.

The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

arr2d = []
count = 0
# We are going to multiply two three digit numbers
# So the range is 100 to 999
for i in range(100, 1000):
    for j in range(100, 1000):
        # The biggest number of multiplication in three digits are
        # 999 * 998 = 997002
        # if it is bigger than that it is not multiplication of three digits
        if i * j > 997002:
            break
        k = i * j
        k = str(k) #Integer can't sliced so we have to convert to string to slice
        if k == k[::-1]: # check palindrome
            arr2d.append(int(k)) # we have to convert to integer to compare integer
            count += 1 # just checking how many times we calculate
            print('{0} * {1} = {2}'.format(i,j,k)) # two figure out multiplication
print(count)
print(max(arr2d)) # find the maximum number in the list.
