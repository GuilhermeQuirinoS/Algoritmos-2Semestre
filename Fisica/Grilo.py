from re import I
import numpy as np
import math

Tempo = float(input("Tempo de queda de Chirpy(em segundos):"))
V0 = float(input("Velocidade Inicial de Milada(em m/s):"))
Y = 0;

g = 9.8

#Chirpy
Y0 = ((g*(Tempo**2))/2)

#Milada
tempoAR = (((math.sqrt(-(4*((-(g/2))*Y0))))) / (2*(g/2)))

xMax = V0 * tempoAR 

print("Distancia da base: %.4f"% xMax)