'''
dados = () ou dados = tuple()
dados = [] ou dados = list()
dados = {} ou dados = dict()
'''
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('-' * 30)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-' * 30)
for k in pessoas.keys():
    print(k)
print('-' * 30)
for v in pessoas.values():
    print(v)
print('-' * 30)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-' * 30)
# Funciona sem precisar do .append() ou .remove()
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')