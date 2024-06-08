'''Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), 
mas com uma validação de dados para aceitar apenas valores que seja monetários.'''

from utilidades import dado, moeda

p = dado.leiaDinheiro('Digite o valor: R$')
t = str(input('''[1] Real \t[2] Dólar \t[3] Euro
[4] Libra \t[5] Iene \t[6] Peso Argentino
[7] Won Sul-Coreano \t[8] Rúpia Indiana \t[9] Rublo Russo
Escolha a moeda: '''))
print(f'O valor convertido é {moeda.moeda(p, t)}')