# put your python code here
numbers = list(map(int, input().split()))
i = 0  ## first max
a = 0  ## second max
for number in numbers:
    if i < number:
        i = number
print(i)
# a = 0
# for number in numbers:
#     while a < number and a < i:
#         a = number
#     if a==i:
#         break
for number in numbers:
    if number == i:
        continue
    if a < number:  ##i=15
        a = number
#
print(a)
