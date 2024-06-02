frase = 'Curso em Vídeo Python'
#FATIAMENTO
print(frase[9]) #9
print(frase[9:21]) #9 até 20
print(frase[9:21:2]) # 9 até 20 de 2 em 2
print(frase[:9]) #0 até 8
print(frase[9:]) #9 até o final
print(frase[9::3]) #9 até o final de 3 em 3

#ANÁLISE
print(len(frase)) #nº de caractéres
print(frase.count('o')) #nº de 'o'
print(frase.count('o', 0, 13)) #nº de 'o' de 0 a 12
print(frase.find('Vídeo')) #onde começa = 11 : frase(11)
print(frase.lower().find('vídeo'))
print(frase.find('android')) #não encontrou = -1
print('Curso' in frase) #TRUE

#TRANSFORMAÇÃO
print(frase.replace('Python', 'Android')) #Substitui 'Python' por 'Android'
frase = frase.replace('Python', 'Android')
print(frase.upper().count('O'))
print(frase.lower())
print(frase.capitalize()) #Deixa só a primeira maiúscula e o resto minúscula
print(frase.title()) #Deixa a primeira letra de cada palavra maiúscula e o resto minúscula
print(frase.strip()) #remove os espaços do início e do fim da string
print(frase.rstrip()) #remove somente os espaços da direita (fim) da string
print(frase.lstrip()) #remove somente os espaços da esquerda (início) da string

#DIVISÃO
print(frase.split()) #separa as palavras da string e cria uma lista
dividido = frase.split()
print(dividido[0])
print(dividido[2][3]) #3ª letra da 2ª palavra

#JUNÇÃO
print('-'.join(frase)) #junta as palavras separadas = Curso-em-Vídeo-Python