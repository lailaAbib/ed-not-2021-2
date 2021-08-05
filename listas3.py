#lstas de strings
frutas = ["laranja", "maça", "uva", "pera", "mamão", "abacate", "amora"]

#imprimindo apenas a fruta "uva"
print(frutas[2])

#substuindo 'pera' por 'melão'
frutas[3] = "melão"
print(frutas)

# Descobrindo quantos elementos há na lista
print(len(frutas))

print('------------------')

# Percorrendo e imprimindo cada um dos elementos da lista
for fruta in frutas:
    print(fruta)

print('------------------')

# Percorrendo e imprimindo cada elemento e sua posição
for i in range(len(frutas)):
    print(f"{frutas[i]} está na posição {i}")

print('------------------')

# Percurso em ordem invertida
# len(frutas) - 1: a lista precisa começar no último elemento, que é
# determinado por len() - 1
# 2º argumento: -1, porque o limite final nao entra e precisamos terminar em 0
# 3 argumento: -1, porque a lista precisa ser decrescente
for j in range(len(frutas) - 1, -1, -1):
    print(frutas[j])

print('------------------')

frutas.sort()
print(frutas)