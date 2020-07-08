'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.

The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

def findSum(arg1):
    a = arg1
    arr3 = []
    for i in range(1,x+1):
        if 3 * i > x:
            break
        else:
            arr3.append(3 * i)
    print(list(arr3))
    arr5 = []
    for i in range(1,x+1):
        if 5 * i >= x:
            break
        else:
            arr5.append(5 * i)
    print(list(arr5))
    arr = arr3 + arr5
    noDup = []
    for i in arr:
        if i not in noDup:
            noDup.append(i)
    print(list(noDup))

    SSum = sum(noDup)
    print(SSum)

x = int(input())
findSum(x)
