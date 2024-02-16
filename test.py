import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani

def mandlebrot(x,y,threshold):
    z = complex(0,0)
    c = complex(x,y)

    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 16.:
            return i
    
    return threshold - 1

x_start, y_start = -2.0, -2.0

width, height = 3, 2

real = np.linspace(x_start, x_start + width, width * 250)
imag = np.linspace(y_start, y_start + width, height * 250)

fig,ax = plt.subplots()

def printeaza(a):

    ax.clear()
    ax.set_xticks([], [])
    ax.set_yticks([], [])

    X = np.empty((len(real),len(imag)))

    threshold = round(1.15**(1+a))

    for i in range(len(real)):
        for j in range(len(imag)):
            X[i,j] = mandlebrot(real[i],imag[j],threshold)
    
    img = ax.imshow(X.T, interpolation="bicubic", cmap='inferno')
    return img


animare = ani.FuncAnimation(fig, printeaza, frames = 45, interval = 120)
plt.show()