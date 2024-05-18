ano = int(input('Digite o ano de nascimento: '))
idade = 2024 - ano
print(idade)

if idade < 10:
    print('MIRIM')
elif idade < 15:
    print('INFANTIL')
elif idade < 20:
    print('JÚNIOR')
elif idade < 22:
    print('SÊNIOR')
else:
    print('MASTER')