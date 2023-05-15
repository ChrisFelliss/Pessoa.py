# 3) Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
# 4, 1] = 25

def funcao(lista1):
    lista2 = []
    maior_1 = 0.1, 0.1
    for i in range(2):
        try:
            maior_1 = lista2[0]
        except:
            pass
        maior = (lista1[0], 0)
        for indice, valor in enumerate(lista1):
            if maior[0] < valor != maior_1[0] and maior[1] != indice != maior_1[1]:
                maior = valor, indice
        lista2.append(maior)
    return lista2[0][0] + lista2[1][0]


print(funcao([5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]))

