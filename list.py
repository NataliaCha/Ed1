numbers =[1,45,89,45,-67, 55.6]
persona = ['Sofia','Leon','Amelia']
result = numbers[5] + numbers[0]
# print(numbers[2])
print(result)
print(len(numbers)) # know the lenght for the list
print(numbers[-1])# to call the last element in the list
print(numbers[-2])# to call the pre last element in the list
print(numbers[2:4]) # part of the list (the last element is not included)
print(numbers[0:-2])
print(numbers[4:])
numbers.append(123)# to add to the list
print(numbers)

newlist=[numbers,persona]
print(newlist)
newnewwlist = [numbers[0:],persona[0:]]
print(newnewwlist)
new_1list=[]
new_1list=numbers+persona
print(new_1list)