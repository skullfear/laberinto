from muro import * 
from espacio import * 
from personaje import * 
from meta import * 
from elementos import * 

def main():
    with open('laberinto.txt', 'r') as archivo:
        matriz = [list(line.strip()) for line in archivo]

    elementos = {
        '1': Muro('1'),
        '0': Espacio('0'),
        'x': Personaje('x'),
        'w': Meta('w'),
        ' ': Espacio(' ')  # Agregar una entrada para el espacio en blanco
    }

    for fila in matriz:
        for elemento in fila:
            print(elementos.get(elemento, elementos[' ']), end=' ')
        print()

if __name__ == '__main__':
    main()