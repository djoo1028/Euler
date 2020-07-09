'''

Each new term in the Fibonacci sequence is generated by adding the previous two terms.

By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''

# def fibonacci(arg1):
#     a = arg1
#     x = 1
#     y = 1
#     arr = []
#     for i in range(a-1):
#         temp = y
#         z = x + y
#         x = temp
#         y = z
#         arr.append(z)
#     print(list(arr))
#     #
#     sum = 0
#     for i in range(len(arr)):
#         if i % 2 == 0:
#             sum += arr[i]
#         else:
#             pass
#     print(sum)
#
# x = int(input())
#
# fibonacci(x)

x = 1
y = 2
result = 2
while True:
    data = x + y
    if data > 4000000:
        break
    if  data % 2 == 0:
        result += data
    x = y
    y = data

print(result)