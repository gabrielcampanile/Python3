'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep
from random import randint

def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.5)
    tam = len(num)
    print(f'Foram informados {tam} ao todo.')
    maximo = max(num) if tam > 0 else 0
    print(f'O maior valor informado foi {maximo}')


i = randint(0, 10)
maior(2, 3, 4, 5, 13, 5, 0)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()