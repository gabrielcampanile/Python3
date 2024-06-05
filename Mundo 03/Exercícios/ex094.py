'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
 e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

pessoa = dict()
grupo = list()
media = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    grupo.append(pessoa.copy())

    resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while resp not in 'sn':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp in 'n':
        break

print('-=' * 30)
print(f'- O grupo tem {len(grupo)} pessoas.')

media /= len(grupo)
print(f'- A média de idade é de {media:.2f} anos.')

print(f'- As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()

print(f'- Lista das pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] > media:
        print(f'    Nome = {p["nome"]}; Sexo = {p["sexo"]}; Idade = {p["idade"]}')