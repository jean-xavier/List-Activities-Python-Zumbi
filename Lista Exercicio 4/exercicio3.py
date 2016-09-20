# Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores. Imprima os três vetores.
import random

lista1 = []
lista2 = []
lista3 = []

while len(lista1) != 10:
    lista1.append(random.randrange(1,100))

while len(lista2) != 10:
    lista2.append(random.randrange(1,100))

for n in lista1:
    lista3.append(n)

for n in lista2:
    lista3.append(n)

print(lista1)
print(lista2)
print(lista3)