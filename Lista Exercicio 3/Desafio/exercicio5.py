# Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321

num =  int(input("Digite um numero inteiro de até 4 digitos: "))

milhar = 0
centena = 0
dezena = 0

while num >= 1000:
    milhar = milhar + 1
    num = num - 1000

while num >= 100:
    centena = centena + 1
    num = num - 100

while num >= 10:
    dezena = dezena + 1
    num = num - 10

if milhar == 0 and centena != 0:
    print("%i%i%i"%(num,dezena,centena))
elif centena == 0 and dezena != 0:
    print("%i%i"%(num,dezena))
else:
    print("%i%i%i%i"%(num,dezena,centena,milhar))
