# Classe é uma estrutura que representa conjuntamente dados e algoritmos.
# A classe é como uma forma de bolo com a qual podemos criar diferentes
# "bolos" (objetos).
# Cada "bolo" (objeto) pode ser feito com seus própios ingredientes(dados) 
# e modo de fazer (algoritmos), mas terão sempre o formato pela "forma" (classe).

class FormaGeometrica():

    #Dados
    # Quando pertece uma classe, ganham o nome
    # de ATRIBUTOS
    base = 0
    altura = 0
    tipo = "R" # Retângulo

    # Algoritmos
    # São representados por funções que, quando se encontram
    # dentro de uma classe, ganham o nome de MÉTODOS

    # Este método é executado quando um objeto é criado a partir
    # de uma classe
    def __init__(self, base = 0, altura = 0, tipo = "R"):
        # Recebe os valores passados ao construtor e os armazena
        # dentro dos atributos
        self.base = base
        self.altura = altura
        self.tipo = tipo

###################################################################

# Criando objetos a partir da classe

retangulo1 = FormaGeometrica(15, 10, "R")

print(f"[retangulo1] base: {retangulo1.base}, altura: {retangulo1.altura}, tipo: {retangulo1.tipo}")
