'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
só que agora utilizando um laço for.'''

n = int(input('Escolha um número: '))
print('Tabuada do {}:'.format(n))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n * c))