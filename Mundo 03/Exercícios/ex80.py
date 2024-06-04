'''Crie um programa onde o usuário possa digitar cinco valores numéricos e 
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.'''

valores = list()

for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        for v in valores:
            i = valores.index(v)
            if n <= v:
                valores.insert(i, n)
                print(f'Adicionado na posição {i} da lista...')
                break

print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')