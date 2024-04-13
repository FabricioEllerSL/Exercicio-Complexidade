from Catraca import Catraca
from Estacionamento import Estacionamento

def ordenar_por_vagas_disponiveis(catracas):
    n = len(catracas)
    for i in range(n):
        for j in range(0, n-i-1):
            if catracas[j].vagas_disponiveis() > catracas[j+1].vagas_disponiveis():
                catracas[j], catracas[j+1] = catracas[j+1], catracas[j]

    return [str(catraca) for catraca in catracas]

        