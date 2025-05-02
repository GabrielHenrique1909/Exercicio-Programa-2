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

def remover_dado(dadosrolados, dadosguardados, dadopararemover):
    for i in range(len(dadosguardados)):
        if i == dadopararemover:
            dadosrolados.append(dadosguardados[i])
            del dadosguardados[i]
    return [dadosrolados, dadosguardados]

def calcula_pontos_regra_simples(dados):
    pontcategorias = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for dado in dados:
        pontcategorias[dado]+=dado
    return pontcategorias

def calcula_pontos_soma(dados):
    soma = 0
    for dado in dados:
        soma += dado
    return soma

gvjkgv igi 
 