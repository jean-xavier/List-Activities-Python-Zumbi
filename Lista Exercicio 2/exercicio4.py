# Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input("Digite o valor de n1: "))
n2 = float(input("Digite o valor de n2: "))
n3 = float(input("Digite o valor de n3: "))

if n1 > n2 and n1 > n3:
    print("Maior numero %.2f"%n1)
elif n2 > n1 and n2 > n3:
    print("Maior numero %.2f"%n2)
else:
    print("Maior numero %.2f"%n3)
    
    