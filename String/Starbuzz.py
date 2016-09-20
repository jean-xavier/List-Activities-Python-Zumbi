import urllib.request
import time

def pega_preco():
    # pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
    pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    texto = pagina.read().decode('utf8')
    onde = texto.find('>$')
    inicio = onde + 2
    fim = inicio + 4
    return float(texto[inicio:fim])

# opcao = input("Deseja comprar já? (S/N)")
opcao = ''

if opcao == 'S':
    preco = pega_preco()
    print ("Comprar! Preço: %5.2f" % preco)
else:
    preco = 99.99
    while preco >= 4.74:
        preco = pega_preco()
        if preco >= 4.74:
            time.sleep(10)
            # time.sleep(600)
    print ("Comprar! Preço: %5.2f" % preco)
