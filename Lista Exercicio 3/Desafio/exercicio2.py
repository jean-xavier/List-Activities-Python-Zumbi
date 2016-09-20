# Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
# algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
# os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
# nenhuma delas esteja em falta no caixa.

valor_pagamento = float(input("Digite o valor a ser pago: "))
troco = valor_pagamento

print("O troco com menos notas para R$%.2f" % valor_pagamento)

if troco >= 50:
    notas = troco - troco % 50
    troco = troco % 50
    print("%i nota(s) de 50 reais"%(notas/50))

if troco >= 20:
    notas = troco - troco % 20
    troco = troco % 20
    print("%i nota(s) de 20 reais"%(notas/20))

if troco >= 10:
    notas = troco - troco % 10 
    troco = troco % 10 
    print("%i nota(s) de 10 reais"%(notas/10))

if troco >= 5:
    notas = troco - troco % 5
    troco = troco % 5     
    print("%i nota(s) de 5 reais"%(notas/5))

if(troco > 1):
    print (troco," reais")
elif troco == 1:
    print (troco," real")

