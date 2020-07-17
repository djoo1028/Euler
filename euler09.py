'''

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.

'''

# We can think a is less than 500
# if it is greater than 500 then a + b + c = 1000 would not work
for a in range(500):
    # As same reason b is also less than 500
    for b in range(500):
        # Use condition a + b + c = 1000 to find c
        c = (1000 - a) - b
        # a < b < c
        if a < b < c:
            # Apply Pythagorean theorem
            if a ** 2 + b ** 2 == c**2:
                print('a : {0}, b : {1}, c : {2}, and abc is {3}'. format(a,b,c, a*b*c))
