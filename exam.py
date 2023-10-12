"""import random

with open('cities.txt', 'r') as file:
    cities = [i.strip().lower() for i in file]
count = 0
while len(cities) > 0:
    count += 1
    user = input('Введите название города: ').lower()
    end_with = [i for i in cities if i[0] == user[-1]]
    choise = random.choice(end_with)
    if user not in cities:
        print('Такого города нет в списке')
    elif user in cities:
        cities.remove(choise)
        print(f'{choise.capitalize()}')

    if count > 1:
        if user[0] != choise[-1]:
            print('Первая буква не совпадает с последней')"""

import random

with open('cities.txt', 'r') as file:
    cities = [i.strip().lower() for i in file]
count = 0
while len(cities) > 0:
    count += 1
    user = input('Введите название города: ').lower()
    end_with = [i for i in cities if i[0] == user[-1]]
    choise = random.choice(end_with)

    if user not in cities:
        print('Такого города нет в списке')
    if user in cities:
            cities.remove(choise)
            print(f'{choise.capitalize()}')
            if count > 1 and user[0] != choise[-1]:
                print('Первая буква не совпадает с последней')
