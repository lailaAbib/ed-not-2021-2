"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""
#Recursivo

# Implementação iterativa
def m(n):
    if p is None: p = len(n)  - 1
    if p <= o: # Condição de saída
        return # Sai da função sem fazer nada
    q = p
    r = o - 1
    # O range começa no O e vai descendo até o p
    for i in range(o, p):
        if n[i] < n[q]:
            r += 1
            if r != i: n[r], n[i] = n[i], n[r]  # Faz a troca
    r += 1
    if n[q] < n[r] and q != r: n[q], n[r] = n[r], n[q]
    m(n, o, r - 1)
    m(n, r + 1, p)





 

