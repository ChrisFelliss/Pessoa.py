# 5) Escreva uma função que recebe uma lista com n números inteiros, e retorna uma
# lista com a soma cumulativa dos elementos da lista original onde o i-ésimo
# elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] =
# [1,3,6]

def funcao(lista):
    lista2 = []
    for indice in range(len(lista)):
        lista2.append(sum(lista[0:indice+1]))
    return lista2


print(funcao([2, 4, 6]))

