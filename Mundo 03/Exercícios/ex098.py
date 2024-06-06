''' Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

from time import sleep

def contagem(i, f, p):
    if (p > 0 and i > f) or (p < 0 and i < f):
        print('FIM!')
        sleep(0.5)
        return
    print(i, end=' ', flush=True)
    sleep(0.5)
    contagem(i + p, f, p)

def contador(i, f, p):
    print('-=' * 30)
    if p == 0:
        p = 1
    elif p < 0:
        p = abs(p)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i < f:
        contagem(i, f, p)
    elif i > f:
        contagem(i, f, -p)


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input(f'{"Início:":<8}'))
f = int(input(f'{"Fim:":<8}'))
p = int(input(f'{"Passo:":<8}'))
contador(i, f, p)