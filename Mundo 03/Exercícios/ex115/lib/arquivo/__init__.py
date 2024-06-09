from lib.interface import *


def arquivoExiste(arq, pasta):
    caminho = pasta + '/' + arq
    try:
        a = open(caminho, 'rt') #read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arq, pasta):
    caminho = pasta + '/' + arq
    try:
        a = open(caminho, 'wt+') # write text  + (create if it doesn't exist)
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def lerArquivo(arq, pasta):
    caminho = pasta + '/' + arq
    try:
        a = open(caminho, 'rt')
    except:
        print('Erro ao tentar ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<34}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, pasta, nome='desconhecido', idade=0):
    caminho = pasta + '/' + arq
    try:
        a = open(caminho, 'at') #append text
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()