from funcoes import *

combinacoespossiveis = ["1","2","3","4","5","6","sem_combinacao",'quadra','full_house',"sequencia_baixa","sequencia_alta","cinco_iguais"]
indicespossiveis = [0,1,2,3,4]
disponibilidade = {}
for comb in combinacoespossiveis:
    disponibilidade[comb]=True    
cartela_de_pontos = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela_de_pontos)

dadosrolados = rolar_dados(5)
dadosguardados = []
print(f"Dados rolados: {dadosrolados}")
print(f"Dados guardados: {dadosguardados}")
print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
entrada = input(">")
contagemjogos=1
while contagemjogos <13:
    contagemrerolagem=1
    while entrada != "0":
        while entrada not in "01234":
            print('Opção inválida. Tente novamente.')
            entrada = input(">")
        if entrada == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input(">"))
            while indice not in indicespossiveis:
                print('Opção inválida. Tente novamente.')
                indice = int(input(">"))
            roladoeguardado = guardar_dado(dadosrolados, dadosguardados, indice)
            dadosrolados = roladoeguardado[0]
            dadosguardados = roladoeguardado[1]    
        if entrada == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input(">"))
            while indice not in indicespossiveis:
                print('Opção inválida. Tente novamente.')
                indice = int(input(">"))
            roladoeguardado = remover_dado(dadosrolados, dadosguardados, indice)
            dadosrolados = roladoeguardado[0]
            dadosguardados = roladoeguardado[1]
        if entrada == "3":
            if contagemrerolagem >= 3:
                print('Você já usou todas as rerrolagens.')
            else:
                dadosrolados = rolar_dados(len(dadosrolados))
            contagemrerolagem+=1    
        if entrada == "4":
            imprime_cartela(cartela_de_pontos)    
        print(f"Dados rolados: {dadosrolados}")
        print(f"Dados guardados: {dadosguardados}")
        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
        entrada = input(">")    
    print('Digite a combinação desejada:')
    dados = dadosrolados + dadosguardados
    combinacao = input(">")    
    while combinacao not in combinacoespossiveis:
        print("Combinação inválida. Tente novamente.")
        combinacao = input(">")    
    while disponibilidade[combinacao]!=True:
        print('Essa combinação já foi utilizada.') 
        combinacao = input(">")
        while combinacao not in combinacoespossiveis:
            print("Combinação inválida. Tente novamente.")
            combinacao = input(">")    
    disponibilidade[combinacao]=False    
    cartela_de_pontos = faz_jogada(dados, combinacao, cartela_de_pontos)
    contagemjogos += 1
    if contagemjogos==13:
        break
    dadosrolados = rolar_dados(5)
    dadosguardados = []
    print(f"Dados rolados: {dadosrolados}")
    print(f"Dados guardados: {dadosguardados}")
    print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
    entrada = input(">")

pontuacaofinal = 0
pontsimples = 0

valoressimples = cartela_de_pontos["regra_simples"]
for val in valoressimples.values():
    pontsimples+=val

if pontsimples >= 63:
    bonus = 35
else:
    bonus = 0    

for dics in cartela_de_pontos.values():
    for pontuações in dics.values():
        pontuacaofinal+=pontuações

imprime_cartela(cartela_de_pontos)
print(f"Pontuação total: {pontuacaofinal+bonus}")