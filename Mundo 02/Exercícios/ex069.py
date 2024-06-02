'''Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

maior = totM = Fnova = 0

while True:
    print('-' * 25 + '\n   CADASTRE UMA PESSOA   \n' + '-' * 25)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    
    sexo = 'x'
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip()
    if sexo in 'Mm':
        totM += 1
    elif sexo in 'Ff' and idade < 20:
        Fnova +=1

    opçao = 'x'
    while opçao not in 'SsNn':
        opçao = str(input('-' * 25 + '\nQuer continuar? [S/N] ')).strip().upper()[0]
    if opçao in 'Nn':
        print('=' * 5 + 'FIM DO PROGRAMA' + '=' * 5)
        break

print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {totM} homens cadastrados')
print(f'E temos {Fnova} mulheres com menos de 20 anos')
