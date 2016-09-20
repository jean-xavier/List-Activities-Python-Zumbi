''' Questão A (Vestibular FATEC 2008). Uma escola do Ensino Fundamental ofereceu a alguns de seus alunos
um passeio ao zoológico. Para tanto, a escola pretende gastar EXATAMENTE 93 reais e sabe que o ingresso
do zoológico custa 5 reais para os menores de 12 anos e 7 reais os que têm 12 anos ou mais. Elabore um
algoritmo que retorne o número máximo de alunos que a escola pode levar ao zoológico considerando todos
os valores como inteiros. O seu programa deve ter uma abordagem genérica e não levar em conta
peculiaridades nos dados fornecidos.'''

for i in range(20):
	for j in range(20):
		if (i * 5) + (j * 7) == 93:
			print("%d aluno(s) menores de 12 anos" %i)
			print("%d aluno(s) com 12 anos ou mais" %j)
			print("--------------------------------")



