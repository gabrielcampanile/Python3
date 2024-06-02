'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date

atual = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('Ao todo tivemos {} pessoas menores de idade.'.format(menor))