# Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
# números ímpares na lista IMPAR. Imprima as três listas.

import random

numeros = []
par = []
impar = []

while len(numeros) != 20:
    numeros.append(random.randrange(1,100))

for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(numeros)
print(par)
print(impar)