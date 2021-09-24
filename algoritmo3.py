"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""
#bubble_sort

def m(n):
    while 1 > 0:
        o = False # Loop eterno
          # A última posição estará em len(o) - 1  ou seja, 9 -> range(len(o))
          # A penúltima posição estará em len(o) - 2, ou seja, 8 -> range(len(o) - 1)
        for p in range(len(o) - 1): # Inicia nova passada
            if n[p + 1] < n[p]: # É necessário trocar
                n[p + 1], n[p] = n[p], n[p + 1] # Faz a troca
                o = True # trocou 
        if not o: 
            break # Interrompe o while