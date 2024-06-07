def moeda(preço=0, moeda='R$'):
    """
    -> Formata um valor para a moeda brasileira.
    :param preço: O valor a ser formatado.
    :param moeda: (opcional) O tipo de moeda a ser utilizado.
    :return: O valor formatado.
    """
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
