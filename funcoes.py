from random import randint

def rolar_dados(n):
    lista = []
    for i in range(n):
        lista.append(randint(1,6))
    return lista

def guardar_dado(dadosrolados, dadosguardados, dadoparaguardar):
    for i in range(len(dadosrolados)):
        if i == dadoparaguardar:
            dadosguardados.append(dadosrolados[i])
            del dadosrolados[i]
    return [dadosrolados,dadosguardados]        
