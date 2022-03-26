import time
ini = time.time()

archivo = open("arreglo.txt")

def cocktailSort(a):
    n = len(a)
    cam = True
    inicio = 0
    fin = n-1
    while (cam==True):
        cam = False
        for i in range (inicio, fin):
            if (a[i] > a[i+1]) :
                a[i], a[i+1]= a[i+1], a[i]
                cam=True
        if (cam==False):
            break
        cam = False
        fin = fin-1
        for i in range(fin-1, inicio-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                cam = True
        inicio = inicio+1


fn = time.time()

#prueba
a = [8, 1, 7, 4, 9, 10, 2, 5, 3, 6]
cocktailSort(a)
print("Ordenado:")
#a
print(a)
#tiempo
print(fn-ini)
#txt
print(archivo.read())
