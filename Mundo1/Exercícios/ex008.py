#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor em metros: '))
cm = m*100
mm = cm*10

print('{:.1f} metros == {:.1f} centímetros == {:.1f} milímetros'.format(m, cm, mm))