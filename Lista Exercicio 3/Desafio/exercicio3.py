# Verifique se um inteiro positivo n é primo.

primo = int(input("Digite um numero pra verificar ser é primo: "))
cont = 1
valid_primo = 0

while cont <= primo:
    if(primo % cont == 0):
        valid_primo = valid_primo + 1    
    cont = cont + 1

if valid_primo == 2:
    print("Primo")
else:
    print("Não é primo")        

