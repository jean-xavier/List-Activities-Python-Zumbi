# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
# anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
# crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
# necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento

pais_a = 8000
pais_b = 20000
anos = 0

while pais_a <= pais_b:
    pais_a = pais_a + (pais_a * 3 / 100)
    pais_b = pais_b + (pais_b * 1.5 / 100)
    anos = anos + 1

print (pais_a)
print (pais_b)
print (anos)