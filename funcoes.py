
from math import pi
# Função é um preço de código que tem um nome e pode receber informações
# externas para fazer o seu trabalho. Opcionalmente, uma função pode também
# produzir um valor de resultado.
# Uma função é definida apenas uma vez e pode ser utilizada
# (chamada) várias vezes, evitando repetições de código.
# Existem funções já providas pela linguagem, como, por exemplo.
# len(), range() , e sort(), e podemos definir também nossas próprias
# funções.

def imc(peso, altura):
    """
    Função que calcula índice de Massa corpórea(IMC)
    """
    return peso / altura ** 2 #peso/ (altura)²

p = float(input('Informe o peso da pessoa: '))
a = float(input('Informe a altura da pessoa: '))

# Fazendo uma chamada de função imc()
resultado = imc(p, a)


print(f"O IMC calculado é {resultado}.")

print('------------------------------------')

def area_forma(base, altura, forma = "R"):
    area = 0
    if forma == "R": # Retângulo
        area = base * altura
    elif forma == "T":  # Triângulo
        area = base * altura / 2
    elif forma == "E": # Elipse
        area = (base / 2) * (altura / 2) * pi
    return area

print('------------------------------------')

print(f"Retângulo 7.5x11: {area_forma(7.5, 11, 'R')}")
print(f"Triângulo 78x12: {area_forma(8, 12, 'T')}")
print(f"Circulo 15x15: {area_forma(15, 15, 'E')}")
print(f"Quadrado 9.5x9.5: {area_forma(9.5, 9.5)}")


