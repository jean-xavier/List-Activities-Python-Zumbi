'''
(Enade 2011) No livro “O Homem que Calculava”, de Malba Tahan, um personagem desejava
ganhar os grãos de trigos que fossem distribuídos sobre um tabuleiro de xadrez do seguinte modo: um
grão na primeira casa do tabuleiro, o dobro (2) na segunda, novamente o dobro (4) na terceira, outra vez o
dobro (8) na quarta, e assim por diante, até a sexagésima quarta casa do tabuleiro. Faça um algoritmo que
calcule a quantidade total de grãos de trigos necessários para realizar esta distribuição
'''

acumulador = 1
total = acumulador

for i in range(60):
	print('%d na casa %d do tabuleiro'%(acumulador, i + 1))
	acumulador *= 2
	total += acumulador

print("Total de grãos necessarios %d" %total)