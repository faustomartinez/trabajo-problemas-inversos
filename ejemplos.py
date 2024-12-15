import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import funciones

# Construimos el vector x_true para nuestro ejemplo
def construir_x_true():
    dx = 10
    dy = 10
    up_width = 10
    bar_width = 5
    size = 64

    imagen_h = np.zeros((size,size))
    for i in range(size):
        if i < dy or i > size-dy:
            continue
        for j in range(size):
            if j < dx or j > size - dx:
                continue
            if j < dx + up_width or j > size - dx - up_width:
                imagen_h[i,j] = 1
            if abs(i - size/2) < bar_width:
                imagen_h[i,j] = 1
                
    x_exacto = funciones.vectorizar(imagen_h)
    return x_exacto

# Construimos la matriz de difuminación para nuestro ejemplo
def construir_A(propagacion, dimensiones):
    m = dimensiones[0]
    n = dimensiones[1]

    A = np.zeros((m*n, m*n))
    contador = 0

    for i in range(m):
        for j in range(n):
            column = funciones.vectorizar(funciones.P(propagacion, [i,j], dimensiones))
            A[:, contador] = column
            contador += 1
    factor_normalizacion = np.sum(A[:, int(m*n/2 + n/2)])
    A = 1/factor_normalizacion * A

    return A


def construir_mate():
    size = 64
    imagen = np.zeros((size, size))

    # Coordenadas y dimensiones para el cuerpo del mate
    centro_x, centro_y = size // 2, size // 2
    radio_cuerpo = size // 3
    altura_cuerpo = size // 4

    # Dibujar el cuerpo del mate (parte inferior redondeada)
    for i in range(size):
        for j in range(size):
            if (i - (centro_x + altura_cuerpo // 2)) ** 2 + (j - centro_y) ** 2 <= radio_cuerpo ** 2 and i >= centro_x - altura_cuerpo:
                imagen[i, j] = 1

    # Dibujar la boca del mate (rectángulo horizontal en la parte superior, más angosta)
    for i in range(centro_x - altura_cuerpo, centro_x - altura_cuerpo + 5):
        for j in range(centro_y - radio_cuerpo // 2, centro_y + radio_cuerpo // 2):
            imagen[i, j] = 1

    # Dibujar la bombilla (línea diagonal ligeramente más gruesa del centro hacia arriba derecha)
    for i in range(centro_x - altura_cuerpo, centro_x - altura_cuerpo - 15, -1):
        for j_offset in range(-2, 3):  # Grosor adicional
            j = centro_y + (centro_x - altura_cuerpo - i) // 2 + j_offset
            if 0 <= j < size:
                imagen[i, j] = 1

    x_exacto = funciones.vectorizar(imagen)
    return x_exacto

