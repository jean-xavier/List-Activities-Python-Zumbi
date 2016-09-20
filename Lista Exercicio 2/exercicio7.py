'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
'''

metros = float(input("Digite o tamanho em metros: "))

quant_litros = metros / 3
quant_latas = 0

while quant_litros > 0:
    if quant_litros < 18:
        quant_litros = 0
    else:
        quant_litros = quant_litros - 18
    quant_latas = quant_latas + 1

print("Será necessario %d latas de 18 litros de tinta, sendo que ira custar R$%d reais" %(quant_latas,quant_latas*18))

