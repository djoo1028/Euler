'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,

then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,

how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)

contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.

The use of "and" when writing out numbers is in compliance with British usage.

'''
# I am going to use dictionary at here
# because two values are paired
# Create dictionary directly

data = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
70: 'seventy', 80: 'eighty', 90: 'ninety'}

#Create dictionary by using list and zip
data1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100,1000]
data2 = '''one two three four five six seven eight nine ten 
eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
twenty thirty forty fifty sixty seventy eighty ninety hundred thousand'''

numbers = dict(zip(data1, data2.split()))

# combine letter function
def func(num):
    # when num is less than 100
    if num < 100:
        if num not in numbers:
            # if num does not exist, we can create liek down below
           numbers[num] = numbers[num - num % 10] + numbers[num % 10]
        return numbers[num]
    # when num is greater than 100 and less than 1000
    if num < 1000:
        # if num is divisible by 100 we do not have to add 'and'
        if num % 100 == 0:
            return numbers[num // 100] + numbers[100]
        # if num is not divisble by 100 we have to add 100 in the middle
        return numbers[num // 100] + numbers[100] + 'and' + numbers[num % 100]
    return 'one' + numbers[1000]

total = 0
for i in range(1,1001):
    value = func(i)
    total += len(value)
    print(i, value, len(value), total)