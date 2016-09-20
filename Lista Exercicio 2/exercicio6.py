'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$ 
'''

valor_hora = float(input("Digite quanto você ganha por hora: "))
quant_hrs_mes = int(input("Digite quantas horas você trabalha no mês: "))

salario_bruto = valor_hora * quant_hrs_mes
imposto = salario_bruto * 0.11 
INSS = salario_bruto * 0.08 
sindicato = salario_bruto * 0.05 
salario_liquido = salario_bruto - imposto - INSS - sindicato

print("Salário Bruto : R${}".format(salario_bruto))
print("IR (11%) : R${}".format(imposto) )
print("INSS (8%) : R${}".format(INSS))
print("Sindicato ( 5%) : R${}".format(sindicato))
print("Salário Liquido : R${}".format(salario_liquido)) 