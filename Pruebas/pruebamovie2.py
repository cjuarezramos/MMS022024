import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

k = 5
Lx = 10
Ly = 10
dx = 1
dy = 1
Tfin = 20
dt = 1
condicion = 1/8 * (dx**2 + dy**2) / k
print(condicion)

x = np.arange(0, Lx + dx, dx)
y = np.arange(0, Ly + dy, dy)
t = np.arange(0, Tfin + dt, dt)
[X,Y] = np.meshgrid(x,y)

T = np.zeros((len(y), len(x), len(t)))*np.nan
# condiciones iniciales
for i in range(len(x)):
    for j in range(len(y)):
        if j>i:
            T[j, i, 0] = 25

# condiciones de frontera
T[:, 0, :] = 65
T[-1, :, :] = 10
for i in range(len(x)):
    T[i,i, :] = 100
plt.figure()
plt.contourf(X,Y,T[:,:,0])

for l in range(len(t) - 1):
    for j in range(1, len(y) - 1):
        for i in range(1, len(x) - 1):
            if j>i:
                d2Tdx2 = (T[j, i + 1, l] - 2 * T[j, i, l] + T[j, i - 1, l]) / dx**2
                d2Tdy2 = (T[j + 1, i, l] - 2 * T[j, i, l] + T[j - 1, i, l]) / dy**2
                T[j, i, l + 1] = T[j, i, l] + k * dt * (d2Tdy2 + d2Tdx2)
            

# Gráficas
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots()
contour = ax.contourf(X, Y, T[:, :, 0])
fig.colorbar(contour)
ax.set_title('Distribución de Temperatura')

def update(frame):
    ax.clear()
    contour = ax.contourf(X, Y, T[:, :, frame])
    return contour

ani = animation.FuncAnimation(fig, update, frames=len(t))
plt.show()
