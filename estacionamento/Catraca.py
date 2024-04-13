
# Classe Catraca
class Catraca:

    # Quantidade total de vagas padrão que a catraca monitora
    qtd_vagas = 100

    # Construtor que recebe a quantidade de entradas e a quantidade de saidas
    def __init__(self, qtd_entrada, qtd_saida):
        self.qtd_entrada = qtd_entrada
        self.qtd_saida = qtd_saida

    # Método que retorna a quantidade de vagas disponíveis
    def vagas_disponiveis(self):
        return self.qtd_vagas - (self.qtd_entrada - self.qtd_saida)
    
    def vagas_ocupadas(self):
        return self.qtd_vagas - self.vagas_disponiveis()
    
    def __str__(self):
        return f'Entradas: {self.qtd_entrada}\n Saidas: {self.qtd_saida}\n Vagas disponíveis: {self.vagas_disponiveis()}\n Vagas ocupadas: {self.vagas_ocupadas()}'
    



