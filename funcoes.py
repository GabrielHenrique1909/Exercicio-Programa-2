from random import randint

def rolar_dados(n):
    lista = []
    for i in range(n):
        lista.append(randint(1,6))
    return lista
