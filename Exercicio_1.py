import random
def merge_sort(lista):
    if len(lista) == 1:
        return lista
    
    mid = len(lista) // 2
    left = lista[:mid]
    right = lista[mid:]
    
    a = merge_sort(left)
    b = merge_sort(right)

    return merge(a, b)

def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1

    result.extend(a[i:])
    result.extend(b[j:])
    return result

lista = random.sample(range(1,100), 32)
#print("Lista não organizada: ", lista)
print("Lista organizada: ", merge_sort(lista))
lista2 = random.sample(range(1,3000), 2048)
#print("Lista não organizada: ", lista2)
print("Lista organizada: ", merge_sort(lista2))
lista = random.sample(range(1,100000000), 1048576)
print("Lista organizada: ", merge_sort(lista))

