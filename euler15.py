'''
find the number of routes

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,

there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

The formula of shortest way is (width + height)! / ((width)! * (height)!)
So in this case, 40! / (20! * 20!)
'''

def facotrial(num):
    fac_num = 1
    if num == 0:
        return 1
    elif num <= 0:
        return False
    else:
        for i in range(1, num+1):
            fac_num = fac_num * i
    return fac_num

print(facotrial(0))
print(facotrial(-1))
print(facotrial(40) / (facotrial(20) * facotrial(20)))