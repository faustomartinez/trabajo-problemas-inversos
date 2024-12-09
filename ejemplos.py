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
            column = funciones.vec(funciones.P(propagacion, [i,j], dimensiones))
            A[:, contador] = column
            contador += 1
    factor_normalizacion = np.sum(A[:, int(m*n/2 + n/2)])
    A = 1/factor_normalizacion * A

    return A

# Definimos una función para la transformada de Haar
def Haar_Wavelet_transform(n):
    W = np.zeros((n,n))
    knt = 0
    for k in range (0, int(n/2)):
        W[k][knt] = 1
        W[k][knt+1] = 1
        W[k+int(n/2)][knt] = 1
        W[k+int(n/2)][knt+1] = -1
        knt=knt+2
    W=(1/np.sqrt(2))*W
    W1 = W[0:int(n/2),:]
    return W1
