# Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras
# “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
# minúsculas e de remover antes os caracteres especiais.

texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.”'''

lista = texto.split()
cont_palavras = 0

for palavra in lista:
    if len(palavra) > 4:
        for letra in "python":
            if letra.lower() in palavra:
                cont_palavras = cont_palavras + 1 
                break   

print (cont_palavras)