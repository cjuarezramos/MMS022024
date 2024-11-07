import mat2py as mp
from mat2py.core import *


def main():
    k = 0.5
    Lx = 10
    Ly = 10
    dx = 1
    dy = 1
    Tfin = 20
    dt = 0.1
    condicion = mrdivide((1 / 8) * ((dx**2) + (dy**2)), k)
    x = M[0:dx:Lx]
    y = M[0:dy:Ly]
    t = M[0:dt:Tfin]
    T = zeros(length(y), length(x), length(t))
    T[I[:, :, 1]] = 20
    T[I[1, :, :]] = 100
    T[I[:, 1, :]] = 10
    T[I[end, :, :]] = 65
    T[I[:, end, :]] = 35
    for l in M[1 : (length(t) - 1)]:
        for j in M[2 : (length(y) - 1)]:
            for i in M[2 : (length(x) - 1)]:
                d2Tdx2 = mrdivide(
                    (T(j, i + 1, l) - (2 * T(j, i, l))) + T(j, i - 1, l), dx**2
                )
                d2Tdy2 = mrdivide(
                    (T(j + 1, i, l) - (2 * T(j, i, l))) + T(j - 1, i, l), dy**2
                )
                T[I[j, i, l + 1]] = T(j, i, l) + ((M[M[k] @ dt]) @ (d2Tdy2 + d2Tdx2))

    X, Y = meshgrid(x, y)
    h = copy(figure)
    contourf(X, Y, T[I[:, :, 1]])
    colorbar
    ax = copy(gca)
    ax.NextPlot = "replaceChildren"
    _M[I[length(t)]] = struct("cdata", M[[]], "colormap", M[[]])
    h.Visible = "off"
    for l in M[2 : length(t)]:
        contourf(X, Y, T[I[:, :, l]])
        colorbar
        drawnow
        _M[I[l]] = copy(getframe)

    h.Visible = "on"
    movie(_M)


if __name__ == "__main__":
    main()