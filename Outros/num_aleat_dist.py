import random

numeros_inteiros = []

while len(numeros_inteiros) != 15:
    num_aleatorio = random.randint(10, 100)
    if num_aleatorio not in numeros_inteiros:
        numeros_inteiros.append(num_aleatorio)

numeros_inteiros.sort()
print(numeros_inteiros)
