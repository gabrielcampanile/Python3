a = [2, 3, 4, 7]
b = a # Cria uma ligação entre as duas listas
b[2] = 8
print('Ligação entre listas')
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]
b = a[:] # Cria uma cópia da lista
b[2] = 8
print('Cópia de listas')
print(f'Lista A: {a}')
print(f'Lista B: {b}')