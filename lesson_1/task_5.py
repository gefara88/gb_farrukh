print("Задача 5")
print("Выручка и издержки фирмы")
print("введите выручку фирмы")
income = int(input(""))
print("введите издержку фирмы")
loss = int(input(""))
if income < loss:
    print("убыток — издержки больше выручки")
elif income == loss:
    print("убытки и выручка равны")
elif income > loss:
    print("выручка больше убытков")
    incomer = income / loss
    print("рентабельность выручки =", incomer)
    print("для расчета прибыли фирмы в расчете на одного сотрудника введите число сотрудников")
    emp = int(input(""))
    ppe = (income - loss) / emp
    print("расчета прибыли фирмы в расчете на одного сотрудника =", ppe)
