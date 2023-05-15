# 7) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
# caso algum elemento apareça mais de uma vez ou False caso nenhum elemento
# apareça mais de uma vez. Ex [1, 2, 3, 1] = True. Ex. [3, 7, 2, 4] = False

def funcao(lista1):
    dicio = {}
    for i in lista1:
        if str(i) in list(dicio.keys()):
            return True
        else:
            dicio[str(i)] = 1
    return False

print(funcao([3, 7, 2, 4]))

