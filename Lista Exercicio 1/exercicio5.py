preco = float(input("Digite o preco: "))
porcent_desconto = float(input("Digite o desconto: "))

desconto = preco * porcent_desconto / 100;

print("O senhor(a) vai ter o desconto de %.2f reais"%(desconto))
print("Novo valor %.2f reais"%(preco - desconto))

print 