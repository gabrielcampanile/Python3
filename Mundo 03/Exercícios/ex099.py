from random import randint

def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
    tam = len(num)
    print(f'Foram informados {tam} ao todo.')
    maximo = max(num) if tam > 0 else 0
    print(f'O maior valor informado foi {maximo}')


i = randint(0, 10)
maior(2, 3, 4, 5, 13, 5, 0)