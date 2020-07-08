'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.

The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

def findSum(arg1):
    
    a = arg1    # input value will be range for the summation
    arr3 = []   # multiple of 3
    for i in range(1,x+1): # Remove 0 and include the last spot
        if 3 * i > x:      # If the value is greater than range than break for loop
            break
        else:
            arr3.append(3 * i) # add in to the list
    print(list(arr3))
    arr5 = []                 # multiple of 5
    for i in range(1,x+1):
        if 5 * i >= x:
            break
        else:
            arr5.append(5 * i)
    print(list(arr5))
    arr = arr3 + arr5          # Add two list which have multiple of 3 and 5
    noDup = []
    for i in arr:              # Remove duplicate numbers
        if i not in noDup:     # If a number does not exist add and if number is exist move to next index
            noDup.append(i)
    print(list(noDup))         # checke

    SSum = sum(noDup)          # Sum all numbers in list
    print(SSum)     

x = int(input())
findSum(x)
