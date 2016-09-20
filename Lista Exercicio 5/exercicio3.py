# Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também
# divisíveis por 7?

contador = 0
for n in range(1067, 3628):
    if n % 2 == 0 and n % 7 == 0:
        contador += 1

print(contador)