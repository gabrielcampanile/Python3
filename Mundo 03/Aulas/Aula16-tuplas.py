# Tuplas são imutáveis
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# print(lanche) #('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# print(lanche[2]) #Pizza
# print(lanche[-1]) #Pudim
# print(lanche[1:3]) #('Suco', 'Pizza')
# print(lanche[:2]) #('Hambúrguer', 'Suco')
# print(lanche[2:]) #('Pizza', 'Pudim')
# print(lanche[-3:]) #('Suco', 'Pizza', 'Pudim')

for comida in lanche:
    print(f'Eu vou comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

print(sorted(lanche))