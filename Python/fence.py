def solucao():
    n  = int(input())
    if n < 6:
        return 0
    fatores = [0] * (n+1)
    for i in range(2,n+1):
        if fatores[i] == 0:
            for j in range(i,n+1,i):
                fatores[j] += 1
    cont = 0
    for i in range(1,n+1):
        if fatores [i] == 2:
            cont += 1
    return cont

print(solucao())