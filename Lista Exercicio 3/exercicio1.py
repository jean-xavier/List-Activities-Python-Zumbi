n = -1
while n < 0 or n > 10:
    n = int(input("Digite uma nota: "))
    if n < 0 or n > 10:
        print("Valor digitado invalido!")