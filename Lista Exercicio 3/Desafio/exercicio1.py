# Dizemos que um número natural é triangular se ele é produto de três números naturais
# consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n,
# verificar se n é triangular.

num = int(input("Digite um numero inteiro: "))
i = 0
while i < num:
    if i * (i+1) * (i+2) == num:
        print(num,"é triangular pois ele é produto dos três numeros:",i , i+1, i+2) 
    i = i + 1