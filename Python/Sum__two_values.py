import sys

def solucao():
    linha_entrada = sys.stdin.readline()
    
    if not linha_entrada:
        return
        
    n, x = map(int, linha_entrada.split())
    
    valores = list(map(int, sys.stdin.readline().split()))
    
    vistos = {}
    
    for i, valor_atual in enumerate(valores):
        complemento = x - valor_atual
        
        if complemento in vistos:
            print(f"{vistos[complemento]} {i + 1}")
            return
        
        vistos[valor_atual] = i + 1
        
    print("IMPOSSIBLE")

solucao()