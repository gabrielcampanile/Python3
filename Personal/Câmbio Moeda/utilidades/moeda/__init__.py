def resumo(preço=0, aum=0, red=0):
    """
    -> Exibe um resumo do valor informado.
    :param preço: O valor a ser analisado.
    :param aum: O percentual de aumento.
    :param red: O percentual de redução.
    """
    print(f'{"-"*32}\n{"RESUMO DO VALOR".center(32)}\n{"-"*32}')
    print(f'Preço analisado:\t{moeda(preço)}')
    print(f'Dobro do preço:\t\t{dobro(preço, True)}')
    print(f'Metade do preço:\t{metade(preço, True)}')
    print(f'{aum}% de aumento:\t\t{aumentar(preço, aum, True)}')
    print(f'{red}% de redução:\t\t{diminuir(preço, red, True)}')
    print('-' * 32)


def moeda(preço=0, moeda='R$'):
    """
    -> Formata um valor para a moeda.
    :param preço: O valor a ser formatado.
    :param moeda: (opcional) O tipo de moeda a ser utilizado.
    :return: O valor formatado.
    """
    if moeda == '1' or moeda == 'R$' or moeda == 'BRL' or moeda == 'Real' or moeda == 'Reais':
        moeda = 'R$'
        preço = preço
    elif moeda == '2' or moeda == '$' or moeda == 'US$' or moeda == 'USD' or moeda == 'Dólar' or moeda == 'Dolar' or moeda == 'Dólares' or moeda == 'Dolares' or moeda == 'Dólares Americanos' or moeda == 'Dolares Americanos' or moeda == 'Dólar Americano' or moeda == 'Dolar Americano':
        moeda = 'US$'
        preço /= 5.38
    elif moeda == '3' or moeda == '€' or moeda == 'EUR' or moeda == 'Euro' or moeda == 'Euros':
        moeda = '€'
        preço /= 6.37
    elif moeda == '4' or moeda == '£' or moeda == 'GBP' or moeda == 'Libra' or moeda == 'Libras' or moeda == 'Libras Esterlinas':
        moeda = '£'
        preço /= 7.42
    elif moeda == '5' or moeda == '¥' or moeda == 'JPY' or moeda == 'Iene' or moeda == 'Ienes' or moeda == 'Ienes Japoneses':
        moeda = '¥'
        preço /= 0.049
    elif moeda == '6' or moeda == 'ARS' or moeda == 'Peso' or moeda == 'Pesos' or moeda == 'Pesos Argentinos':
        moeda = '$'
        preço /= 0.057
    elif moeda == '7' or moeda == '₩' or moeda == 'KRW' or moeda == 'Won' or moeda == 'Wons' or moeda == 'Wons Sul-Coreanos':
        moeda = '₩'
        preço /= 0.0048
    elif moeda == '8' or moeda == '₹' or moeda == 'INR' or moeda == 'Rúpia' or moeda == 'Rúpias' or moeda == 'Rúpias Indianas':
        moeda = '₹'
        preço /= 0.073
    elif moeda =='9' or moeda == '₽' or moeda == 'RUB' or moeda == 'Rublo' or moeda == 'Rublos' or moeda == 'Rublos Russos':
        moeda = '₽'
        preço /= 0.073
    else:
        preço = preço

    return f'{moeda}{preço:.2f}'.replace('.', ',')


def metade(preço=0, form=False):
    """
    -> Calcula a metade de um valor.
    :param preço: O valor a ser calculado.
    :param form: (opcional) Se deseja ou não formatar o valor.
    :return: O valor da metade do preço.
    """
    preço /= 2
    return preço if not form else moeda(preço)


def dobro(preço=0, form=False):
    """
    -> Calcula o dobro de um valor.
    :param preço: O valor a ser calculado.
    :param form: (opcional) Se deseja ou não formatar o valor.
    :return: O valor do dobro do preço.
    """
    preço *= 2
    return preço if not form else moeda(preço)


def aumentar(preço=0, aum=0, form=False):
    """
    -> Calcula o aumento de um valor.
    :param preço: O valor a ser calculado.
    :param aum: O percentual a ser aumentado.
    :param form: (opcional) Se deseja ou não formatar o valor.
    :return: O valor com o aumento do preço.
    """
    preço += (preço * aum) / 100
    return preço if not form else moeda(preço)


def diminuir(preço=0, red=0, form=False):
    """
    -> Calcula a redução de um valor.
    :param preço: O valor a ser calculado.
    :param red: O percentual a ser reduzido.
    :param form: (opcional) Se deseja ou não formatar o valor.
    :return: O valor com a redução do preço.
    """
    preço -= (preço * red) / 100
    return preço if not form else moeda(preço)


def dolar(preço=0, moeda='US$'):
    """
    -> Formata um valor para a moeda americana.
    :param preço: O valor a ser formatado.
    :param moeda: (opcional) O tipo de moeda a ser utilizado.
    :return: O valor formatado.
    """
    preço /= 5.38
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def euro(preço=0, moeda='€'):
    """
    -> Formata um valor para a moeda europeia.
    :param preço: O valor a ser formatado.
    :param moeda: (opcional) O tipo de moeda a ser utilizado.
    :return: O valor formatado.
    """
    preço /= 6.37
    return f'{moeda}{preço:.2f}'.replace('.', ',')