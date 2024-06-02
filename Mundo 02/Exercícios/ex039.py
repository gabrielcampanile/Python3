'''Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

sexo = str(input('Você é homem ou mulher? ')).lower()

if sexo == 'mulher':
    print('Você não precisa realizar o alistamento militar obrigatório.')
elif sexo == 'homem':
    nasc = int(input('Digite o ano de nascimento: '))
    atual = date.today().year
    idade = atual - nasc
    tempo = abs(18 - idade)

    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

    if idade < 18:
        print('\033[32mAinda faltam {} anos para o alistamento!\033[m'.format(tempo))
        print('Seu alistamento será em {}'.format(atual + tempo))
    elif idade == 18:
        print('\033[33mChegou a sua hora de servir!\033[m')
        print('Você deve se alistar IMEDIATAMENTE!')
    else:
        print('\033[31mVocê já deveria ter se alistado há {} anos\033[m'.format(tempo))
        print('Seu alistamento foi em {}'.format(atual - tempo))
else:
    print('Sexo inválido.')