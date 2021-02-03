# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Задание 1
listName = ['Марьяна', 'Галина ', 'Елена', 'Сона']
listName1 = ('Марьяна', 'Галина ', 'Елена', 'Сона')
listName2 = {'Марьяна': 27, 'Галина': 30, 'Елена': 50, 'Сона': 28}
print(type(listName))
print(type(listName1))
print(type(listName2))

# Задание 2

l = ["a", "l", "g", "o", "r", "y", "t", "m", "n"]

j = 0
for i in range(int(len(l) / 2)):
    l[j], l[j + 1] = l[j + 1], l[j]
    j += 2

print(l)

# Задание 3
month = int(input("Введите месяц - "))
weather = ("зима", "весна", "лето", "осень")
weather1 = {"1": "зима", "2": "зима", "3": "зима", "4": "весна", "5": "весна", "6": "весна", "7": "лето", "8": "зима", "9": "зима", "10": "зима", "11": "зима", "12": "зима"}
if 1 <= month <= 3:
    print("Это зимний месяц")
elif 4 <= month <= 6:
    print("Это весна")
elif 6 <= month <= 9:
    print("Это лето")
elif 9 <= month <= 11:
    print("Это осень")
else:
    print("Вы ввели не релевантное число")