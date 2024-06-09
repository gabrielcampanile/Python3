''' 115a: Vamos criar um menu em Python, usando modularização.
    115b: Vamos ver como fazer acesso a arquivos usando o Python.
    115c: Vamos finalizar o projeto de acesso a arquivos em Python.'''

from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
pasta = 'C:/Users/gabri/OneDrive/Documentos/Programação/Curso em Vídeo/Python3/Mundo 03/Exercícios/ex115'

if not arquivoExiste(arq, pasta):
    criarArquivo(arq, pasta)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Função para listar pessoas cadastradas
        lerArquivo(arq, pasta)
    elif resposta == 2:
        # Opção para cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).title() 
        idade = leiaInt('Idade: ')
        cadastrar(arq, pasta, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print(f'{colors["red"]}ERRO! Digite uma opção válida!{colors["clear"]}')
    sleep(2)