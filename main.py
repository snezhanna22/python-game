#игра "камень, ножницы, бумага"

import random

print('-------------------------------------------')
print('Вы запустили игру "Камень, ножницы, бумага"')
print('Если хотите узнать свои баллы вводите "*"')
print('Начинаем игру...')

user_score = 0
pk_score = 0


while True:
    
    user = input('Выберите варинт:  "камень", "ножницы", "бумагу" или -(минус) для выхода: ').lower()
    options = ['камень', 'ножницы', 'бумага']
    random_pk = random.choice(options)
    print(f'Компьютер выбрал: {random_pk}.')

    if random_pk == user:
        print('Ничья! Вы выбрали одинаковый вариант.')
    elif user == 'камень':
        if random_pk == 'ножницы':
            print('Камень бьет ножницы. Вы выиграли')
            user_score += 1
        else:
            print('Бумага заварачивает камень. Вы проиграли.')
            pk_score += 1
    elif user == 'ножницы':
        if random_pk == 'камень':
            print ('Камень разбивает ножницы. Вы проиграли.')
            pk_score += 1
        else:
            print('Ножницы режут бумагу. Вы выиграли.')
            user_score += 1
    elif user == 'бумага':
        if random_pk == 'камень':
            print('Бумага заварачиивает камень. Вы выиграли.')
            user_score += 1
        else:
            print('Ножницы режут бумагу. Вы проиграли.')
            pk_score += 1
    elif user == '*':
        print(f'Ваши очки: {user_score}')
        print(f'Очки компьютера: {pk_score}')
    if user == '-':
        break