# 1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]

def funcao(lista1):
    lista2 = []
    for valor in lista1:
        if valor not in lista2:
            lista2.append(valor)
    return lista2

print(funcao([5, 4, 5, 7, 3, 4]))

