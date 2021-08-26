# 3! = 3 . 2 . 1 = 6
# 4! = 4. 3 . 2 . 1 = 24
# 5! = 5 . 4 . 3 . 2 . 1 = 120
# 6! = 6 . 5 . 4 . 3 . 2 . 1 = 720
# 7! = 7 . 6 . 5 . 4 . 3 . 2 . 1 = 5.040
# 8! = 8 . 7 . 6 . 5 . 4 . 3 . 2 . 1 = 40.320
# 9! = 9 . 8 . 7 . 6 . 5 . 4 . 3 . 2 . 1 = 362.880
# 10! = 10 . 9 . 8 . 7 . 6 . 5 . 4 . 3 . 2 . 1 = 3.628.800


# Implementação interativo
def fatorial(n):
    resultado = 1
    if(n > 1):
        # range começa no número n e vai descendo até 1
        for i in range(n, 1, -1):
            resultado *= i
            print(f'Resultado: {resultado}, i: {i}')
    return resultado

print(f'5! = {fatorial(5)}')
print(f'7! = {fatorial(7)}')

# n! = n * (n - 1)! p/ n > 1
# Recursividade ocorre quando definição de uma função inclui a própia
# função sendo definida


# Em programação, a recursividade se traduz quando uma função efetua
# chamadas a si própria.

# Implementação recursiva
def fatorial2(n):
    # Em uma função recursiva, a condição de saída é aquela em que 
    # a função é capaz de retornar um resultado SEM chamar novamente
    # a si mesma
    if n <= 1: # Condição de saída
        return 1
    return n * fatorial2(n - 1)

print('-------------------------------------')
print(f'519! = {fatorial(519)}')
