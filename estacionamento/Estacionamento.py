import random
from Catraca import Catraca
import Operacoes

# Classe Estacionamento
class Estacionamento:

    #Construtor que recebe a lista de catracas e o identificador do estacionamento
    def __init__(self, catracas, id):
        self.catracas = catracas
        self.id = id

    def __str__(self):
        return f'Estacionamento numero #{self.id}'




