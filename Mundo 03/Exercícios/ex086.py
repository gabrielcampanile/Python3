'''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.'''

matriz = []

for i in range(0, 3):
    for j in range(0, 3):
        matriz.append(int(input(f'Digite um valor para [{i}, {j}]: ')))

print('-=' * 20)
for pos, m in enumerate(matriz):
    print(f'[ {m} ]', end='')
    if (pos + 1) % 3 == 0:
        print()