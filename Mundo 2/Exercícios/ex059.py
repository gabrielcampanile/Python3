'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0

while opçao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opçao = int(input('>' * 5 + ' Qual é a sua opção? '))
    
    if opçao == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opçao == 2:
        print('O resultado entre {} x {} é {}'.format(n1, n2, n1 * n2))
    elif opçao == 3:
        print('Entre {} e {}, o maior valor é '.format(n1, n2), end='')
        if n1 >= n2:
            print(n1)
        else:
            print(n2)
    elif opçao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    
    print('=-=' * 10)
    sleep(3)
