'''
OPERADORES ARITMÉTICOS:
+ ADIÇÃO            EX: 5+2 == 7
- SUBTRAÇÃO         EX: 5-2 == 3
* MULTIPLICAÇÃO     EX: 5*2 == 10
/ DIVISÃO           EX: 5/2 == 2.5
** POTÊNCIA         EX: 5**2 == 25
// DIVISÃO INTEIRA  EX: 5//2 == 2
% RESTO DE DIVISÃO  EX: 5%2 == 1

PRECEDÊNCIA:
1 ()
2 **
3 * / // %
4 + -
'''

nome = input('Qual é o seu nome: ')
print('Prazer em te conhecer {:>20}'.format(nome))
print('Prazer em te conhecer {:<20}'.format(nome))
print('Prazer em te conhecer {:^20}'.format(nome))
print('Prazer em te conhecer {:=^20}'.format(nome))

