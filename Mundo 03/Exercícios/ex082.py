''' Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''

valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

pares = []
impares = []

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')