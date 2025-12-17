import math

def resolver_primos():
    limite = 100_000_000
    is_prime = bytearray([1]) * limite
    is_prime[0] = is_prime[1] = 0

    for p in range(2, int(math.sqrt(limite)) + 1):
        if is_prime[p]:
            is_prime[p*p::p] = bytes(len(is_prime[p*p::p]))
            
    contador = 0
    for i in range(limite):
        if is_prime[i]:
            contador += 1
            if contador % 100 == 1:
                print(i)

resolver_primos()