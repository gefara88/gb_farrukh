print("Задача 3")
print("Вы вводите любую цифру а я считаю ее как цифра + две таких цифр + три таких цифр")
n = int(input(""))
num = str(n)
n1 = num + num
n2 = num + num + num
comp = n + int(n1) + int(n2)
print("итоговая цифра =", comp)
