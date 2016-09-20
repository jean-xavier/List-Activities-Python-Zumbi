# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
# seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
# faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na
# variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais
# variáveis com o conteúdo ZERO.

peso_peixes = float(input("Digite o peso da mercadoria: "))
peso_extra = 0
multa = 0

if peso_peixes > 50:
    peso_extra = peso_peixes - 50
    multa = peso_extra * 4.00
    print("Peso extra %.2f quilo(s). Multa a pagar: %.2f real(s)"%(peso_extra, multa))
else:
    print("Peso extra %.2f quilo(s). Multa a pagar: %.2f real(s)"%(peso_extra, multa))
    
