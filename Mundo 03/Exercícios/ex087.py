'''Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.                                    
C) O maior valor da segunda linha.'''

matriz = []
somaPar = somaCol3 = maiorLin2 = 0

for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz.append(n)
        if n %  2 == 0:
            somaPar += n
        if j == 2:
            somaCol3 += n
        if i == 1:
            if j == 0:
                maiorLin2 = n
            elif n > maiorLin2:
                maiorLin2 = n

print('-=' * 20)
for pos, m in enumerate(matriz):
    print(f'[ {m} ]', end='')
    if (pos + 1) % 3 == 0:
        print()
print('-=' * 20)

print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaCol3}')
print(f'O maior valor da segunda linha é {maiorLin2}')