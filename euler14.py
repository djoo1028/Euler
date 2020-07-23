'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.

Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

'''
# Import time to check calculation time
import time
start = time.time()

# The maximum number of chain
max_cnt = 0
# The number when the number has the maximum chain
value = 0
# Check the the number from 1 to 1000000
for n in range(1, 1000000):
    cnt = 0
    # To store the number because n keep chainging by iterating
    temp = n

    # Infinite loop
    while True:
        # Break when n is 1
        if n == 1:
            # when n is 1 check the number of chain
            # If we find the different maximum number of chain
            # Then it will change the numbers as well
            if cnt > max_cnt:
                max_cnt = cnt
                value = temp
            break
        # collatz condition
        # when the number is even divide by 2
        # when the number is odd 3n + 1
        if (n % 2 == 0):
            n = n // 2
            cnt += 1
        else:
            n = 3 * n + 1
            cnt += 1
# Print the result
print(max_cnt, value) # 524, 837799
# Check the calculation time
print('time :', time.time() - start) # 26.344