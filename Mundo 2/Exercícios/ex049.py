n = int(input('Escolha um número: '))
print('Tabuada do {}:'.format(n))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n * c))