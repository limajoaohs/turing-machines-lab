import sys

def resolver_primal_fear():
    limite = 1_000_000
    
    is_prime = bytearray([1]) * limite
    is_prime[0] = is_prime[1] = 0
    for p in range(2, int(limite**0.5) + 1):
        if is_prime[p]:
            is_prime[p*p::p] = bytes(len(is_prime[p*p::p]))
            
    fearful_count = [0] * limite
    for i in range(2, limite):
        fearful_count[i] = fearful_count[i-1]
        
        s_num = str(i)
        if '0' in s_num:
            continue
            
        is_i_fearful = True
        for j in range(len(s_num)):
            trunc_num = int(s_num[j:])
            if not is_prime[trunc_num]:
                is_i_fearful = False
                break
        
        if is_i_fearful:
            fearful_count[i] += 1
            
    try:
        input_lines = sys.stdin.readlines()
        if not input_lines:
            return
            
        for line in input_lines[1:]:
            n = int(line)
            print(fearful_count[n])
            
    except (IOError, ValueError):
        return

resolver_primal_fear()