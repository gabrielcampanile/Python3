num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
print(num)
num.sort(reverse=True)
num.insert(2, 0) # Adiciona o 0 na posição 2
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.pop() # Remove o último elemento
num.pop(2) # Remove o elemento na posição 2
print(num)
num.remove(2) # Remove o primeiro elemento 2
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')