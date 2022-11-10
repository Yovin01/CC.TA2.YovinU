from cProfile import label
import matplotlib.pyplot as plt
import numpy as mat

#Codigo visto en clase
def codigo_4 (n):
    p=0
    for i in range(1, n,i*2):
        p = p+1

    for j in range(1,n,j*2):
        print("Hola")

#Graficas    
def cod_4 (n):
    # Funcion modificada
    return 2*mat.log2(n) + 1

def cod_4_5 (n):
    # Funcion Original
    return mat.log2(n) + mat.log2(mat.log2(n)) +1

n = range(1 , 100)
plt.plot(n, [cod_4(i) for i in n], label= 'Funcion inicial')
plt.plot(n, [cod_4_5(i) for i in n],label= 'Funcion modificada')
plt.axhline(1, color="black")
plt.axvline(1, color="black")
plt.xlim(1, 100)
plt.ylim(1, 25)
plt.legend(loc='lower right')
plt.show() 