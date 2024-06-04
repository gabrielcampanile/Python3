'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

valores = []

while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 20)
# valores.sort()
print(sorted(valores))