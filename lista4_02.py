# 2) Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
# o número de vezes que cada número ocorre na sequência.

def funcao(lista1):
    dicio = {}
    for valor in lista1:
        if str(valor) in list(dicio.keys()):
            dicio[str(valor)] = int(dicio[str(valor)]) + 1
        else:
            dicio[str(valor)] = 1
    return dicio


print(funcao([5, 4, 5, 7, 3, 4]))
print(funcao([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]))

