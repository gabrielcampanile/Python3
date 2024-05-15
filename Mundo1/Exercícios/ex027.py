#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
nombre = nome.title().split()

print('Olá sr(a). {}. Ou devo chamá-lo de {}?'.format(nombre[len(nombre)-1], nombre[0]))