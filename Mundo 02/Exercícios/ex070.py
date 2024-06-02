'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. 
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

print('-' * 25 + '\n   LOJA SUPER BARATÃO   \n' + '-' * 25)

total = caro = barato = 0
baratonome = ''

while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    
    if total == 0 or preço < barato:
        barato = preço
        baratonome = nome
    if preço >= 1000:
        caro += 1
    total += preço

    opçao = ' '
    while opçao not in 'SsNn':
        opçao = str(input('Deseja adicionar mais um produto? [S/N] ')).strip().upper()[0]

    if opçao in 'Nn':
        # print('-' * 10 + 'FIM DO PROGRAMA' + '-' * 10)
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {baratonome} que custou R${barato:.2f}')
