from re import I
import numpy as np
import math

# inputs = velocidade em m/s (V0)
#         angulo do lancamento em graus
# outputs = distancia percorrida (alcance)
#             altura maxima
#             duracao do lancamento
def recebe():
	while True:
		if iV0 <= 0:
			print("Valor Invalido")

		elif iAngulo < 0 or iAngulo > 90:
			print("Valor Invalido")

		elif iTempod < 0:
			print("Valor Invalido")

		elif iY0 < 0:
			print("Valor Invalido")
			break


recebe()

iV0 = int(input("Digite a velocidade (em m/s):"))
iY0 = int(input("Digite a altura inicial(em metros)"))
iTempod = int(input("Digite o instante de tempo determinado(em segundos):"))
iAngulo = int(input("Digite o ângulo de lançamento (em graus):"))


angRAd = np.deg2rad(iAngulo)
g = 9.8
# X final
alcanceMax = (((iV0**2) * np.sin(2*angRAd)) / g)
# h max
alturaMax = ((iV0**2) * (np.sin(angRAd)**2) / (2*g))
# t até hmax
tempoSubida = (((iV0 * np.sin(angRAd)) / g))
# t total
tempoAR = 2*((iV0 * np.sin(angRAd)) / g)

t = np.arange(0, tempoAR, 0.1)

# todas as posições x e y menos quando y = 0
x = abs(iV0) * np.cos(angRAd) * t
y = (abs(iV0) * np.sin(angRAd) * t) - ((g*(t**2))/2)


print("\n\n\n***********")
print("Distância percorrida:", alcanceMax, "metros")
print("Altura máxima:", alturaMax, "metros")
print("Tempo quando atinge Hmax:", tempoSubida, "segundos")
print("Tempo no AR:", tempoAR, "segundos")
print("")
print("Valor de X:", x, "metros")
print("Valor de Y:", y, "metros")
print("***********")
