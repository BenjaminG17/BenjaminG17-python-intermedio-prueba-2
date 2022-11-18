# Cree una calculadora que reciba una lista de numeros. Utilice función lambda, map, filter o reduce según corresponda.
# Imprima el resultado por la consola.

# Por ejemplo, si la lista es [2, 3, 4, 5, 6], el programa debe devolver:
# Suma: 20
# Resta: -16
# Multiplicación: 720
# División: 0.001388888888888889
# Exponente: 2348542582773833227889480596789337027375682548908319870707290971532209025114608443463698998384768703031934976
# Raiz cuadrada: 1.001927263624698

from functools import reduce
valores=input("Ingrese numeros que quiere calcular separados por un guion: ")
numeros= valores.split('-')
numeros = list(map(lambda x: int(x), numeros))
print(numeros)


def main(listado):
    suma = reduce(lambda x,y: x+y ,listado)
    print(suma)
    restar = reduce(lambda x,y: x-y, listado)
    print(restar)
    producto = reduce(lambda x,y: x*y, listado)
    print(producto)
    division = reduce(lambda x,y: x/y, listado)
    print(division)
    exponencial= reduce(lambda x,y:x**y, listado)
    print(exponencial)
    raizCuadrada =reduce(lambda x,y: x**(1/y), listado)
    print(raizCuadrada) 

if __name__ == "__main__":
    main(numeros)