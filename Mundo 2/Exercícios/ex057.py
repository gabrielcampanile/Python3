'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MF':
    print('Dados inválidos. ', end='')
    sexo = str(input('Por favor, informe o seu sexo: ')).upper()

if sexo == 'M':
    print('Sexo MASCULINO registrado com sucesso!')
else:
    print('Sexo FEMININO registrado com sucesso!')