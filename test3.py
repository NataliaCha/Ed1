numbers1 = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))
sum_elements_1 = 0             # Создание переменной для хранения суммы

for element in numbers1:
    sum_elements_1 += element # Добавляем текущий элемент к сумме

sum_elements_2 = 0             # Создание переменной для хранения суммы

for element in numbers2:
    sum_elements_2 += element # Добавляем текущий элемент к сумме

if sum_elements_1>sum_elements_2 :
    print(1)
else:
    print(2)