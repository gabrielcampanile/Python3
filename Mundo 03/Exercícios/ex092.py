'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import date

clt = {}

clt['nome'] = str(input('Nome: ')).strip().title()
ano = int(input('Ano de Nascimento: '))
clt['idade'] = date.today().year - ano
clt['ctps'] = int(input('Carteira de Trabalho: (0 não tem) '))
if clt['ctps'] > 0:
    clt['contratação'] = int(input('Ano de Contratação: '))
    clt['salário'] = float(input('Salário: R$'))
    clt['aposentadoria'] = -(date.today().year - clt['contratação'] - 35 - clt['idade'])

print('-=' * 40)
print(clt)
for k, v in clt.items():
    print(f'{k} tem o valor {v}')