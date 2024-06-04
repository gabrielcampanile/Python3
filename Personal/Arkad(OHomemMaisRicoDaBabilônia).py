s = float(input('Digite o seu salário: '))
r = s * 0.1
v = s * 0.7
c = s * 0.2
t = r + v + c
print(f'De acordo com os conhecimentos de Arkad, o homem mais rico da Babilônia, você deveria:')
print(f'Adicionar à sua reserva {r:.2f} do seu salário,\nPassar o mês (sabiamente) com {v:.2f}\nE pagar as suas contas com {c:.2f}')
print('Dessa forma, você estará no caminho para o sucesso financeiro!')
print(f'{t}')