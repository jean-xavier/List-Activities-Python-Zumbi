# A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
# formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
# soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
# de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.

n1 = 1
n2 = 1
n3 = 1

num = int(input("Digite um numero inteiro: "))

print(n3)

while n3 < num:
    print(n3)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
