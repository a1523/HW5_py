# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф

from random import *
import os

def player_vs_player():
    candies_total = 120
    max_take = 28
    count = 0
    player1 = input('Введите имя игрока 1: ')
    player2 = input('Введите имя игрока 2: ')
    print('Первым будет ходить ...')

    x = randint(1,2)
    if x == 1:
        lucky = player1
        loser = player2
    else:
        lucky = player2
        loser = player1
    print(f'Поздравляю {lucky}, ты ходишь первым!')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'{lucky}, сколько Вы возьмете конфет? '))
            while step > candies_total or step > max_take:
                step = int(input(f'{lucky}, можно взять не больше {max_take} конфет. Попробуйте еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'На кону еще {candies_total} конфет')
            count = 1
        else:
            print('Конец игры')
        
        if count == 1:
            step = int(input(f'{loser}, сколько Вы возьмете конфет? '))
            while step > candies_total or step > max_take:
                step = int(input(f'{loser}, можно взять не больше {max_take} конфет. Попробуйте еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'На кону еще {candies_total} конфет')
            count = 0
        else:
            print('Конец игры')


    if count == 1:
        print(f'{loser} победил')
    if count == 0:
        print(f'{lucky} победил')

player_vs_player()


