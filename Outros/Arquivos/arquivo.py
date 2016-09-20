# arquivo = open('números.txt', 'w')
#
# for linha in range(1, 101):
#     arquivo.write('%d\n'%linha)
# arquivo.close()

# arquivo = open('números.txt', 'r')

# for linha in arquivo.readlines():
#     print(linha.rstrip())
# arquivo.close()

with open('números.txt') as f:
    print(f.read())