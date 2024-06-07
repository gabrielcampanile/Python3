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
    

# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')