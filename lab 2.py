#2.	Написати програму, яка запитує в користувача суму грошей в гривнях і переводить її в євро та долари.
баланс = int(input("Баланс в грн: "))
долари = round(баланс / 38.5, 2)
євро = round(баланс / 42, 2)
print("Баланс в доларах:", долари)
print("Баланс в євро:", євро)
