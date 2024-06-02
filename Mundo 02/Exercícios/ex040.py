'''Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''

p1 = float(input('Digite a sua primeira nota: '))
p2 = float(input('Digite a sua segunda nota: '))
media = (p1 + p2) / 2

cores = {'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'limpa': '\033[m'}

print('Sua média é {:.2f}'.format(media))
if media < 5.0:
    print('{}REPROVADO!{}'.format(cores['vermelho'], cores['limpa']))
elif 5.0 <= media < 7.0:
    print('{}RECUPERAÇÃO!{}'.format(cores['amarelo'], cores['limpa']))
else:
    print('{}APROVADO!{}'.format(cores['azul'], cores['limpa']))