for count in range(1, 6):
    print('oi')
    print(count)
print('fim')

for count in range(6, 0, -1):
    print(count)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('Somatório de todoso os valores: {}'.format(s))