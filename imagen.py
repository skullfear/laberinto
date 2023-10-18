import pygame
import sys
from muro import * 
from espacio import * 
from personaje import * 
from meta import * 



# Cargar el laberinto desde el archivo
def cargar_laberinto(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido

# Función para mostrar el laberinto
def mostrar_laberinto(laberinto, elementos, pantalla):
    x, y = 0, 0  # Coordenadas iniciales

    for fila in laberinto.split('\n'):
        for elemento in fila:
            objeto = elementos.get(elemento, elementos['2'])
            imagen = pygame.image.load(objeto.simbolo + '.png')
            pantalla.blit(imagen, (x, y))
            x += 60
        x = 60
        y += 60

    pygame.display.flip()

def main():
    pygame.init()

    ancho, alto = 1000, 700
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption('Laberinto')

    elementos = {
        '1': Muro('1'),
        '0': Espacio('0'),
        'x': Personaje('x'),
        'w': Meta('w'),
        '2': Espacio('2')
    }

    laberinto = cargar_laberinto('laberinto.txt')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mostrar_laberinto(laberinto, elementos, pantalla)

if __name__ == '__main__':
    main()