#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

msg = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(msg))
print('Só tem espaços? ', msg.isspace())
print('É um número? ', msg.isnumeric())
print('É alfabético? ', msg.isalpha())
print('É alfanumérico? ', msg.isalnum())
print('Está em maiúsculas? ', msg.isupper())
print('Está em minúsculas? ', msg.islower())
print('Está capitalizada? ', msg.istitle())