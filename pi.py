from cmath import pi, sqrt
import math

n = 3 #número de lados do poligono inicial
r = 1 #a distância entre o centro e o vértice
while True:
    Ang = 360/n
    ACmp = (180-Ang)/2 
    Ares = (math.sin(math.radians(Ang))*r)/math.sin(math.radians(ACmp))
    piT = (n*Ares)/2*r
    Aprox = math.pi/piT
    n+=1

    print("o valor atual de N é " + str(n) + " o erro aprox do Pi Teórico é " + str(Aprox) + " e o valor resultante é " + str(piT))
