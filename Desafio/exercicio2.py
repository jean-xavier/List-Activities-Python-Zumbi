'''
Conversor de decimal para romano. Você deverá programar um algoritmo em Python que traduza um número 
lido no sistema arábico para romano. Evite fazer muitos “ifs”. A idéia é usar um comando while para 
analisar cada casa decimal e gerar os caracteres romanos diferentemente para cada iteração. Exemplo 
2011 = MMXI em romano. Não precisa testar até o infinito, basta de 1 até 2013.
'''

num_arabico = int(input("Digite um numero: "))

romanos = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
arabicos = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

contador = len(romanos)
new_num_romans = ''

while contador != 0:
    contador -= 1
    while num_arabico >= arabicos[contador]:
        new_num_romans += romanos[contador]
        num_arabico -= arabicos[contador]

print (new_num_romans)