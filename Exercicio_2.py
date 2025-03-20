import random
import time

# Implementação do algoritmo
def maxVal1(A):
    max_val = A[0]
    iterations = 0
    for i in A:
        iterations += 1
        if i > max_val:
            max_val = i
    print(f"Número de iterações: {iterations}")
    return max_val
def create_random_array(n):
    return [random.randint(0, 999999) for _ in range(n)]

# Testes
sizes = [32, 2048, 1048576]

for n in sizes:
    print(f"\nTeste com vetor de tamanho {n}:")
    
    # Criando vetor com valores aleatórios
    A = create_random_array(n)
    
    # Medindo tempo
    start_time = time.time()
    result = maxVal1(A)
    end_time = time.time()
    
    time_spent = end_time - start_time
    
    print(f"Maior valor encontrado: {result}")
    print(f"Tempo gasto: {time_spent:.6f} segundos")