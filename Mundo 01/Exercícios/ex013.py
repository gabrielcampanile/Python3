#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário: R$'))
aumento = salario * 15 / 100

print('Novo salário com aumento de 15%: R${:.2f}'.format(salario + aumento))