p1 = float(input('Digite a sua primeira nota: '))
p2 = float(input('Digite a sua segunda nota: '))
media = (p1 + p2) / 2

cores = {'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'limpa': '\033[m'}

if media < 5.0:
    print('{}REPROVADO!{}'.format(cores['vermelho'], cores['limpa']))
elif 5.0 <= media < 7.0:
    print('{}RECUPERAÇÃO!{}'.format(cores['amarelo'], cores['limpa']))
else:
    print('{}APROVADO!{}'.format(cores['azul'], cores['limpa']))