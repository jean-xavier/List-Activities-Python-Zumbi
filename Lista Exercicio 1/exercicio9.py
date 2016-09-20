# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

distancia_pecorrida = float(input("Digite a distancia percorrida: "))
dias_alugado = int(input("Digite quantos dias o carro foi alugado: "))

valor_distancia_pecorrida = distancia_pecorrida * 0.15
valor_dias_alugado = dias_alugado * 60

valor_total = valor_dias_alugado + valor_distancia_pecorrida

print("Valor a pagar: %.2f"%(valor_total))