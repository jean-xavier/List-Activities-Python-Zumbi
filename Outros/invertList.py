cont = 0
lista = []

while cont < 10:
    x = int(input("Digite o %i° numero: "%(cont + 1)))
    lista.append(x)
    cont = cont + 1

while cont != 0:
    cont = cont - 1
    print(lista[cont])
    