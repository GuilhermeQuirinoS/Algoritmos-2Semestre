import math
# Biblioteca para gerar os gráficos.

import matplotlib.pyplot
# Biblioteca para interface gráfica.

from tkinter import*
from tkinter.ttk import Combobox


# Valores passados.
tempo = [0.00, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36, 0.38, 0.40, 0.42, 0.44, 0.46, 0.48, 0.50, 0.52, 0.54, 0.56, 0.58, 0.60, 0.62, 0.64, 0.66, 0.68, 0.70, 0.72, 0.74, 0.76, 0.78, 0.80, 0.82, 0.84, 0.86, 0.88, 0.90, 0.92, 0.94, 0.96, 0.98, 1.00, 1.02, 1.04, 1.06, 1.08, 1.10, 1.12, 1.14, 1.16, 1.18, 1.20, 1.22, 1.24, 1.26, 1.28, 1.30, 1.32, 1.34, 1.36, 1.38, 1.40, 1.42, 1.44, 1.46, 1.48, 1.50, 1.52, 1.54, 1.56, 1.58,1.60, 1.62, 1.64, 1.66, 1.68, 1.70, 1.72, 1.74, 1.76, 1.78, 1.80, 1.82, 1.84, 1.86, 1.88, 1.90, 1.92, 1.94, 1.96, 1.98, 2.00, 2.02, 2.04, 2.06, 2.08, 2.10, 2.12, 2.14, 2.16, 2.18, 2.20, 2.22, 2.24, 2.26, 2.28, 2.30, 2.32, 2.34, 2.36, 2.38, 2.40, 2.42, 2.44, 2.46, 2.48, 2.50, 2.52, 2.54, 2.56, 2.58, 2.60, 2.62, 2.64, 2.66, 2.68, 2.70, 2.72, 2.74, 2.76, 2.78, 2.80, 2.82, 2.84, 2.86, 2.88, 2.90, 2.92, 2.94, 2.96, 2.98, 3.00, 3.02, 3.04, 3.06, 3.08, 3.10, 3.12, 3.14, 3.16,3.18, 3.20, 3.22, 3.24, 3.26, 3.28, 3.30, 3.32, 3.34, 3.36, 3.38, 3.40, 3.42, 3.44, 3.46, 3.48, 3.50, 3.52, 3.54, 3.56, 3.58, 3.60, 3.62, 3.64, 3.66, 3.68, 3.70, 3.72, 3.74, 3.76, 3.78, 3.80, 3.82, 3.84, 3.86, 3.88, 3.90, 3.92, 3.94, 3.96, 3.98, 4.00, 4.02, 4.04, 4.06, 4.08, 4.10, 4.12, 4.14, 4.16, 4.18, 4.20, 4.22, 4.24, 4.26, 4.28, 4.30, 4.32, 4.34, 4.36, 4.38, 4.40, 4.42, 4.44, 4.46, 4.48, 4.50, 4.52, 4.54, 4.56, 4.58, 4.60, 4.62, 4.64, 4.66, 4.68, 4.70, 4.72, 4.74,4.76, 4.78, 4.80, 4.82, 4.84, 4.86, 4.88, 4.90, 4.92, 4.94, 4.96, 4.98, 5.00, 5.02, 5.04, 5.06, 5.08, 5.10, 5.12, 5.14, 5.16, 5.18, 5.20, 5.22, 5.24, 5.26, 5.28, 5.30, 5.32, 5.34, 5.36, 5.38, 5.40, 5.42, 5.44, 5.46, 5.48, 5.50, 5.52, 5.54, 5.56, 5.58, 5.60, 5.62, 5.64, 5.66, 5.68, 5.70, 5.72, 5.74, 5.76, 5.78, 5.80, 5.82, 5.84, 5.86, 5.88, 5.90, 5.92, 5.94, 5.96, 5.98, 6.00, 6.02, 6.04, 6.06, 6.08, 6.10, 6.12, 6.14, 6.16, 6.18, 6.20, 6.22, 6.24, 6.26, 6.28, 6.30, 6.32,6.34, 6.36, 6.38, 6.40, 6.42, 6.44, 6.46, 6.48, 6.50, 6.52, 6.54, 6.56, 6.58, 6.60, 6.62, 6.64, 6.66, 6.68, 6.70, 6.72, 6.74, 6.76, 6.78, 6.80, 6.82, 6.84, 6.86, 6.88, 6.90, 6.92, 6.94, 6.96, 6.98, 7.00, 7.02, 7.04, 7.06, 7.08, 7.10, 7.12, 7.14, 7.16, 7.18, 7.20, 7.22, 7.24, 7.26, 7.28, 7.30, 7.32, 7.34, 7.36, 7.38, 7.40, 7.42, 7.44, 7.46, 7.48, 7.50, 7.52, 7.54, 7.56, 7.58, 7.60, 7.62, 7.64, 7.66, 7.68, 7.70, 7.72, 7.74, 7.76, 7.78, 7.80, 7.82, 7.84, 7.86, 7.88, 7.90,7.92, 7.94, 7.96, 7.98, 8.00, 8.02, 8.04, 8.06, 8.08, 8.10, 8.12, 8.14, 8.16, 8.18, 8.20, 8.22, 8.24, 8.26, 8.28, 8.30, 8.32, 8.34, 8.36, 8.38, 8.40, 8.42, 8.44, 8.46, 8.48, 8.50, 8.52, 8.54, 8.56, 8.58, 8.60, 8.62, 8.64, 8.66, 8.68, 8.70, 8.72, 8.74, 8.76, 8.78, 8.80, 8.82, 8.84, 8.86, 8.88, 8.90, 8.92, 8.94, 8.96, 8.98, 9.00, 9.02, 9.04, 9.06, 9.08, 9.10, 9.12, 9.14, 9.16, 9.18, 9.20, 9.22, 9.24, 9.26, 9.28, 9.30, 9.32, 9.34, 9.36, 9.38, 9.40, 9.42, 9.44, 9.46, 9.48,9.50, 9.52, 9.54, 9.56, 9.58, 9.60, 9.62, 9.64, 9.66, 9.68, 9.70, 9.72, 9.74, 9.76, 9.78, 9.80, 9.82, 9.84, 9.86, 9.88, 9.90, 9.92, 9.94, 9.96, 9.98, 10.00, 10.02, 10.04, 10.06, 10.08, 10.10, 10.12, 10.14, 10.16, 10.18, 10.20, 10.22, 10.24, 10.26, 10.28, 10.30, 10.32, 10.34, 10.36, 10.38, 10.40, 10.42, 10.44, 10.46, 10.48, 10.50, 10.52, 10.54, 10.56, 10.58, 10.60, 10.62, 10.64, 10.66, 10.68, 10.70, 10.72, 10.74, 10.76, 10.78, 10.80, 10.82, 10.84, 10.86, 10.88, 10.90, 10.92, 10.94, 10.96, 10.98, 11.00, 11.02, 11.04, 11.06, 11.08, 11.10, 11.12, 11.14, 11.16, 11.18, 11.20, 11.22, 11.24, 11.26, 11.28, 11.30, 11.32, 11.34, 11.36, 11.38, 11.40, 11.42, 11.44, 11.46, 11.48, 11.50, 11.52, 11.54, 11.56, 11.58, 11.60, 11.62, 11.64, 11.66, 11.68, 11.70, 11.72, 11.74, 11.76, 11.78, 11.80, 11.82, 11.84, 11.86, 11.88, 11.90, 11.92, 11.94, 11.96, 11.98, 12.00, 12.02, 12.04, 12.06, 12.08, 12.10, 12.12, 12.14, 12.16, 12.18, 12.20, 12.22, 12.24, 12.26,12.28, 12.30, 12.32, 12.34, 12.36, 12.38, 12.40, 12.42, 12.44, 12.46, 12.48, 12.50, 12.52, 12.54, 12.56, 12.58, 12.60, 12.62, 12.64, 12.66, 12.68, 12.70, 12.72, 12.74, 12.76, 12.78, 12.80, 12.82, 12.84, 12.86, 12.88, 12.90, 12.92, 12.94, 12.96, 12.98, 13.00, 13.02, 13.04, 13.06, 13.08, 13.10, 13.12, 13.14, 13.16, 13.18, 13.20, 13.22, 13.24, 13.26, 13.28, 13.30, 13.32, 13.34, 13.36, 13.38, 13.40, 13.42, 13.44, 13.46, 13.48, 13.50, 13.52, 13.54, 13.56, 13.58, 13.60, 13.62, 13.64, 13.66, 13.68, 13.70, 13.72, 13.74, 13.76, 13.78, 13.80, 13.82, 13.84, 13.86, 13.88, 13.90, 13.92, 13.94, 13.96, 13.98, 14.00, 14.02, 14.04, 14.06, 14.08, 14.10, 14.12, 14.14, 14.16, 14.18, 14.20, 14.22, 14.24, 14.26, 14.28, 14.30, 14.32, 14.34, 14.36, 14.38, 14.40, 14.42, 14.44, 14.46, 14.48, 14.50, 14.52, 14.54, 14.56, 14.58, 14.60, 14.62, 14.64, 14.66, 14.68, 14.70, 14.72, 14.74, 14.76, 14.78, 14.80, 14.82, 14.84, 14.86, 14.88, 14.90, 14.92, 14.94, 14.96, 14.98, 15.00, 15.02, 15.04, 15.06, 15.08, 15.10, 15.12, 15.14, 15.16, 15.18, 15.20, 15.22, 15.24, 15.26, 15.28, 15.30, 15.32, 15.34, 15.36, 15.38, 15.40, 15.42,15.44, 15.46, 15.48, 15.50, 15.52, 15.54, 15.56, 15.58, 15.60, 15.62, 15.64, 15.66, 15.68, 15.70, 15.72, 15.74, 15.76, 15.78, 15.80, 15.82, 15.84, 15.86, 15.88, 15.90, 15.92, 15.94, 15.96, 15.98, 16.00, 16.02, 16.04, 16.06, 16.08, 16.10, 16.12, 16.14, 16.16, 16.18, 16.20, 16.22, 16.24, 16.26, 16.28, 16.30, 16.32, 16.34, 16.36, 16.38, 16.40, 16.42, 16.44, 16.46, 16.48, 16.50, 16.52, 16.54, 16.56, 16.58, 16.60, 16.62, 16.64, 16.66, 16.68, 16.70, 16.72, 16.74, 16.76, 16.78, 16.80, 16.82, 16.84, 16.86, 16.88, 16.90, 16.92, 16.94, 16.96, 16.98, 17.00, 17.02, 17.04, 17.06, 17.08, 17.10, 17.12, 17.14, 17.16, 17.18, 17.20, 17.22, 17.24, 17.26, 17.28, 17.30, 17.32, 17.34, 17.36, 17.38, 17.40, 17.42, 17.44, 17.46, 17.48, 17.50, 17.52, 17.54, 17.56, 17.58, 17.60, 17.62, 17.64, 17.66, 17.68, 17.70, 17.72, 17.74, 17.76, 17.78, 17.80, 17.82, 17.84, 17.86, 17.88, 17.90, 17.92, 17.94, 17.96, 17.98, 18.00, 18.02, 18.04, 18.06, 18.08, 18.10, 18.12, 18.14, 18.16, 18.18, 18.20, 18.22, 18.24, 18.26, 18.28, 18.30, 18.32, 18.34, 18.36, 18.38, 18.40, 18.42, 18.44, 18.46, 18.48, 18.50, 18.52, 18.54, 18.56, 18.58,18.60, 18.62, 18.64, 18.66, 18.68, 18.70, 18.72, 18.74, 18.76, 18.78, 18.80, 18.82, 18.84, 18.86, 18.88, 18.90, 18.92, 18.94, 18.96, 18.98, 19.00, 19.02, 19.04, 19.06, 19.08, 19.10, 19.12, 19.14, 19.16, 19.18, 19.20, 19.22, 19.24, 19.26, 19.28, 19.30, 19.32, 19.34, 19.36, 19.38, 19.40, 19.42, 19.44, 19.46, 19.48, 19.50, 19.52, 19.54, 19.56, 19.8, 19.60, 19.62, 19.64, 19.66, 19.68, 19.70, 19.72, 19.74, 19.76, 19.78, 19.80, 19.82, 19.84, 19.86, 19.88, 19.90, 19.92, 19.94, 19.96, 19.98, 20.00]

bolaX = []

bolaY = [0.5,	0.51599, 0.53195,	0.54789,	0.56381,	0.5797,	0.59557,	0.61141,	0.62723,	0.64303,	0.6588,	0.67455,	0.69027,	0.70597,	0.72165,	0.7373,	0.75293,	0.76853,	0.78411,	0.79967,	0.8152,	0.83071,	0.84619,	0.86165,	0.87709,	0.8925,	0.90789,	0.92325,	0.93859,	0.95391,	0.9692,	0.98447,	0.99971,	1.01493, 1.03013,	1.0453,	1.06045,	1.07557	,1.09067, 1.10575,	1.1208,	1.13583,	1.15083,	1.16581,	1.18077,	1.1957,	1.21061,	1.22549,	1.24035,	1.25519,	1.27,	1.28479,	1.29955,	1.31429,	1.32901,	1.3437,	1.35837,	1.37301,	1.38763,	1.40223,	1.4168,	1.43135,	1.44587,	1.46037,	1.47485,	1.4893,	1.50373,	1.51813,	1.53251,	1.54687,	1.5612,	1.57551,	1.58979,	1.60405,	1.61829,	1.6325,	1.64669,	1.66085,	1.67499,	1.68911,	1.7032,	1.71727,	1.73131,	1.74533,	1.75933,	1.7733,	1.78725,	1.80117,	1.81507,	1.82895,	1.8428,	1.85663,	1.87043,	1.88421,	1.89797,	1.9117,	1.92541,	1.93909,	1.95275,	1.96639,	1.98,	1.99359,	2.00715,	2.02069,	2.03421,	2.0477,	2.06117,	2.07461,	2.08803, 2.10143,	2.1148,	2.12815,	2.14147,	2.15477,	2.16805, 2.1813,	2.19453, 2.20773,	2.22091,	2.23407,	2.2472,	2.26031,	2.27339,	2.28645,	2.29949,	2.3125,	2.32549,	2.33845,	2.35139,	2.36431,	2.3772,	2.39007,	2.40291,	2.41573,	2.42853,	2.4413,	2.45405,	2.46677,	2.47947,	2.49215,	2.5048,	2.51743,	2.53003,	2.54261,	2.55517,	2.5677,	2.58021,	2.59269,	2.60515,	2.61759,	2.63,	2.64239,	2.65475,	2.66709,	2.67941,	2.6917,	2.70397,	2.71621,	2.72843,	2.74063,	2.7528,	2.76495,	2.77707,	2.78917,	2.80125,	2.8133,	2.82533,	2.83733,	2.84931,	2.86127,	2.8732,	2.88511,	2.89699,	2.90885,	2.92069,	2.9325,	2.94429,	2.95605, 2.96779,	2.97951,	2.9912,	3.00287,	3.01451,	3.02613,	3.03773,	3.0493,	3.06085,	3.07237,	3.08387,	3.09535,	3.1068,	3.11823,	3.12963,	3.14101,	3.15237,	3.1637,	3.17501,	3.18629,	3.19755,	3.20879,	3.22, 3.23119,	3.24235,	3.25349,	3.26461,	3.2757,	3.28677,	3.29781,	3.30883,	3.31983,	3.3308,	3.34175,	3.35267,	3.36357,	3.37445,	3.3853,	3.39613,	3.40693,	3.41771,	3.42847,	3.4392,	3.44991,	3.46059, 3.47125,	3.48189,	3.4925,	3.50309,	3.51365,	3.52419,	3.53471,	3.5452, 3.55567,	3.56611,	3.57653,	3.58693,	3.5973,	3.60765,	3.61797,	3.62827,	3.63855,	3.6488,	3.65903,	3.66923,	3.67941,	3.68957,	3.6997,	3.70981,	3.71989,	3.72995,	3.73999,	3.75, 3.75999,	3.76995,	3.77989,	3.78981,	3.7997,	3.80957, 3.81941,	3.82923,	3.83903, 3.8488,	3.85855,	3.86827,	3.87797,	3.88765, 3.8973,	3.90693,	3.91653,	3.92611,	3.93567,	3.9452,	3.95471, 3.96419,	3.97365,	3.98309,	3.9925,	4.00189	,4.01125,	4.02059,	4.02991,	4.0392,	4.04847,	4.05771,	4.06693,	4.07613,	4.0853,	4.09445,	4.10357,	4.11267,	4.12175,	4.1308,	4.13983,	4.14883,	4.15781,	4.16677,	4.1757,	4.18461,	4.19349,	4.20235,	4.21119,	4.22,	4.22879,	4.23755,	4.24629,	4.25501,	4.2637,	4.27237,	4.28101,	4.28963,	4.29823,	4.3068,	4.31535,	4.32387, 4.33237,	4.34085,	4.3493,	4.35773,	4.36613,	4.37451,	4.38287,	4.3912,	4.39951,	4.40779,	4.41605,	4.42429,	4.4325,	4.44069,	4.44885,	4.45699,	4.46511,	4.4732,	4.48127,	4.48931,	4.49733,	4.50533,	4.5133,	4.52125,	4.52917,	4.53707,	4.54495,	4.5528,	4.56063,	4.56843,	4.57621,	4.58397,	4.5917,	4.59941,	4.60709,	4.61475,	4.62239,	4.63,	4.63759,	4.64515,	4.65269, 4.66021,	4.6677,	4.67517,	4.68261,	4.69003,	4.69743,	4.7048,	4.71215,	4.71947,	4.72677,	4.73405,	4.7413,	4.74853,	4.75573,	4.76291,	4.77007,	4.7772,	4.78431,	4.79139,	4.79845,	4.80549,	4.8125,	4.81949,	4.82645,	4.83339,	4.84031,	4.8472,	4.85407,	4.86091,	4.86773,	4.87453,	4.8813,	4.88805,	4.89477,	4.90147,	4.90815,	4.9148,	4.92143,	4.92803,	4.93461,	4.94117,	4.9477,	4.95421, 4.96069,	4.96715,	4.97359,	4.98,	4.98639,	4.99275,	4.99909,	5.00541,	5.0117,	5.01797,	5.02421,	5.03043,	5.03663,	5.0428,	5.04895,	5.05507,	5.06117,	5.06725,	5.0733,	5.07933,	5.08533,	5.09131,	5.09727,	5.1032,	5.10911,	5.11499,	5.12085,	5.12669, 5.1325,	5.13829,	5.14405,	5.14979,	5.15551,	5.1612,	5.16687, 5.17251,	5.17813,	5.18373,	5.1893,	5.19485,	5.20037,	5.20587,	5.21135,	5.2168,	5.22223,	5.22763,	5.23301,	5.23837,	5.2437,	5.24901,	5.25429,	5.25955,	5.26479,	5.27,	5.27519,	5.28035,	5.28549	,5.29061,	5.2957,	5.30077,5.30581,	5.31083,	5.31583,	5.3208,	5.32575,	5.33067,	5.33557,	5.34045,	5.3453,	5.35013,	5.35493,	5.35971,	5.36447]



tempoInterceptado  =  [ ] 
#robô
roboX  =  []
roboY  =  []
rVelocidadeX  =  [2] 
rVelocidadeY  =  [1] 
rAceleracaoX  =  [1] 
rAceleracaoY  =  [0.5] 
#bola
bolaInterceptadaX  =  [ ]
bolaInterceptadaY  =  [ ]
bVelInterceX  =  [ ]
bVelInterceY  =  [ ] 
bAcelIntercX  =  [ ] 
bAcelIntercY  =  [ ] 

cos  =  0 
sen  =  0
aceleracao  =  0.32  
raio  =  8.0
i = 0.0
float(i)

roboRx  =  [ ]
roboRy  =  [ ]
andamento = [0]

rx = 0
ry = 0
bolaBx = 0
bolaBy= 0
distRoboBolatotal = [0]
posroboX = 0
posroboY= 0

# variaveis para gerar gráficos.
groboRx = []
groboRy = []
gbolaBx = []
gbolaBy = []
gTempo = []
gdistancia = []
gveloRoboX = []
gveloRoboy = []
gacelacaoX = []
gacelacaoy = []
gacelacaoBolaX = []
gacelacaoBolay = []
gveloBolax = []
gveloBolay= []


aceleracaoBolax = []
aceleracaoBolay = []

velovidaddeBolax = []
velovidaddeBolay = []

velovidaddeBolax2 = []
velovidaddeBolay2 = []
# variaveis para interface gráfica.
dist1 = []
tempo1 = []
distTotal1 = []
posroboX1 = []
posroboy1 = []
posBolax = []
posBolay = []

# interface gráfica
janela = Tk()
janela.title('Projeto Ora Bolas')

rotulo = Label(janela, text='Dados sobre a interceptação', font=('Arial Bold', 12))
rotulo.place(relx = 0.5, rely = 0.05, anchor = CENTER)

Robox = Label(janela, text='Posição do robo em x: ', font =('Arial Bold', 12))
Robox.place(relx = 0.2, rely= 0.1, anchor = 'center')
#pegar os valores de X.
Robox2 = Entry(janela, width = 16, font=('Arial Bold', 12))
Robox2.place(relx = 0.5, rely = 0.1, anchor = CENTER)

Roboy = Label(janela, text='Posição do robo em y: ', font =('Arial Bold', 12))
Roboy.place(relx = 0.2, rely= 0.17, anchor = 'center')
#pegar os valores de Y.
Roboy2 = Entry(janela, width = 16, font=('Arial Bold', 12))
Roboy2.place(relx = 0.5, rely = 0.17, anchor = CENTER)

i = 0
j = 0
def andaRobo ():
        global j
        if(j == 0):
          #salvar as posições de X e Y.
          posroboX = float(Robox2.get()) 
          posroboY = float(Roboy2.get())

          roboX.insert(0, posroboX)
          roboY.insert(0, posroboY)
        tamBolax = len(bolaX)
        j = 1
        global i 
        while( i < tamBolax):
          #para achar a velocidade da bola, para isso usamos a função Velocidade escalar média, deltaS/deltaT.
          velovidaddeBolax.insert(i, (bolaX[i+1] - bolaX[i])/(tempo[i+1] - tempo[i]))
          velovidaddeBolay.insert(i, (bolaY[i+1] - bolaY[i])/(tempo[i+1] - tempo[i]))

          velovidaddeBolax2.insert(i, (bolaX[i+2] - bolaX[i+1])/(tempo[i+2] - tempo[i+1]))
          velovidaddeBolay2.insert(i, (bolaY[i+2] - bolaY[i+1])/(tempo[i+2] - tempo[i+1]))
          
          # achar a aceleração da bola usamos a função de Aceleração Média de um Móvel, deltaV/deltaT.
          aceleracaoBolax.insert(i, (velovidaddeBolax2[i] - velovidaddeBolax[i])/(tempo[i+1] - tempo[i]))
          aceleracaoBolay.insert(i, (velovidaddeBolay2[i] - velovidaddeBolay[i])/(tempo[i+1] - tempo[i]))

          #calcular a distancia do robo e da bola, usamos a função de distancia entre dois pontos.
          distRoboBolatotal.insert(i,(math.sqrt ( math.pow ( ( bolaX[i]-roboX[i]),2)+math.pow((bolaY[i]-roboY[i]),2))))
          if(distRoboBolatotal[i] == 0):
            print("a distancia do robô e da bola é igual a 0, ou seja, o robo ja está do lado da bola")
            break
          # calcular o seno e o cosseno.
          cos = (bolaX[i]-roboX[i])/distRoboBolatotal[i] 
          
          sen  =  ( bolaY[i]-roboY[i])/distRoboBolatotal[i] 

          if ( tempo[i] <= 2.0 ):
            #decompondo o vetor aceleração de X e Y. 
            rAceleracaoX.insert(i, aceleracao * cos )
            rAceleracaoY.insert(i, aceleracao * sen )
            
            # achando a velocidade até 2s com v = v + a * t. 
            rVelocidadeX.insert(i+1, rVelocidadeX [ i ]  +  ( rAceleracaoX [ i ] * tempo [ i ] ) )
            # utilizando função horária da posição em função do tempo pois o movimento eh uniformemente variado até 2s s = s0 + v0 + 0,5at²
            rVelocidadeY.insert(i+1, rVelocidadeY [ i ]  +  ( rAceleracaoY [ i ] * tempo [ i ] ) )
            roboX.insert(i+1, roboX [ i ]  +  ( rVelocidadeX[i]*tempo[i]) + (0.5 *(rAceleracaoX[i]*(tempo[i]*tempo[i]))))
            roboY.insert(i+1,roboY [ i ]  +  ( rVelocidadeY [ i ] * tempo [ i ] )  +  ( 0.5 * ( rAceleracaoY [ i ] * ( tempo [ i ] * tempo [ i ] ) ) ) )
          else:
            #depois que o robo atingir a velocidade máxima em 2s o movimento passa a ser uniforme	entao s = s0 + v * deltaT
            # decompondo a velocidade constante (2.0) em x e  (1.0) y
            rVelocidadeX[i]= 2.0 * cos
            rVelocidadeY[i] = 1.0 * sen 
            
            # usando na função horaria de deslocamento
            roboX.insert(i+1,roboX[i]+(rVelocidadeX[i]* 0.02)) 
            roboY.insert(i+1,roboY [ i ]  +  ( rVelocidadeY [ i ] * 0.02 ))

          #variáveis para gerar gráficos.
          gTempo.insert(i, tempo[i])
          groboRx.insert(i, roboX[i])
          groboRy.insert(i, roboY[i])  
          gbolaBx.insert(i, bolaX[i])       
          gbolaBy.insert(i, bolaY[i])
          gdistancia.insert(i, distRoboBolatotal[i])
          gveloRoboX.insert(i, rVelocidadeX[i])
          gveloRoboy.insert(i, rVelocidadeY[i])
          gacelacaoX.insert(i, rAceleracaoX[i])
          gacelacaoy.insert(i, rAceleracaoY[i])
          gacelacaoBolaX.insert(i,  aceleracaoBolax[i])
          gacelacaoBolay.insert(i,  aceleracaoBolay[i])
          gveloBolax.insert(i, velovidaddeBolax[i])
          gveloBolay.insert(i, velovidaddeBolay[i])

          i = i + 1
          # A distancia do robo está igual ao raio.
          if( distRoboBolatotal[i-1] >= raio):
            # Variáveis para interface gráfica.
            dist1.insert(0, distRoboBolatotal[0])
            tempo1.insert(0, tempo[i-1])
            distTotal1.insert(0, distRoboBolatotal[i-1])
            posroboX1.insert(0, abs(roboX[i-1])) 
            posroboy1.insert(0, abs(roboY[i-1]))
            posBolax.insert(0, bolaX[i-1])
            posBolay.insert(0,bolaY[i-1] )
            # apenas para segurança, Se a interface gráfica ocorrer algum problema.
            print("Distancia inicial da bola e do robo: ",distRoboBolatotal[0])
            print("Momento da intercptação, tempo =", tempo[i-1])
            print('distancia da bola no momento da interceptação: %.4f' % distRoboBolatotal[i-1])
            print('posição do robo em x no momento da interceptação: %.4f'% abs(roboX[i-1]))
            print('posição do bola em x: %.4f' % bolaX[i-1])
            print('posição da bola em y :%.4f'% bolaY[i-1])
            print('posição do robo em y no momento da interceptação: %.4f'% abs(roboY[i-1]))
            break

# Funções que geram os gráficos.
def geraGraficoBolay( bolaY, tempo):
  matplotlib.pyplot.title('trajetória bola Y')
  matplotlib.pyplot.xlabel('POSIÇÃO EM Y')
  matplotlib.pyplot.ylabel('TEMPO')

  matplotlib.pyplot.plot(bolaY, tempo)

  matplotlib.pyplot.show()


def geraGraficoDistancia(gTempo, gdistancia):
  #distancia do robo e da bola.
  matplotlib.pyplot.title('distancia do robo e da bola até o momento da interceptação')
  matplotlib.pyplot.xlabel('distancia')
  matplotlib.pyplot.ylabel('TEMPO')

  matplotlib.pyplot.plot(gdistancia, gTempo)

  matplotlib.pyplot.show()

def geraGraficoposicao(gbolaBx,gbolaBy,groboRx,groboRy):
  # esse grafico marca o instante da interceptação, sobre o tempo 
  matplotlib.pyplot.title('coordenadas do robo e da bola até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = Posição do robo Laranja = Posição da bola')
  #posição em x.
  matplotlib.pyplot.plot(groboRx, groboRy)
  #posição em y.
  matplotlib.pyplot.plot(gbolaBx, gbolaBy)
  matplotlib.pyplot.show()

def geraGraficoposicaoTempo(gbolaBx,gbolaBy,groboRx,groboRy, gTempo):
  #distancia do robo e da bola.
  matplotlib.pyplot.title('trajetória do robo e da bola até o momento da interceptação \n em função do tempo')

  matplotlib.pyplot.xlabel('Azul = robo em x  Lar = robo em y  Verd = bola em x verm = bola em y')

#posição do robo
  matplotlib.pyplot.plot(groboRx, gTempo)
  matplotlib.pyplot.plot(groboRy, gTempo)
#posição da bola
  matplotlib.pyplot.plot(gbolaBx, gTempo)
  matplotlib.pyplot.plot(gbolaBy, gTempo)

  matplotlib.pyplot.show()


def geraGraficoVelo(gveloRoboX, gveloRoboy, gTempo):
  #velocidade do robo.
  matplotlib.pyplot.title('velocidade do robo até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = velocidade do robo em x  Laranja = velocidade do robo em y ')


  matplotlib.pyplot.plot(gveloRoboX, gTempo)
  matplotlib.pyplot.plot(gveloRoboy, gTempo)
  matplotlib.pyplot.show()

def geraGraficoVeloBola(gveloBolax, gveloBolay, gTempo):
  #velocidade do robo.
  matplotlib.pyplot.title('velocidade da bola até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = velocidade da bola em x  Laranja = velocidade da bola em y ')


  matplotlib.pyplot.plot(gveloBolax, gTempo)
  matplotlib.pyplot.plot(gveloBolay, gTempo)
  matplotlib.pyplot.show()

def geraGraficoAceleracaoRobo(gacelacaoX, gacelacaoy, gTempo):
  #aceleração.
  matplotlib.pyplot.title('aceleração do robo até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = aceleração do robo em x  Laranja = aceleração do robo em y ')
  matplotlib.pyplot.plot(gacelacaoX, gTempo)
  matplotlib.pyplot.plot(gacelacaoy, gTempo)




  matplotlib.pyplot.show()

def geraGraficoAceleracaoBola(gacelacaoBolaX, gacelacaoBolay, gTempo):
  #aceleração.
  matplotlib.pyplot.title('aceleração da bola até o momento da interceptação')
  matplotlib.pyplot.xlabel('Azul = aceleração da bola em x  Laranja = aceleração da bola em y ')


  matplotlib.pyplot.plot(gacelacaoBolaX, gTempo)
  matplotlib.pyplot.plot(gacelacaoBolay, gTempo)

  matplotlib.pyplot.show()


geraGraficoVelo(gveloRoboX, gveloRoboy, gTempo)
geraGraficoVeloBola(gveloBolax, gveloBolay, gTempo)
geraGraficoposicaoTempo(gbolaBx,gbolaBy,groboRx,groboRy, gTempo)
geraGraficoposicao(gbolaBx,gbolaBy,groboRx,groboRy)
geraGraficoDistancia(gTempo, gdistancia)
geraGraficoAceleracaoRobo(gacelacaoX, gacelacaoy, gTempo)
geraGraficoAceleracaoBola(gacelacaoBolaX, gacelacaoBolay, gTempo)