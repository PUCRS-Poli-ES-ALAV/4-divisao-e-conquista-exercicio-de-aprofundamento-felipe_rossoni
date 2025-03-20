import random
import time

def max(v1,v2):
    if v1 < v2:
        return v2
    return v1


def maxVal2(A):
    if len(A) <= 2:
        return max(A[0], A[-1])
    else:
        m = int(len(A)/2)
        v1 = maxVal2(A[:m])
        v2 = maxVal2(A[m+1:])
        return max(v1,v2)
    
def create_random_array(n):
    return [random.randint(0, n*10) for _ in range(n)]

# Testes
sizes = [32, 2048, 1048576]

for n in sizes:
    print(f"\nTeste com vetor de tamanho {n}:")
    
    # Criando vetor com valores aleatórios
    A = create_random_array(n)
    
    # Medindo tempo
    start_time = time.time()
    result = maxVal2(A)
    end_time = time.time()
    
    time_spent = end_time - start_time
    
    print(f"Maior valor encontrado: {result}")
    print(f"Tempo gasto: {time_spent:.6f} segundos")