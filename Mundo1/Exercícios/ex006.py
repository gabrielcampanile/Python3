#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('N: '))
print('Dobro: {} \nTriplo: {} \nRaiz Quadrada: {:.2f}'.format(n*2, n*3, pow(n, (1/2))))