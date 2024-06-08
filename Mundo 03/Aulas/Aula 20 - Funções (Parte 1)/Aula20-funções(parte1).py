def lin():
    print('-' * 30)


# Programa Principal deve ter duas linhas de espaço
lin()
print('Curso em Vídeo')
lin()
print('Aprenda Python')
lin()
print('Gustavo Guanabara')
lin()

# Função com parâmetro
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem(f'{"Curso em Vídeo":^30}')
mensagem(f'{"Aprenda Python":^30}')
mensagem(f'{"Gustavo Guanabara":^30}')