def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a, b):
    return a ** (1/b)

def modulo(a):
    return abs(a)

def fatorial(a):
    if a == 0:
        return 1
    else:
        return a * fatorial(a-1)
    
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)
    
def mmc(a, b):
    return a * b // mdc(a, b)

def media(lista):
    return sum(lista) / len(lista)

def mediana(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        return (lista[n//2 - 1] + lista[n//2]) / 2
    else:
        return lista[n//2]
    
def moda(lista):
    contagem = {}
    for i in lista:
        if i in contagem:
            contagem[i] += 1
        else:
            contagem[i] = 1
    maximo = max(contagem.values())
    return [i for i in contagem if contagem[i] == maximo]