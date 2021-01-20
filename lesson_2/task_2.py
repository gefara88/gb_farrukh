print("Задача 2")
print("Обмен значений соседних элементов")
first_data = int(input("Введите количество элементов"))
list_ = []
a = 0
b = 0
while a < first_data:
    list_.append(input("Введите следующее значение "))
    a += 1

for s in range(int(len(list_) / 2)):
    list_[b], list_[b + 1] = list_[b + 1], list_[b]
    b += 2
print(list_)
