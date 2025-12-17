import math

def gcd_list(numbers):
    if not numbers:
        return 0
    
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = math.gcd(result, numbers[i])
        if result == 1:
            return 1
    return result

def count_divisors(n):
    if n == 0:
        return 0
    
    count = 0
    limit = int(math.sqrt(n))
    
    for i in range(1, limit + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count
n_str = input()    
n = int(n_str)
arr = list(map(int, input().split()))
        
common_divisor = gcd_list(arr)
        
print(count_divisors(common_divisor))