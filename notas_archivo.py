import time


def procesa_fila(fila: list[str]) -> list[float]:
    nums = list()
    for num_str in fila:
        num = float(num_str)
        nums.append(num)
    
    return nums


def calcula_nota_final(alumno: list[float]) -> float:
    nota_lab = 0
    for i in range(1, 13):
        nota_lab += alumno[i]
    nota_lab = nota_lab / 13.0

    nota_final = ((5 * nota_lab) + (2.5 * alumno[13]) + (2.5 * alumno[14])) / 10.0

    return nota_final


if __name__ == '__main__':
    inicio_total = time.perf_counter()

    inicio_entrada = time.perf_counter()
    with open("notas.csv", "r") as f:
        contenido = f.read()
    fin_entrada = time.perf_counter()

    inicio_cpu = time.perf_counter()
    filas = contenido.split("\n")
    
    alumnos = list()
    for i in range(1, len(filas)):
        fila = filas[i].split(",")
        nota_alumno = procesa_fila(fila)
        alumnos.append(nota_alumno)
    
    notas_finales = list()
    for alumno in alumnos:
        nota = calcula_nota_final(alumno)
        notas_finales.append(nota)
    fin_cpu = time.perf_counter()

    inicio_salida = time.perf_counter()
    print(alumnos)
    print(notas_finales)
    fin_salida = time.perf_counter()

    fin_total = time.perf_counter()

    tiempo_total = fin_total - inicio_total
    tiempo_entrada = fin_entrada - inicio_entrada
    tiempo_cpu = fin_cpu - inicio_cpu
    tiempo_salida = fin_salida - inicio_salida

    print(f"Tiempo total de ejecucion: {tiempo_total} segundos")
    print(f"Tiempo total de E/S: {tiempo_entrada + tiempo_salida} segundos")
    print(f"Tiempo total de procesamiento: {tiempo_cpu} segundos")
    print(f"Porcentaje de lectura de archivo: {(tiempo_entrada / tiempo_total) * 100}% - porcentaje de salida: {(tiempo_salida / tiempo_total) * 100}%")
    print(f"Procentaje de tiempo en E/S: {((tiempo_entrada + tiempo_salida) / tiempo_total) * 100}%")