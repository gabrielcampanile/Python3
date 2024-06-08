def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    valor = 0

    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    
    return valor


# def leiaDinheiro(msg):
#     valor = 0

#     while True:
#         n = str(input(msg)).replace(',','.')
#         if n.isnumeric():
#             valor = float(n)
#             break
#         else:
#             print(f'\033[0;31mERRO! "{n}" é um preço inválido!\033[m')
    
#     return valor