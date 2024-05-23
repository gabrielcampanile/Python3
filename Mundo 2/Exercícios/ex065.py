''' Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

cont = soma = media = maior = menor = 0
resp = 'S'

while resp in 'Ss':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))