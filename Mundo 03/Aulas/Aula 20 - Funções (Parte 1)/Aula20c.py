def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

# Programa Principal
soma(4,5)
soma(8,9)
soma(b=2,a=1)


def soma2(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma2(5,2)
soma2(2,9,4)

