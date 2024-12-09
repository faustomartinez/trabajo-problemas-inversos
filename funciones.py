import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Función para convertir una imagen 2D a un vector 1D
def vectorizar(imagen):
    n, m = image.shape
    return imagen.reshape((n*m))

# Función para convertir un vector 1D a una imagen 2D
def im(x, dimensiones):
    return x.reshape(dimensiones)

# Función para mostrar un vector 1D como su correspondiente imagen 2D
def mostrar_vector(vec, dimensiones, escala=1):
    imagen = im(vec, dimensiones)
    # Los parámetros son para mostrar al vector en escala de grises
    plt.imshow(imagen, vmin=0, vmax=scale * np.max(vec), cmap='gray')
    plt.axis('off')
    plt.show()

# Función para guardar la imagen generada por el vector en una archivo
def guardar_vector(vec, dimensiones, nombre_archivo, escala=1):
    imagen = im(vec,dimensiones)
    plt.imshow(imagen, vmin=0, vmax=scale * np.max(vec), cmap='gray')
    plt.axis('off')
    plt.savefig(nombre_archivo, bbox_inches='tight')

# Funcion para difuminar un determinado pixel con una determinada propagación Gaussiana
def P(propagacion, pixel, dimensiones):
    imagen = np.zeros(dimensiones)
    for i in range(dimensiones[0]):
        for j in range(dimensiones[1]):
            v = np.exp(-(((i-pixel[0])/propagacion[0])**2 + ((j-pixel[1])/propagacion[1])**2)/2)
            if v < 0.0001:
                continue
            imagen[i,j] = v
    return imagen

# Construimos la matriz del operador primera derivada en 1D
def operador_derivada_1D(n):

    d = np.ones(n-1)
    D = np.diag(d,-1)
    L = np.identity(n) - D

    return L

# Construimos la matriz del operador primera derivada en 2D
def operador_derivada_2D(n):

    L1 = operador_derivada_1D(n)
    KP1 = np.kron(np.identity(n), L1)
    KP2 = np.kron(L1, np.identity(n))
    L = np.vstack((KP1,KP2))

    return L


def 

