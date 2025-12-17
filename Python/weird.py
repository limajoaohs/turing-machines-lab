numero = int(input())
lista = []
for i in range(1,numero//2): 
    if numero % i == 0:
        break
    else:
        lista.append(i)
if lista[0] == null:
    print(-1)
else:
    print(*lista)