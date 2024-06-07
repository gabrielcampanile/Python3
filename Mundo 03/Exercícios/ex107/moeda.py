def metade(preço=0):
    preço /= 2
    return preço


def dobro(preço=0):
    preço *= 2
    return preço


def aumentar(preço=0, aum=0):
    preço += (preço * aum) / 100
    return preço


def diminuir(preço=0, red=0):
    preço -= (preço * red) / 100
    return preço
