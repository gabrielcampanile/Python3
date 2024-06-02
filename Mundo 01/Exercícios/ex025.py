#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite o seu nome completo: ')).strip() #remove os espaços do início e do fim da string

print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))