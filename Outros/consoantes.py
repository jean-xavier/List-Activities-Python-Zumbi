letras = []
cont = 0
consoantes = 0

while cont < 10:
    letra = str(input("Digite a %i° letra: "%(cont + 1)))
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        consoantes = consoantes + 1
    cont = cont + 1
    
print ("Foram digitadas %i consoante(s)" % consoantes)

