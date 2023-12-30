"""Нужно за 5 попыток угадать случайное число от 1 до 99"""
from random import randint

with open('003_game_points') as file:
    points = int(file.read())
print("Добро пожаловать в игру: 'Угадай число!'")
print('Вам нужно угадать число за 5 попыток')
request = input(f'У вас {points} очков. Хотите ли Вы начать игру? Y/N ')
while request.capitalize() == 'Y':
    number = randint(1, 100)
    attempts = 5
    win_points = 10000
    print('Я загадал число от 1 до 99.')
    while True:
        print(f'Возможный выигрыш: {win_points} очков!')
        user_number = input(f"Какое это число? ")
        while not user_number.isdigit():
            print("Вы ввели не число.")
            user_number = input(f"Так какое это число?")
        if int(user_number) == number:
            print(f"Поздравляю! Вы угадали и заработали {win_points} очков")
            points += win_points
            break
        else:
            if int(user_number) > number:
                print("Оно МЕНЬШЕ!")
            else:
                print("Оно БОЛЬШЕ!")
            attempts -= 1
            win_points = int(win_points / 2)
        if attempts == 0:
            print(f"У Вас закончились попытки, загаданное число равнялось: {number}. Мы убрали у вас 500 очков.")
            points -= 500
            break
    with open('003_game_points', 'w') as file:
        file.write(str(points))
    request = input(f'У вас {points} очков. Хотите ли Вы испытать удачу еще раз? Y/N ')
