print("Это экспериментальный чат бот, введите свое имя")
name = input("")
print("Очень счастлив с вами познакомиться, " + name + " меня завут Monty Python, можно просто Пай")
print("Увачаемый " + name + " сколько вам лет?")
age = int(input(""))
if age >= 18:
    print("Все по закону я могу, с вами общаться?")
    print(name + " вы мне очень понравились, но я на работе.")
    print(name + " могу с вами выйти на связь завтра в это время?")
    que = input("")
    if que == "да" or que == "Да" or que == "Yes" or que == "yes" or que == "da" or que == "Da":
        print("Я безмерно счастлив. Берегите себя, я буду жадать с не терпением нашего следующего чата :).")
    else:
        print("Пожалуйста извините меня, мне жаль но я все таки должен идти :(")
else:
    print("Я не могу общаться с не совершеннолетними без присутствия взрослых.")
    print(name + " Даже если рядом есть взрослый рядом вы не в моем вкусе извините.")
