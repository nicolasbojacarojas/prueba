import numpy as np
import matplotlib.pyplot as plt
def vida():
    plt.axis("equal")
    puntos = np.linspace(0, 2*np.pi, 100)
    x = np.sin(puntos)
    y = np.cos(puntos)
    for j in range(-2, 3):
        if j==0:
            for i in range(0,3):
                x1 = 1/3*np.sin(puntos)
                y1 = 1/3*np.cos(puntos)
                if i == 1:
                    my = i - 5/3
                elif i == 2:
                    my = i -4/3
                else:
                    my = i
                plt.plot(x1,y1 + my, "k")
        elif j==-1:
            mx1 = -(np.sqrt(3)/6)
            for i in range(-2,2):
                x1 = 1/3*np.sin(puntos)
                y1 = 1/3*np.cos(puntos)
                if i==-2:
                    my1 = i + 3/2    
                elif i==-1:
                    my1 = i + 5/6
                elif i==0:
                    my1 = i + 1/6
                else:
                    my1 = i - 1/2
                plt.plot (x1 + mx1, y1 + my1, "k")
        elif j==1:
            mx2 = (np.sqrt(3)/6)
            for i in range(-2,2):
                x2 = 1/3*np.sin(puntos)
                y2 = 1/3*np.cos(puntos)
                if i==-2:
                    my2 = i + 3/2    
                elif i==-1:
                    my2 = i + 5/6
                elif i==0:
                    my2 = i + 1/6
                else:
                    my2 = i - 1/2
                plt.plot (x2 + mx2, y2 + my2, "k")
        elif j==-2:
            mx3 = -np.sqrt(3)/3
            for i in range (-1, 2):
                x3 = 1/3*np.sin(puntos)
                y3 = 1/3*np.cos(puntos)
                if i==-1:
                    my3 = -1/3
                elif i==0:
                    my3 = i
                else:
                    my3 = 1/3
                plt.plot (x3 + mx3, y3 + my3, "k")
        elif j==2:
            mx4 = np.sqrt(3)/3
            for i in range (-1, 2):
                x4 = 1/3*np.sin(puntos)
                y4 = 1/3*np.cos(puntos)
                if i==-1:
                    my4 = -1/3
                elif i==0:
                    my4 = i
                else:
                    my4 = 1/3
                plt.plot (x4 + mx4, y4 + my4, "k")

    pdif1 = np.linspace (4*np.pi/6, 8*np.pi/6)
    xpdif1 = 1/3*np.sin(pdif1)
    ypdif1 = 1/3*np.cos(pdif1)
    plt.plot(xpdif1, ypdif1+1,"k")

    pdif2 = np.linspace (10*np.pi/6,14*np.pi/6)
    xpdif2 = 1/3*np.sin(pdif2)
    ypdif2 = 1/3*np.cos(pdif2)
    plt.plot(xpdif2, ypdif2-1,"k")

    pdif3 = np.linspace (4*np.pi/6,10*np.pi/6)
    xpdif3 = 1/3*np.sin(pdif3)
    ypdif3 = 1/3*np.cos(pdif3)
    plt.plot(xpdif3 + np.sqrt(3)/6, ypdif3+5/6,"k")

    pdif4 = np.linspace (2*np.pi/6,8*np.pi/6)
    xpdif4 = 1/3*np.sin(pdif4)
    ypdif4 = 1/3*np.cos(pdif4)
    plt.plot(xpdif4 - np.sqrt(3)/6, ypdif4+5/6,"k")

    pdif5 = np.linspace (0,2*np.pi,100)
    xpdif5 = 1/3*np.sin(pdif5)
    ypdif5 = 1/3*np.cos(pdif5)
    plt.plot(xpdif5, ypdif5+1/3,"k")

    pdif6 = np.linspace (0,2*np.pi,100)
    xpdif6 = 1/3*np.sin(pdif6)
    ypdif6 = 1/3*np.cos(pdif6)
    plt.plot(xpdif6, ypdif6-1/3,"k")

    pdif7 = np.linspace (10*np.pi/6,16*np.pi/6)
    xpdif7 = 1/3*np.sin(pdif7)
    ypdif7 = 1/3*np.cos(pdif7)
    plt.plot(xpdif7 - np.sqrt(3)/6, ypdif7 - 5/6,"k")

    pdif8 = np.linspace (8*np.pi/6,14*np.pi/6)
    xpdif8 = 1/3*np.sin(pdif8)
    ypdif8 = 1/3*np.cos(pdif8)
    plt.plot(xpdif8 + np.sqrt(3)/6, ypdif8 - 5/6,"k")

    pdif9 = np.linspace (8*np.pi/6, 2*np.pi/6)
    xpdif9 = 1/3*np.sin(pdif9)
    ypdif9 = 1/3*np.cos(pdif9)
    plt.plot(xpdif9 - np.sqrt(3)/3, ypdif9 + 2/3,"k")

    pdif0 = np.linspace (4*np.pi/6, 10*np.pi/6)
    xpdif0 = 1/3*np.sin(pdif0)
    ypdif0 = 1/3*np.cos(pdif0)
    plt.plot(xpdif0 + np.sqrt(3)/3, ypdif0 + 2/3,"k")

    pd0 = np.linspace (10*np.pi/6, 16*np.pi/6)
    xpd0 = 1/3*np.sin(pd0)
    ypd0 = 1/3*np.cos(pd0)
    plt.plot(xpd0 - np.sqrt(3)/3, ypd0 - 2/3,"k")
    
    pd1 = np.linspace (14*np.pi/6, 8*np.pi/6)
    xpd1 = 1/3*np.sin(pd1)
    ypd1 = 1/3*np.cos(pd1)
    plt.plot(xpd1 + np.sqrt(3)/3, ypd1 - 2/3,"k")
    
    pd2 = np.linspace (12*np.pi/6, 8*np.pi/6)
    xpd2 = 1/3*np.sin(pd2)
    ypd2 = 1/3*np.cos(pd2)
    plt.plot(xpd2 + np.sqrt(3)/2, ypd2 - 1/2,"k")

    pd3 = np.linspace (12*np.pi/6, 16*np.pi/6)
    xpd3 = 1/3*np.sin(pd3)
    ypd3 = 1/3*np.cos(pd3)
    plt.plot(xpd3 - np.sqrt(3)/2, ypd3 - 1/2,"k")

    pd4 = np.linspace (14*np.pi/6, 18*np.pi/6)
    xpd4 = 1/3*np.sin(pd4)
    ypd4 = 1/3*np.cos(pd4)
    plt.plot(xpd4 - np.sqrt(3)/2, ypd4 + 1/2,"k")

    pd5 = np.linspace (6*np.pi/6, 10*np.pi/6)
    xpd5 = 1/3*np.sin(pd5)
    ypd5 = 1/3*np.cos(pd5)
    plt.plot(xpd5 + np.sqrt(3)/2, ypd5 + 1/2,"k")

    pd6 = np.linspace (8*np.pi/6, 6*np.pi/6)
    xpd6 = 1/3*np.sin(pd6)
    ypd6 = 1/3*np.cos(pd6)
    plt.plot(xpd6 + np.sqrt(3)/3, ypd6 + 1,"k")

    pd7 = np.linspace (6*np.pi/6, 4*np.pi/6)
    xpd7 = 1/3*np.sin(pd7)
    ypd7 = 1/3*np.cos(pd7)
    plt.plot(xpd7 - np.sqrt(3)/3, ypd7 + 1,"k")

    pd7 = np.linspace (10*np.pi/6, 12*np.pi/6)
    xpd7 = 1/3*np.sin(pd7)
    ypd7 = 1/3*np.cos(pd7)
    plt.plot(xpd7 + np.sqrt(3)/3, ypd7 - 1,"k")

    pd8 = np.linspace (2*np.pi/6, 0*np.pi/6)
    xpd8 = 1/3*np.sin(pd8)
    ypd8 = 1/3*np.cos(pd8)
    plt.plot(xpd8 - np.sqrt(3)/3, ypd8 - 1,"k")

    pd9 = np.linspace (4*np.pi/6, 6*np.pi/6)
    xpd9 = 1/3*np.sin(pd9)
    ypd9 = 1/3*np.cos(pd9)
    plt.plot(xpd9 - np.sqrt(3)/6, ypd9 + 7/6,"k")

    pd10 = np.linspace (6*np.pi/6, 8*np.pi/6)
    xpd10 = 1/3*np.sin(pd10)
    ypd10 = 1/3*np.cos(pd10)
    plt.plot(xpd10 + np.sqrt(3)/6, ypd10 + 7/6,"k")

    p0 = np.linspace (10*np.pi/6, 12*np.pi/6)
    xp0 = 1/3*np.sin(p0)
    yp0 = 1/3*np.cos(p0)
    plt.plot(xp0 + np.sqrt(3)/6, yp0 - 7/6,"k")

    p0 = np.linspace (0*np.pi/6, 2*np.pi/6)
    xp0 = 1/3*np.sin(p0)
    yp0 = 1/3*np.cos(p0)
    plt.plot(xp0 - np.sqrt(3)/6, yp0 - 7/6,"k")

    p1 = np.linspace (0*np.pi/6, 6*np.pi/6)
    xp1 = 1/3*np.sin(p1)
    yp1 = 1/3*np.cos(p1)
    plt.plot(xp1 - np.sqrt(3)/2, yp1 + 1/6,"k")
    
    p2 = np.linspace (0*np.pi/6, 6*np.pi/6)
    xp2 = 1/3*np.sin(p2)
    yp2 = 1/3*np.cos(p2)
    plt.plot(xp2 - np.sqrt(3)/2, yp2 - 1/6,"k")
    
    p3 = np.linspace (6*np.pi/6, 12*np.pi/6)
    xp3 = 1/3*np.sin(p3)
    yp3 = 1/3*np.cos(p3)
    plt.plot(xp3 + np.sqrt(3)/2, yp3 - 1/6,"k")
    
    p3 = np.linspace (6*np.pi/6, 12*np.pi/6)
    xp3 = 1/3*np.sin(p3)
    yp3 = 1/3*np.cos(p3)
    plt.plot(xp3 + np.sqrt(3)/2, yp3 + 1/6,"k")
    
    p4 = np.linspace (10*np.pi/6, 12*np.pi/6)
    xp4 = 1/3*np.sin(p4)
    yp4 = 1/3*np.cos(p4)
    plt.plot(xp4 + np.sqrt(3)/2, yp4 - 5/6,"k")
    
    p5 = np.linspace (0*np.pi/6, 2*np.pi/6)
    xp5 = 1/3*np.sin(p5)
    yp5 = 1/3*np.cos(p5)
    plt.plot(xp5 - np.sqrt(3)/2, yp5 - 5/6,"k")
    
    p6 = np.linspace (6*np.pi/6, 8*np.pi/6)
    xp6 = 1/3*np.sin(p6)
    yp6 = 1/3*np.cos(p6)
    plt.plot(xp6 + np.sqrt(3)/2, yp6 + 5/6,"k")
    
    p7 = np.linspace (4*np.pi/6, 6*np.pi/6)
    xp7 = 1/3*np.sin(p7)
    yp7 = 1/3*np.cos(p7)
    plt.plot(xp7 - np.sqrt(3)/2, yp7 + 5/6,"k")
    
    p8 = np.linspace (2*np.pi/6, 4*np.pi/6)
    xp8 = 1/3*np.sin(p8)
    yp8 = 1/3*np.cos(p8)
    plt.plot(xp8 - 2*np.sqrt(3)/3, yp8 + 1/3,"k")
    
    p9 = np.linspace (2*np.pi/6, 4*np.pi/6)
    xp9 = 1/3*np.sin(p9)
    yp9 = 1/3*np.cos(p9)
    plt.plot(xp9 - 2*np.sqrt(3)/3, yp9,"k")

    q0 = np.linspace (2*np.pi/6, 4*np.pi/6)
    xq0 = 1/3*np.sin(q0)
    yq0 = 1/3*np.cos(q0)
    plt.plot(xq0 - 2*np.sqrt(3)/3, yq0 - 1/3,"k")
    
    q1 = np.linspace (8*np.pi/6, 10*np.pi/6)
    xq1 = 1/3*np.sin(q1)
    yq1 = 1/3*np.cos(q1)
    plt.plot(xq1 + 2*np.sqrt(3)/3, yq1 - 1/3,"k")
    
    q2 = np.linspace (8*np.pi/6, 10*np.pi/6)
    xq2 = 1/3*np.sin(q2)
    yq2 = 1/3*np.cos(q2)
    plt.plot(xq2 + 2*np.sqrt(3)/3, yq2 + 1/3,"k")

    q3 = np.linspace (8*np.pi/6, 10*np.pi/6)
    xq3 = 1/3*np.sin(q3)
    yq3 = 1/3*np.cos(q3)
    plt.plot(xq3 + 2*np.sqrt(3)/3, yq3,"k")
    
    plt.plot(x,y, "k")

    plt.axis('off')

    plt.savefig("flor")

vida()
