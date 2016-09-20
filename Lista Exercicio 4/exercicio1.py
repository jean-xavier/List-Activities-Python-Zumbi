# Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
# as funções max e min.

import random
maior = 0
numeros = []

while len(numeros) != 10:
    numeros.append(random.randrange(0, 100)) 
print(numeros)

for numero in numeros:
    if numero > maior:
        maior = numero
print(maior)

menor = maior
for numero in numeros:
    if numero < menor:
        menor = numero
print(menor)