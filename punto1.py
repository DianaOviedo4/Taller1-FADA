
import math
import time 

def calculaLog(n):
    inicio = time.strftime("%S", time.gmtime()) # captura el segundo actual
    i = 1
    while(int(inicio) == int(time.strftime("%S", time.gmtime()))):
        
        math.log10(n)
        i = i+1
    return print(i)

def calculaRaiz(n):
    inicio = time.strftime("%S", time.gmtime()) 
    i = 1
    while(int(inicio) == int(time.strftime("%S", time.gmtime()))):
        math.sqrt(n)
        i = i + 1
    print(i)

def calculaPorLog(n):
    print(n * math.log10(n))

def calculaCuadrado(n):
    print(n*n)

def calculaCubo(n):
    print(math.pow(n, 3))

def calculaBase2(n):
    print(math.pow(2, n))

def calculaFactorial(n):
    inicio = time.strftime("%S", time.gmtime()) # captura el segundo actual
    i = 1
    while(int(inicio) == int(time.strftime("%S", time.gmtime()))):
        math.factorial(n)
        i = i + 1
    print(i)
