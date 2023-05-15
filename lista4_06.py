# 6) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
# caso a lista esteja ordenada em ordem ascendente ou False caso não esteja
# ordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = False

def funcao(lista):
    num = 0
    for valor in lista:
        if valor > num:
            num = valor
        else:
            return False
    return True


print(funcao([1, 5, 7]))

