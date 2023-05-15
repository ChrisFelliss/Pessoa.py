# 9) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando todas as ocorrências de valores repetidos. Ex: [5, 4, 5, 7, 3, 4] =
# [7, 3]

def funcao(lista):
    lista2 = []
    dicio = {}
    for valor in lista:
        if str(valor) in list(dicio.keys()):
            dicio[str(valor)] = int(dicio[str(valor)]) + 1
        else:
            dicio[str(valor)] = 1
    for key in dicio.keys():
        if dicio[key] == 1:
            lista2.append(int(key))
    return lista2





print(funcao([5, 4, 5, 7, 3, 4]))


