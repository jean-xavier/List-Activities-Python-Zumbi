ano = int(input("Digite o ano: "))

if ano % 4 == 0 or ano % 400 == 0:
    print("É")
elif ano % 100 == 0:
    print("Não é")
    
        