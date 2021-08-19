comps = 0
passadas = 0
trocas = 0

def bubble_sort(lista):


    global comps, passadas, trocas
    comps = 0
    passadas = 0 
    trocas = 0

    while True:
        passadas += 1
        trocou = False

        for i in range(len(lista) - 1):
            comps += 1
            if lista[i + 1] < lista[i]:
               lista[i + 1],  lista[i] = lista[i], lista[i + 1]
               trocas += 1
               trocou = True

        if not trocou:
            break

# nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

# Pior caso : lista em ordem inversa
# nums = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0]

# Melhor caso : lista já ordenada
nums = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]

bubble_sort(nums)

print(nums)
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")

#####################################################################3

from data.nomes_desord import nomes
from time import time

nomes_parcial = nomes[:30000] # Usa apenas os primeiros 30 mil nomes

ini = time()
bubble_sort(nomes_parcial)
fim = time()

print(nomes_parcial)
print(f"Tempo: {fim - ini}")
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")