import requests

# ANSI escape sequence for yellow color
YELLOW = "\033[93m"

def verificar_acessibilidade(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(YELLOW + "O site está acessível.")
        else:
            print(YELLOW + "O site não está acessível.")
    except requests.exceptions.RequestException as e:
        print(YELLOW + "Ocorreu um erro ao tentar acessar o site:", e)

# Exemplo de uso
url = "http://127.0.0.1:5500/index.html"
verificar_acessibilidade(url)