cont = 0
consoantes = 0

while cont < 10:
    letra = str(input("Digite a %i° letra: "%(cont + 1)))
    if letra in 'aeiou':
        consoantes += 1
    cont += 1
    
print ("Foram digitadas %i consoante(s)" % consoantes)