#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Velocidade do carro: '))

if vel > 80:
    multa = (vel - 80) * 7
    print('\033[31mVocê foi multado!\nA multa vai custar R${:.2f}\033[m'.format(multa))
else:
    print('\033[32mSe safou!\033[m')