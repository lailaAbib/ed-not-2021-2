# ALGORITMO DE ORDENAÇÃO SELECTION SORT
#
# Isola (seleciona) o primeiro elemento da lista e, em seguida,
# encontra o menor valor no restante da lista. Se o valor encontrado
# for o menor que o selecionado, efetua a troca.
# Em seguida, isso o segundo número da lista, buscando pelo menor 
# valor das posições subsequentes. Faz a troca entre os dois valores.
# se necessário. Contínua o processo, até isolar o penúltimo elemento
# da lista.

comps = 0
passadas = 0
trocas = 0

def selection_sort(lista):
    """
        Função que implementa o algoritmo de ordenação selection sort
    """

    global comps, passadas, trocas
    comps = 0
    passadas = 0
    trocas = 0

    # Percurso da lista até a penúltima posição
    for pos_sel in range(len(lista) - 1):    # Seleciona (isola) o elemento que será comparado
        passadas += 1

        pos_menor = pos_sel + 1
        # Rotina para encontrar o menor número no resto da lista
        # Percurso da lista da posição i + 2 até o fim
        for j in range(pos_sel + 2, len(lista)):
            comps += 1

            # Se o elemento da posição atual (j) for menor
            # que o elemento na posição do menor (pos_menor),
            # atualizamos pos_menor
            if lista[j] < lista[pos_menor]:
                pos_menor = j

        # Comparamos lista[sel] com lista[pos_menor] e, se segundo
        # for menor que o primeiro, efetuamos a troca entre eles
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

##################################################################################

# Valores das variáveis no ínicio do selection sort:
# pos_sel: 0 (onde está o 88)
# pos_menor: 1 (onde está o 44)
# j: 2 (onde está o 33)
# nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

# NÃO é o pior caso : lista em ordem inversa
# nums = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0]

# Melhor caso : lista já ordenada
nums = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]

selection_sort(nums)
print(nums)
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")

##########################################################################

from data.nomes_desord import nomes
from time import time

#nomes_parcial = nomes[:30000] # Usa apenas os primeiros 30 mil nomes

ini = time()
#selection_sort(nomes_parcial)
selection_sort(nomes)
fim = time()

#print(nomes_parcial)
print(nomes)
print(f"Tempo: {fim - ini}")
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")
