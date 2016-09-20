salario = float(input("Digite o salario: "))
porcent_aument = float(input("Digite a porcentagem de aumento: "))

novo_salario = salario + ((salario * porcent_aument) / 100)

print ("Novo salario %.2f reais"%(novo_salario))