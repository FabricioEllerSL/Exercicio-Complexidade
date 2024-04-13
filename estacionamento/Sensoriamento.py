import random


# Gerador de quantidade de entradas e saidas para as catracas
# Complexidade O(N) seguindo a notação Big-O
def gerar_entrada_saida(qtd_dados):
    entrada_saida = []

    for i in range(0, qtd_dados):
        entrada = random.randint(0, 100)
        saida = random.randint(0, entrada)
        entrada_saida.append({'entrada': entrada, 'saida': saida})

    # retorna uma lista de dicionarios (estrutura chave-valor) com as entradas e saidas
    return entrada_saida


