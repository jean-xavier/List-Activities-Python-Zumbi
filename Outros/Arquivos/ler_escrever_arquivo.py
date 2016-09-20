frase = input("Digite uma mensagem: ")

arquivo = open('mensagem.txt', 'w')
arquivo.write('%s'%frase)
arquivo.close()

# arquivo = open('mensagem.txt','r')
# cripton = arquivo.read()
# arquivo.close()

with open('mensagem.txt') as mensagem:
    frase = mensagem.read()

cripton = ''

for letra in frase:
    if letra.lower() in 'aeiou':
        cripton = cripton + '*'
    else:
        cripton = cripton + letra


arquivo = open('cripton.txt', 'w')
arquivo.write('%s'%cripton)
arquivo.close()

with open('cripton.txt') as mensagem:
    cripton = mensagem.read()

print(cripton)