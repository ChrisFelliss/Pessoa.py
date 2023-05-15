# 8) Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor
# mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5

def funcao(lista):
    diferenca = 99999999999999
    valor_prox = 0
    for valor in lista:
        media = sum(lista)/len(lista)
        calculo = media - valor
        if calculo < 0:
            calculo = calculo * (-1)
        if calculo < diferenca:
            diferenca = calculo
            valor_prox = valor

    print(valor_prox)




print(funcao([2.5, 7.5, 10.0, 4.0]))


