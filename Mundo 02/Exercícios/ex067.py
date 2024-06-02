'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.'''

while True:
    print('-' * 37)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 37)
    if num < 0:
        break
    else:
        for tab in range(1, 11):
            print(f'{num} x {tab} = {num * tab}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')