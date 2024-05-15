#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salary = float(input('Salário: R$'))

if salary > 1250:
    increase = salary * 10 / 100
    print('Salário após aumento de 10%: R${:.2f}'.format(salary + increase))
else:
    increase = salary * 15 / 100
    print('Salário após aumento de 15%: R${:.2f}'.format(salary + increase))