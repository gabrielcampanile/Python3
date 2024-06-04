'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expressao = str(input('Digite a expressão: '))
# esq = expressao.count('(')
# dir = expressao.count(')')

# if esq != dir:
#     print('Sua expressão está errada!')
# else:
#     print('Sua expressão está válida!')

pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) != 0:
    print('Sua expressão está errada!')
else:
    print('Sua expressão está válida!')