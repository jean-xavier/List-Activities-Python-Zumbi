dias = int(input("Digite os dias\n"))
horas = int(input("Digite as horas\n"))
minutos = int(input("Digite os minutos\n"))
segundos = int(input("Digite o segundos\n"))

total = (minutos * 60) + (horas * minutos * 60) + (dias * minutos * 24) + segundos

print("Total de segundo %f"%(total))