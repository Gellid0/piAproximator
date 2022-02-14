from cmath import pi, sqrt
import math

#n = 31531856
n = 99999999
r = 1
while True:
    Ang = 360/n
    ACmp = (180-Ang)/2
    #Ares = 2*(math.cos(math.radians(Ang/2))*r)   
    Ares = (math.sin(math.radians(Ang))*r)/math.sin(math.radians(ACmp))
    #print(str(math.cos(math.radians(Ang))) + " " + str(Ang))
    piT = (n*Ares)/2*r
    Aprox = math.pi/piT
    n+=1

    print("o valor atual de N é " + str(n) + " o erro aprox do Pi Teórico é " + str(Aprox) + " e o valor de PiT é " + str(piT))
