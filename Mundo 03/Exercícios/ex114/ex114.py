import urllib

import urllib.error
import urllib.parse
import urllib.request

try:
    site = urllib.request.urlopen('https://google.com.br')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print(f'Consegui acessar o site {(site.url).replace("https://", "").replace("www.", "").replace(".com", "").replace(".br", "").replace(".", " ").replace("/", "").title()} com sucesso.')
    # print(site.read())
    # help(urllib)
