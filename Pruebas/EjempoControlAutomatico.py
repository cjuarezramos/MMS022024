"""
Autor: Carlos Anibal Juárez
Fecha: 13/08/2024
Descripción: Es un ejemplo del sistema de control automático.

"""
import numpy as np
import control as ct
import matplotlib.pyplot as plt

# Parametros
M = 0.574
R = 2.27
L = 0.0047
Km = 0.25
Kb = 0.25
B = 0.003026
J = 0.00246
Kc = 1

# setpoint
wi = 1

# definición de datos para solución
# paso de integración
h = 0.001
#tiempo final de simulación
tf = 0.2
# arreglo de tiempo
t = np.arange(0,tf,h)

x = np.zeros([t.size,t.size])


def f(x,wi,t):
    i = x[0]
    w = x[1]
    V = Kc*(wi-w)
    fi = -R/L*i -Kb/L*w + 1/L*V
    fw = Km/J*i-B/J*w
    return fi,fw

# condiciones iniciales
i0 = 0;
w0 = 0;
x[0][0] = i0
x[1][0] = w0

# Solución por euler
for i in np.arange(1,t.size):
    y = f([x[0][i-1],x[1][i-1]],wi,t[i-1])
    x[0][i] = x[0][i-1]+h*y[0]
    x[1][i] = x[1][i-1]+h*y[1]



plt.plot(t,x[1])