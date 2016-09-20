data = input("Digite uma data: ")

meses = ["janeiro","fevereiro","março","abril", "maio","junho","julho","agosto", "setembro","outubro","novembro","dezembro"]

data = data.split("/")
data[1] = int(data[1])

data = data[0] + " de " + meses[data[1] - 1] + " de " + data[2]

print(data)
