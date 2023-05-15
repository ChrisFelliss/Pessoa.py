# 4) Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de qualquer seguimento da lista. Ex: Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9,
# -6, 4, 1] = 34

def funcao(lista):
    if len(lista) == 0:
        return Exception
    maior_soma = 0
    for indice_i in range(0, len(lista)):
        for indice_j in range(0, len(lista)):
            if type(lista[indice_j]) != int:
                return Exception
            if maior_soma < sum(lista[indice_i:indice_j+1]):
                print(sum(lista[indice_i:indice_j+1]))
                maior_soma = sum(lista[indice_i:indice_j+1])
    return maior_soma


assert funcao([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]) == 34
assert funcao([13, -22, 11, 21, 11, 9, -18, 5, -2, 7, -19, 16, 18, -28, 1]) == 59
assert funcao([-24, 19, -7, -20, 7, 18, 11, 20, -30, 16, -22, 0, -27, 3, -8]) == 56
assert funcao([-5, -3, -30, 9, 3, -20, 27, -25, 16, 1, 24, -22, 12, -24, -21]) == 43
assert funcao([2, 5, 'm', 5, -2, 9, -6, -3]) == Exception
assert funcao([]) == Exception



