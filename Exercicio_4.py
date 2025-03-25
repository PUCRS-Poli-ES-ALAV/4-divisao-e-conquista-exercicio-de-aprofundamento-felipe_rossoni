import random
import math
import time

iterations = 0
def multiply(x,y,n):
    global iterations 
    iterations +=1
    if(n == 1):
        return x*y
    else:
        m = math.ceil(n/2)
        a = x//2**m
        b = x % 2**m
        c = y//2**m
        d = y % 2**m
        e = multiply(a, c, m)
        f = multiply(b, d, m)
        g = multiply(b, c, m)
        h = multiply(a, d, m)
        return (2**(2*m))*e + 2**m*(g + h) + f

for bits in [4, 16, 64]:
        print(f"\nTamanho: {bits}-bit")
        
        # Generate max values for the given bit size
        max_val = (2 ** bits) - 1
        
        # Test cases
        x = max_val // 2
        y = max_val // 3
        
        # Track iterations (this is a proxy, as tracking exact recursive calls is complex)
        
        
        # Measure time and perform multiplication
        start_time = time.time()
        result = multiply(x, y, bits)
        end_time = time.time()
        
        #print(f"x = {x}")
        #print(f"y = {y}")
        #print(f"Result = {result}")
        #print(f"Correct: {result == x * y}")
        print(f"Time taken: {(end_time - start_time):.6f} ms")
        print(f"Iterações = {iterations}")
