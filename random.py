import random

MAX_GUESSES = 0

print('-----------------Угадай число-------------------')
name = input('Привет, как я могу к тебе обращаться? ')
print()
print(f'Я загадаю число от 1 до 30. {name} у тебя 6 попыток чтобы угадать число. Поехали!')
print('---------------------------------------------------------')

number = random.randint(1, 30)

while MAX_GUESSES < 6:
    guess = int(input('Введи число:'))
    MAX_GUESSES += 1

    if guess < number:
        print('Твое число меньше того, что я загадал')
    
    if guess > number:
        print('Твое число больше того, что я загадал')

    if guess == number:
        break

if guess == number:
    print(f'{name} ты угадал(а) число, использовав {MAX_GUESSES} попыток.')
else:
    print(f'Увы ты не угадал(а) число. Я загадал число {number}')