ano = int(input('Digite o ano de nascimento: '))
idade = 2024 - ano
print(idade)

if idade < 18:
    print('Você ainda vai ser alistar ao serviço militar.')
    print('\033[32mFaltam {} anos!\033[m'.format(18 - idade))
elif idade == 18:
    print('Chegou a sua hora de se alistar!')
else:
    print('\033[31mJá passou do prazo de alistamento há {} anos\033[m'.format(idade - 18))