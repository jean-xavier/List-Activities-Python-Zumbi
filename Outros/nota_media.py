notas = []
cont = 0
soma = 0
while cont < 4:
    nota = float(input("Digite a %i notas: " %(cont+1)))
    soma = soma + nota
    notas.append(nota)
    cont = cont + 1

print("Notas: ",notas)
print ("Media: ",soma/cont)