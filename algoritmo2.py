"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""
# Busca binaria

def m(n, o):
     
    p = 0               # Primeira posição  
    q = len(n) - 1      # Última posição
      # o que for menor  
    while p <= q:
        r = (n + o) // 2     # Operador divisão 
        if n[r] == o: 
           return r     # retornar onde o r está
        # 2º caso: Se o é menor que n[r]
        elif o < n[r]: q = r - 1  
        else: p = r + 1    # Decarta a 1ª metade da lista
        return -1

