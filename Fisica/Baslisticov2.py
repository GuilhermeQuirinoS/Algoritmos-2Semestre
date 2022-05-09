from re import I
import numpy as np
import math

V0 = float(input("Digite a velocidade (em m/s):"))
Y0 = float(input("Digite a altura inicial(em metros)"))
Tempod = float(input("Digite o instante de tempo determinado(em segundos):"))
Angulo = float(input("Digite o ângulo de lançamento (em graus):"))

g = 9.8
angRAd = np.deg2rad(Angulo)

#1. Velocidades em T = 0:

V0y = abs(V0*(np.sin(angRAd)))
V0x = abs(V0*(np.cos(angRAd)))

#2. Tempo em que o objeto permance no ar:
TempoAR = ((V0y + (math.sqrt((V0y**2)-(4*(-g/2)*Y0)))) / (2*(g/2)))

#3. xMax

xMax = (V0x*TempoAR)

#4. hMax

hMax = Y0 + ((V0**2) * (np.sin(angRAd)**2) / (2*g))

#5. Velocidade em hMax

TempoSubida = ((V0y) / g)

VyhMax = 0
VxhMax = V0x

VthMax = math.sqrt((VyhMax**2) + (VxhMax**2))

#6. Velocidade em xMax

VyxMax = (V0y) - g*TempoAR
VxxMax = V0x

VtxMax = math.sqrt((VyxMax**2) + (VxxMax**2))

#7. Em determinado instante de tempo:
#função da velocidade

Vy = (V0y) - g*Tempod
Vx = (V0x) + 0*Tempod

V = math.sqrt((Vx**2) + (Vy**2))

#função da posição

Y = Y0 + (V0y*Tempod) - ((g*(Tempod**2))/2)
X = (V0x*Tempod)

print("=============================================================")
print("V0x: %.3f"% V0x)
print("V0y: %.3f"% V0y)
print("")
print("TempoAR: %.3f"% TempoAR)
print("xMax: %.3f"% xMax)
print("hMax: %.3f"% hMax)
print("")
print("VxhMax: %.3f"% VxhMax)
print("VyhMax: %.3f"% VyhMax)
print("VthMax: %.3f"% VthMax)
print("")
print("VxxMax: %.3f"% VxxMax)
print("VyxMax: %.3f"% VyxMax)
print("VtxMax: %.3f"% VtxMax)
print("")
print("Vx: %.3f"% Vx)
print("Vy: %.3f"% Vy)
print("V: %.3f"% V)
print("")
print("X: %.3f"% X)
print("Y: %.3f"% Y)
print("=============================================================")