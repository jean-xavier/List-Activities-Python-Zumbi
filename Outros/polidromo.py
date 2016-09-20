palavras = input("Digite uma palavra ou frase: ")
palavra = ''
for letra in palavras:
    if letra != ' ':
        palavra += letra
print('"%s" é polidromo!' %palavras) if palavra[::-1] == palavra else print('"%s" não é polidromo!' %palavras)
