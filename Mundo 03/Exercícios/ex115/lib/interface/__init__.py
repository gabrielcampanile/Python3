colors = {'clear': '\033[m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'purple': '\033[35m',
            'cyan': '\033[36m',
            'gray': '\033[37m',
            'white': '\033[30m'}


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os dados.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{colors["yellow"]}{c}{colors["clear"]} - {colors["blue"]}{item}{colors["clear"]}')
        c +=1
    print(linha())
    opc = leiaInt(f'{colors["green"]}Sua Opção: {colors["clear"]}')
    return opc