forma1 = {
    "base": ,
    "altura": ,
    "tipo":
}
forma2 = {
    "base": ,
    "altura": ,
    "tipo":
}
forma3 = {
    "base": ,
    "altura": ,
    "tipo":
}
forma4 = {
    "base": 10,
    "altura": 5,
    "tipo": "W" # tipo não reconhecido
}

forma5 = {
    "legume": "batata",
    "fruta": "abacate",
    "tipo": "T"
}
from math import pi

def calcular_area(forma):
    if forma["tipo"] == "R": #Retâgulo
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T": #Triângulo
        return forma["base"] * forma["altura / 2"]
    elif forma["tipo"] == "E": # Elipse
        return forma["base"] / 2 * forma["altura"] / 2 * pi
    else:
        # Gera um erro
        raise Exception("Tipo de forma não reconhecido.")

print(f"Área de um Retângulo de 7.5x12: {calcular_area(forma1)}")
print(f"Área de um Triângulo de 6x2.5: {calcular_area(forma2)}")
print(f"Área de uma Elipse de 5x3: {calcular_area(forma3)}")
#print(f"Área de uma forma Desconhecida de 10x5: {calcular_area(forma4)}")
print(f"Área de uma forma Desconhecida de ?x?: {calcular_area(forma5)}")