'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

# Tried to find the 2 ^ 1000 by using while loop
# However, there is no time difference between while loop and direct caclulation
# i = 1
# while i < 1001:
#     result = 2 ** i
#     result
#     i += 1
#print(2 ** 1000)
result = 2 ** 1000
# Make a result as string to read each letter
final = str(result)
summation = 0
for i in range(len(final)):
    # make int to calculate
    summation += int(final[i])
# final result of sum
print(summation)
