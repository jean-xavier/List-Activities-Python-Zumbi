velocidade = int(input("Digite a velocidade do carro: "))

if(velocidade > 110):
    valor_multa = (velocidade - 100) * 5.0
    print ("Você ultrapassou %i km do limite de velocidade"%(velocidade))
    print ("Vai pagar como multa 5.0 reais por está acima da velocidade, total a pagar: ",valor_multa)
else:
    print("Abaixo do limite maximo")