import random
import time

def merge_sort(lista):
    global iter_count
    if len(lista) == 1:
        return lista
    
    mid = len(lista) // 2
    left = lista[:mid]
    right = lista[mid:]
    
    a = merge_sort(left)
    b = merge_sort(right)

    return merge(a, b)

def merge(a, b):
    global iter_count
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        iter_count += 1
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result

def run_sort(lista):
    global iter_count
    iter_count = 0
    start_time = time.time()
    sorted_list = merge_sort(lista)
    end_time = time.time()
    
    #print(f"Lista organizada: {sorted_list[:10]} ... {sorted_list[-10:]}")  # Mostra apenas parte da lista
    print(f"Tempo de execução: {end_time - start_time:.5f} segundos")
    print(f"Número de iterações: {iter_count}\n")

# Testando com diferentes tamanhos de lista
iter_count = 0
lista1 = random.sample(range(1, 100), 32)
run_sort(lista1)

lista2 = random.sample(range(1, 3000), 2048)
run_sort(lista2)

lista3 = random.sample(range(1, 100000000), 1048576)
run_sort(lista3)