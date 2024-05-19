'''Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''

#print('='*10 + ' LOJAS CAMPANILE ' + '='*10)
print('{:=^40}'.format(' LOJAS CAMPANILE '))

preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    desconto = preço * 0.1
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preço - desconto))
elif opção == 2:
    desconto = preço * 0.05
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preço - desconto))
elif opção == 3:
    fatura = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(fatura))
    print('Sua compra vai custar R${:.2f} no final.'.format(preço))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = preço * 1.2
    fatura = juros / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, fatura))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, juros))
else:
    print('Opção inválida.')