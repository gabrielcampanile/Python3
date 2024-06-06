from time import sleep

def contagem(i, f, p):
    print(i, end=' ')
    if i == f:
        print('FIM!')
        return
    contagem(i + p, f, p)

def contador(i, f, p):
    print('-=' * 30)
    if p == 0:
        p = 1
    elif p < 0:
        p = abs(p)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        contagem(i, f, p)
    elif i > f:
        contagem(i, f, -p)


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input(f'{"Início:":<8}'))
f = int(input(f'{"Fim:":<8}'))
p = int(input(f'{"Passo:":<8}'))
contador(i, f, p)