import random

def Embaralhar(string):
    string = list(string)
    random.shuffle(string)
    return ''.join(string)

print(Embaralhar('absfhhjudsjsdkgj'))