def ler_gramatica():
    with open('grammar.txt', 'r') as gramatica:
        regras = gramatica.read().splitlines()
        terminais = []
        variaveis = []

        for linha in regras:
            lado_esquerdo, lado_direito = linha.split(" => ")
            lado_direito = lado_direito.split(" | ")

            for letra in lado_direito:
                if(str.islower(letra)):
                    terminais.append([lado_esquerdo, letra])
                else:
                    variaveis.append([lado_esquerdo, letra])

        return variaveis, terminais


def cyk(variaveis, terminais, entrada):
    tamanho_entrada = len(entrada)

    variaveis_esquerda = [var[0] for var in variaveis]
    variaveis_direita = [var[1] for var in variaveis]

    tabela = [[set() for _ in range(tamanho_entrada-i)] for i in range(tamanho_entrada)]

    for i in range(tamanho_entrada):
        for variavel, terminal in terminais:
            if entrada[i] == terminal:
                tabela[0][i].add(variavel)

    for linha_atual in range(1, tamanho_entrada):
        for coluna_atual in range(tamanho_entrada - linha_atual):
            for k in range(linha_atual):
                if (tabela[k][coluna_atual] and tabela[linha_atual-1 -k][coluna_atual+1 +k]): 
                    combinacoes = set() # set() = lista que não repete valores
                    for variavel1 in tabela[k][coluna_atual]: 
                        for variavel2 in tabela[linha_atual-1 -k][coluna_atual+1 +k]: 
                            combinacoes.add(variavel1 + variavel2) 
                            
                    for combinacao in combinacoes:
                        if combinacao in variaveis_direita:
                            tabela[linha_atual][coluna_atual].add(
                                variaveis_esquerda[variaveis_direita.index(combinacao)])
                            
    if ('S') in tabela[len(entrada)-1][0]: 
        print(entrada, "pertence a gramática")
    else:
        print(entrada, "não pertence a gramática")
    return tabela



variaveis, terminais = ler_gramatica()
palavra = input("Escreva uma palavra:\n")
teste = cyk(variaveis, terminais, palavra)