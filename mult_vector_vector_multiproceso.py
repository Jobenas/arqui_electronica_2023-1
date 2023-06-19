import time
import numpy as np
from itertools import repeat
from multiprocessing import Pool, cpu_count


N = 5000
M = 5000

def mult_vector_vector(x, y):
    suma = 0

    for i in range(len(y)):
        suma += x[i] * y[i]
    
    return suma


if __name__ == '__main__':
    resultado = list()

    mat_M = np.random.randint(100, size=(M,N))
    vector_A = np.random.randint(100, size=(M,))

    inicio = time.perf_counter()
    args = zip(mat_M, repeat(vector_A))
    p = Pool(processes=cpu_count())
    resultado = p.starmap(mult_vector_vector, args)
    p.close()
    p.join()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion multiproceso: {fin - inicio} segundos")

