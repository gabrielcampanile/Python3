def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def metade(preço=0, form=False):
    preço /= 2
    return preço


def dobro(preço=0, form=False):
    preço *= 2
    return preço


def aumentar(preço=0, aum=0, form=False):
    preço += (preço * aum) / 100
    return preço


def diminuir(preço=0, red=0, form=False):
    preço -= (preço * red) / 100
    return preço
