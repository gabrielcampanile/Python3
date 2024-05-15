#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input('Digite um valor em real: '))
dolares = reais / 5.09
libras = reais / 6.36
#08/05/2024

print('Você pode comprar ${:.2f} dólares ou £{:.2f} libras'.format(dolares, libras))