# Parâmetros opcionais

def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')


soma(3, 2, 5)
soma(8, 4)
soma(2)
soma()
soma(c=3, a=2)