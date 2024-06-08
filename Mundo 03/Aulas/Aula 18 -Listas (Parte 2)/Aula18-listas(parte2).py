teste = list()
teste.append('Gabriel')
teste.append(21)
galera = list()
# teste[:] cópia de teste
galera.append(teste[:])
teste[0] = 'Luana'
teste[1] = 20
galera.append(teste[:])
print(galera)