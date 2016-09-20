# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
# quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
# perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
# total de dias.

quant_cigarros = int(input("Digite quantos cigarros por dia você fuma: "))
quant_anos = int(input("Digite há quantos anos você fuma: "))

minutos_perdido = (quant_anos * 365) * 10

print (minutos_perdido / 60)

dias_perdido = minutos_perdido / 24

print("Dias perdidos:  %d"%(dias_perdido))
