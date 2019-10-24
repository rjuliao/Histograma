import cv2 as op
from matplotlib import pyplot as plt
import numpy as np

#Leer una imagen existente
def read():
    vimg = []    
    for i in range(0, 15):
        s = "images/img-"+str(i)+".jpg"    
        vimg.append(s)
    return vimg

#Genera la suma de la intensidades
def hist(i, w, h):
    
    datos = np.zeros(256, dtype = np.int)
    for j in range(w):
        for k in range(h):
            pos = i[j,k]
            datos[pos]+=1
    print(datos)
    #Regresa la suma de cada intensidad
    return datos

if __name__=="__main__":
    #Histograma
    vimg = read()
    a=0
    
    for i in vimg:
        #leo la imagen
        img = op.imread(i,op.IMREAD_GRAYSCALE)
        w, h = img.shape
        print("img: "+i+" w: "+str(w)+" h: "+str(h))
        d = hist(img, w, h)
        
        ar = np.arange(len(d))
        
        plt.bar( ar, d, color="red", alpha=0.5)
        plt.title(i)
        plt.xlabel("Gama de colores en escala de grises")
        plt.ylabel("Frencuencia")
        
        plt.savefig("images/hist-"+str(a)+".png")
        a+=1
        