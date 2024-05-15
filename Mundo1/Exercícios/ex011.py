#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

heigh = float(input('Altura: '))
large = float(input('Largura: '))
area = heigh * large
paint = area // 2
resto = area % 2
print('Para pintar uma parade de {:.2f}m², será necessário {}l de tinta.'.format(area, paint+resto))