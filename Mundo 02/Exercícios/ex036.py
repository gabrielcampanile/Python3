'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestaçao = casa / (anos * 12)
porcentagem = (prestaçao * 100) / salario
aprovaçao = 1 if prestaçao <= salario * 30 / 100 else 0

print('Prestação: R${:.2f}'.format(prestaçao))
print('Equivale a {:.0f}% do salário'.format(porcentagem))

if aprovaçao:
    print('Empréstimo \033[32mAPROVADO\033[m')
else:
    print('Empresário \033[31mNEGADO\033[m')
    