frase = input("Digite uma frase")
cont = 0

while cont < len(frase):
    if frase[cont] in 'aeiou':
        frase = frase[:cont] + '*' + frase[cont+1:]
        print (frase)
    cont = cont + 1
