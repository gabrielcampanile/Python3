'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
No final, mostre:                                                                                                    
A) Quantas pessoas foram cadastradas.                                                                                                                
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.'''

pessoa = []
galera = []
pesado = []
leve = []

while True:
    pessoa.append(str(input('Nome: ')).strip().title())
    pessoa.append(int(input('Peso: ')))

    if len(galera) == 0:
        pesado.append(pessoa[:])
        leve.append(pessoa[:])
    else:
        if pessoa[1] >= pesado[0][1]:
            if pessoa[1] > pesado[0][1]:
                pesado.clear()
            pesado.append(pessoa[:])
        elif pessoa[1] <= leve[0][1]:
            if pessoa[1] < leve[0][1]:
                leve.clear()
            leve.append(pessoa[:])

    galera.append(pessoa[:])
    pessoa.clear()
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp == 'n':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {pesado[0][1]:.1f}Kg. Peso de ', end='')
for p in pesado:
    print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {leve[0][1]:.1f}Kg. Peso de ', end='')
for l in leve:
    print(f'{l[0]} ', end='')
print()
