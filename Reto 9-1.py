#De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
#1
if __name__ == "__main__":
  N = int(input("Ingrese cantidad de gallinas: "))
  M = int(input("ingrese cantidad de gallos: "))
  K = int(input("ingrese cantidad de pollitos: "))
  carneAvesTotal = (lambda x, y, z: (x*6)+(y*7)+(z*1))(K,M,N)
  print("la cantidad de carne de aves es de " + str(carneAvesTotal) + "Kg")


#2
if __name__ == "__main__":
    P = int(input("ingrese cantidad de panes: "))
    M = int(input("ingrese cantidad de bolsas de leche: "))
    H = int(input("ingrese cantidad de huevos: "))
    B = float(input("ingrese un valor en pesos: "))
    cuentaTotal = (lambda a, b, c, d: d - ((a*300)+(b*3300)+(c*350)))(P, M, H, B)
    print("las vueltas o lo que quedo debiendo son: " + str(cuentaTotal) + " pesos")


#3
import math
if __name__ == "__main__":
    a = float(input("ingrese ancho del rectángulo: "))
    b = float(input("ingrese largo del rectángulo: "))
    r = float(input("ingrese el radio del círculo: ")) 
    perimetro = (lambda x,y,z : ((x*2)+(y*2))+(math.pi*(2*z)*2))(a, b, r)
    print("el perímertro de la figura es: " + str(perimetro))