# Pedro, Juan y María son 3 estudiantes de un colegio, cada uno de ellos tiene las notas de sus ramos en una lista ordenadas de la siguiente forma:
# Historia, Lenguaje, Matemáticas, Física, Química y Biología. Escriba un programa que reciba las 3 listas y devuelva una nueva lista con el 
# promedio de cada estudiante. Por ejemplo, si Pedro tiene las notas [4, 5, 6, 7, 4, 3], Juan tiene las notas [5, 6, 4, 3, 3, 3] y María tiene las
# notas [6, 6, 5, 4, 3, 3], el programa debe devolver [5.0, 5.66, 5.0, 4.66, 3.33, 3.0]. Redondee los promedios a 2 decimales.
# Utilice lambda, map, filter o reduce según corresponda.

# Muestre el promedio de cada asignatura de los 3 estudiantes de la siguiente forma por la consola:
# Historia: 5.0
# Lenguaje: 5.66
# Matemáticas: 5.0
# Física: 4.66
# Química: 3.33
# Biología: 3.0

notas_pedro = [4,5,6,7,4,3]
notas_juan = [5,6,4,3,3,3]
notas_maria = [6,6,5,4,3,3]
notas_promedio=[0,0,0,0,0,0]

def main():
    for n in range(0,6):
        notas_promedio[n]=notas_pedro[n]+notas_juan[n]+notas_maria[n]
        # print(notas_promedio[n])
    promedio_asignatura = list(map(lambda x: x/3, notas_promedio))
    promedio_asignatura = list(map(lambda x: round(x,2), promedio_asignatura))
    print(promedio_asignatura)
    return

if __name__ == "__main__":
    main()