from Catraca import Catraca
from Estacionamento import Estacionamento
from Sensoriamento import gerar_entrada_saida
from Operacoes import imprimir_leituras_ordenadas, imprimir_objetos
from Operacoes import imprimir_leituras
from Operacoes import ordenar_por_vagas_disponiveis
from Operacoes import calcular_combinacoes_catracas


total_estacionamentos = 10
catracas_por_estacionamento = 10

estacionamentos = []


# Gerando os estacionamentos solicitados
# Complexidade O(N^3) seguindo a notação Big-O
for i in range(total_estacionamentos):
    catracas = []
    for j in range(catracas_por_estacionamento):
        entradas_saidas = gerar_entrada_saida(1)
        catraca = Catraca(entradas_saidas[0]['entrada'], entradas_saidas[0]['saida'])
        catracas.append(catraca)
    
    estacionamento = Estacionamento(catracas, i+1)
    estacionamentos.append(estacionamento)


# d.1 imprimindo os estacionamentos

print('--------------------------ESTACIONAMENTOS--------------------------------------------------')

imprimir_objetos(estacionamentos)


# d.2 imprimindo as catracas dos estacionamentos

print('----------------------------CATRACAS POR ESTACIONAMENTO------------------------------------')

imprimir_leituras(estacionamentos)



# d.3 ordenando as catracas em ordem crescente pelos seus valores de vagas disponiveis

print('-------------------------CATRACAS ORDENADAS------------------------------------------------')

ordenar_por_vagas_disponiveis(catracas)
imprimir_leituras_ordenadas(estacionamentos)


# d.4 calcular as combinações possiveis de catracas

print('---------------------------COMBINÇÕES POSSIVEIS DE CATRACAS-------------------------------------')

print(f'É possivel fazer um total de {calcular_combinacoes_catracas(estacionamentos)} combinações coom estas catracas')

print('------------------------------------------------------------------------------------------------')

