'''Escreva um programa em Python que leia um número inteiro qualquer
 e peça para o usuário escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão: 
      [ 1 ] converter para BINÁRIO
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEXADECIMAL''')

opçao = int(input('Sua opção: '))

if opçao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertirdo para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertirdo para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')