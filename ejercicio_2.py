# Cree una función que determine si un numero es primo o no. Calcule los numeros primos del 1 al 1000.
# Solo la función para determinar que es primo puede llevar un for, el resto debe ser con lambda, map, filter o reduce. 
# Imprima la lista por la consola.

def main():
    primos = lambda n: [x for x in range(2, n) if all(x % y != 0 for y in range(2, x))]
    lista_primos = primos(1000)
    print(lista_primos)
if __name__ == '__main__':
    main()