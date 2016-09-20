minutos = int(input("Digite os minutos: "))

if minutos < 200:
    valor = minutos * 0.20
elif minutos <= 400:
    valor = minutos * 0.18
elif(minutos <= 800):
    valor = minutos * 0.15
else:
    valor = minutos * 0.08            

print ("Valor da conta é %.2f reais"%valor)