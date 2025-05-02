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

def calcula_pontos_sequencia_baixa(dados):   
    dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for dado in dados:
        dic[dado]+= 1
    if dic[1]>0 and dic[2]>0 and dic[3]>0 and dic[4]>0 or dic[2]>0 and dic[3]>0 and dic[4]>0 and dic[5]>0 or dic[3]>0 and dic[4]>0 and dic[5]>0 and dic[6]>0:
        return 15
    else:
        return 0

def calcula_pontos_sequencia_alta(dados):
    dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for dado in dados:
        dic[dado]+= 1
    if dic[1]>0 and dic[2]>0 and dic[3]>0 and dic[4]>0 and dic[5]>0 or dic[2]>0 and dic[3]>0 and dic[4]>0 and dic[5]>0 and dic[6]>0:
        return 30
    else: 
        return 0
    
def calcula_pontos_full_house(dados):
    dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    s = 0
    for dado in dados:
        dic[dado]+= 1
        s += dado
    if 2 in dic.values() and 3 in dic.values():
        return s
    else: 
        return 0

def calcula_pontos_quadra(dados):
    dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    s = 0
    for dado in dados:
        dic[dado]+= 1
        s += dado
    for chave in dic.keys():
        if dic[chave]>3:
            return s
    return 0

def calcula_pontos_quina(dados):
    dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for dado in dados:
        dic[dado]+= 1
    for chave in dic.keys():
        if dic[chave]>4:
            return 50
    return 0

def calcula_pontos_regra_avancada(dados):
    r = {}
    r['cinco_iguais'] = calcula_pontos_quina(dados)
    r['full_house'] = calcula_pontos_full_house(dados)
    r['quadra'] = calcula_pontos_quadra(dados)
    r['sem_combinacao'] = calcula_pontos_soma(dados)
    r['sequencia_alta'] = calcula_pontos_sequencia_alta(dados)
    r['sequencia_baixa'] = calcula_pontos_sequencia_baixa(dados)
    return  r

def faz_jogada(dados, categoria, cartela_de_pontos):
    s = calcula_pontos_regra_simples(dados)
    a = calcula_pontos_regra_avancada(dados)
    for chave in cartela_de_pontos['regra_simples']:
        if str(chave) == categoria:
            cartela_de_pontos['regra_simples'][chave] = s[chave]
    for chave in cartela_de_pontos['regra_avancada']:
        if chave == categoria:
            cartela_de_pontos['regra_avancada'][categoria] = a[categoria]
    return cartela_de_pontos

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)
    