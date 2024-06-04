'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

turma = []
aluno = []
notas = []

while True:
    aluno.append(str(input('Nome: ')).strip().title())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    turma.append(aluno[:])
    notas.clear()
    aluno.clear()

    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp == 'n':
        break

print('-=' * 20)
print(f'{"Nº":<5}' + f'{"NOME":<12}' + f'{"MÉDIA"}')
print('-' * 22)
for n, a in enumerate(turma):
    print(f'{n:<5}' + f'{a[0]:<13}' + f'{(a[1][0] + a[1][1]) / 2:.2f}')

while True:
    print('-' * 40)
    i = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if i == 999:
        print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
        break
    if i <= len(turma) - 1:
        print(f'As notas de {turma[i][0]} são {turma[i][1]}')
    else:
        print('Aluno não encontrado. Digite novamente.')