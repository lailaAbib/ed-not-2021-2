from time import time
from data.lista_nomes import nomes

comps = 0   # Declarando uma varíavel global

# ALGORITMO DE BUSCA BINARIA

# Dada uma lista que deve estar PREVIAMENTE ORDENADA, e um valor de
# busca, divide a lista em duas metades e procura pelo valor de busca
# apenas na metade aonde o valor poderia estar. Novas subdivisões são
# feitas até que se encontre o valor de busca ou que reste apenas uma
# sublista vazia, quando se conclui que o valor de busca não existe na
# lista.

def busca_binaria(lista, valor_busca):

    global comps #indica que estamos usando uma variavel declarada na linha 13
    comps = 0

    ini = 0                 # Primeira posição
    fim = len(lista) - 1    # Última posição

    while ini <= fim:
        meio = (ini + fim) // 2  # Operador // é divisão inteira

        # 1 º caso: lista[meio] é igual a valor_busca
        if lista[meio] == valor_busca: # ENCONTROU!!
            comps += 1
            return meio         # meio é onde a posição valor_busca está na lista

        # 2º caso: valor_busca é menor que lista[meio]
        elif valor_busca < lista[meio]:
            comps += 2
            fim = meio - 1   # Descarta a 2ª metade da lista

        # 3º casp: valor_busca é maior que lista[meio]
        else:
            comps += 1
            ini = meio + 1  # Decarta a 1ª metade da lista

    # 4º caso: valor_busca não encontrado na lista
    return-1
comps = 0

hora_ini = time()
print(f"Posição de FAUSTO: {busca_binaria(nomes, 'FAUSTO')}, {comps} comparações")
hora_fim = time()
print(f"Tempo gasto procurando FAUSTO: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de ZULEICA: {busca_binaria(nomes, 'ZULEICA')}, {comps} comparações")
hora_fim = time()
print(f"Tempo gasto procurando ZULEICA: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de LUNISVALDO: {busca_binaria(nomes, 'LUNISVALDO')}, {comps} comparações")
hora_fim = time()
print(f"Tempo gasto procurando LUNISVALDO: {(hora_fim - hora_ini) * 1000}ms")