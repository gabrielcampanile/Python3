'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

turma = []

while True:
    nome = str(input('Nome: ')).strip().title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    turma.append([nome, [n1, n2], media])

    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp == 'n':
        break

print('-=' * 20)
print(f'{"Nº":<5}{"NOME":<12}{"MÉDIA":>8}')
print('-' * 22)
for n, a in enumerate(turma):
    print(f'{n:<5}{a[0]:<13}{a[2]:>8.1f}')

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