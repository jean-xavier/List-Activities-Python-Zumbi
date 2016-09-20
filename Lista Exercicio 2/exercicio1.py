lado_a = float(input("Digite o valor do lado A: "))
lado_b = float(input("Digite o valor do lado B: "))
lado_c = float(input("Digite o valor do lado C: "))

if lado_a == lado_b and lado_b == lado_c:
    print("Equilátero")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("Isósceles")
else:
    print("Escaleno")