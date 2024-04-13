# d.1 imprimir os objetos (estacionamentos)

# Complexidade O(N) seguindo a notação Big-O

# O tempo de execução deste algoritmo cresce linearmente com o tamanho da entrada.
# Ou seja, para cada elemento adicional na lista de objetos, o tempo de execução 
# aumenta uma quantidade constante.

# As consequências para entradas grandes podem ser significativas. O tempo de
# execução extremamente longo, o alto consumo de memória e o impacto negativo
# na experiência do usuário exigem cuidado na escolha e implementação desse tipo de algoritmo.

# :param objetos

def imprimir_objetos(objetos):
    for objeto in objetos:
        print(objeto)

# d.2 imprimir as leituras dos sensores para os objetos (leituras das catracas dos estacionamentos)

# Complexidade O(N^2) seguindo a notação Big-O

# O tempo de execução deste algoritmo cresce quadraticamente com o número total de
# catracas em todos os estacionamentos. Essa complexidade é considerada menos boa
# em termos de desempenho do que O(N) ou O(log N), pois o crescimento do tempo de
# execução é proporcional ao quadrado do tamanho da entrada.

# As consequências para entradas grandes neste caso são mais perigoras. O tempo de
# execução vai aumentar na proporção quadrática do tamanho da entrada. Ou seja,
# Uma inserção aqui levará o quadrado do tempo de execução de um algoritmo
# com complexidade O(N)

# :param objetos

def imprimir_leituras(objetos):
    for estacionamento in objetos:
        print()
        print(f'Estacionamento numero #{objetos.index(estacionamento) + 1}')
        print('Catracas:')
        for catraca in estacionamento.catracas:
            print()
            print(f'Catraca numero #{estacionamento.catracas.index(catraca) + 1}')
            print(catraca)


# METODO EXTRA PARA IMPRESSAO DE CATRACAS ORDENADAS

def imprimir_leituras_ordenadas(objetos):
    for estacionamento in objetos:
        print()
        print(f'Estacionamento numero #{objetos.index(estacionamento) + 1}')
        print('Catracas:')
        ordenar_por_vagas_disponiveis(estacionamento.catracas)
        for catraca in estacionamento.catracas:
            print()
            print(f'Catraca numero #{estacionamento.catracas.index(catraca) + 1}')
            print(catraca)



# d.3 ordenar as catracas em ordem crescente pelos seus valores de vagas disponiveis

# Complexidade O(N^2) seguindo a notação Big-O

# O tempo de execução deste algoritmo cresce quadraticamente com o número total de
# catracas em todos os estacionamentos. Essa complexidade é considerada menos boa
# em termos de desempenho do que O(N) ou O(log N), pois o crescimento do tempo de
# execução é proporcional ao quadrado do tamanho da entrada.

# As consequências para entradas grandes neste caso são mais perigoras. O tempo de
# execução vai aumentar na proporção quadrática do tamanho da entrada. Ou seja,
# Uma inserção aqui levará o quadrado do tempo de execução de um algoritmo
# com complexidade O(N)

# :param catracas

def ordenar_por_vagas_disponiveis(catracas):
    n = len(catracas)
    for i in range(n):
        for j in range(0, n-i-1):
            if catracas[j].vagas_disponiveis() > catracas[j+1].vagas_disponiveis():
                catracas[j], catracas[j+1] = catracas[j+1], catracas[j]


# d.4 calcular o número total de combinações possíveis de catracas em todos os estacionamentos
# Complexidade O(2^N) seguindo a notação Big-O

# As consequências de um algoritmo com complexidade O(2^N) podem ser extremamente severas, 
# tornando-o impraticável para a maioria das aplicações reais. O tempo de execução
# desse tipo de algoritmo cresce exponencialmente com o tamanho da entrada (N), o
# que significa que um pequeno aumento no tamanho da entrada pode levar a um aumento
# descomunal no tempo necessário para finalizar a execução.

# Este algoritmo pode levar a necessidade de brute force em alguns casos, 
# especialmente quando a quantidade de catracas e/ou estacionamentos for grande.

# :param estacionamentos

def calcular_combinacoes_catracas(estacionamentos, estacionamento_atual=0, catracas_atual=0):
    if estacionamento_atual == len(estacionamentos):
        return 2 ** catracas_atual
    
    com_catraca = calcular_combinacoes_catracas(estacionamentos, estacionamento_atual + 1, catracas_atual + len(estacionamentos[estacionamento_atual].catracas))
    sem_catraca = calcular_combinacoes_catracas(estacionamentos, estacionamento_atual + 1, catracas_atual)
    
    return com_catraca + sem_catraca


