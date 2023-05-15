# 10)Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma dos números que se repetem da lista. Ex: [5, -2, -2, 5, 3, 5, 10, -2, 3,
# 10, 3, 1] = 20

def funcao(lista):
    dicio = {}
    maior_soma = 0
    for valor in lista:
        if str(valor) in list(dicio.keys()):
            dicio[str(valor)] = int(dicio[str(valor)]) + 1
        else:
            dicio[str(valor)] = 1
    for key in dicio.keys():
        operacao = int(key) * dicio[key]
        if operacao > maior_soma:
            maior_soma = operacao
    return maior_soma


print(funcao([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]))


