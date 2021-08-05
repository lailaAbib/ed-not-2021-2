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