# Noveno-Reto


**Punto 1**

De los retos anteriores seleciones 3 funciones y escribalas en forma de lambdas.

```python
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
```

**Punto 2**

De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).

```python
#De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).
#1
def prestamo(*args) -> float:
    interes = i / 100
    return c * (1 + interes) ** n

if __name__ == "__main__":
    c = float(input("ingrese valor de préstamo en pesos: "))
    i = float(input("ingrese valor de interés en %: "))
    n = int(input("ingrese número de meses: "))
    valorPrestamo = prestamo(c, i, n)
    print("el valor del préstamo por " + str(n) + " meses es de: " + str(valorPrestamo))
    
#2
import math
def areaFigura(*args) -> float:
    aRectangulo = a * b
    aCirculos = (math.pi * (r)**2) * 2  # el área se duplica dado que son dos círculos
    return aRectangulo + aCirculos

if __name__ == "__main__":
    a = float(input("ingrese ancho del rectángulo: "))
    b = float(input("ingrese largo del rectángulo: "))
    r = float(input("ingrese el radio del círculo: ")) 
    area = areaFigura(a, b, r)
    print("el área de la figura es: " + str(area))
    
    
#3
import math 
def areaFigura(*args) -> float:
    arSupEsfera = 4 * math.pi * (r1**2)
    hipot = (h**2 + r2**2)**0.5  # formula de la hipotenusa para hallar área superficial
    arSupCono = (math.pi * r2 * hipot) + (math.pi * (r2**2))
    return arSupEsfera + arSupCono 

if __name__ == "__main__":
    r1 = float(input("ingrese el radio de la esfera: ")) # radio en cm
    r2 = float(input("ingrese el radio del cono: ")) # radio en cm
    h = float(input("ingrese la altura del cono: ")) # altura en cm
    #Volumen = VolumenFigura(r1, r2, h)
    #print("el volumen de la figura es: " + str(Volumen))
    areaSuperficial= areaFigura(r1, r2, h)
    print("el área superficial de la figura es: " + str(areaSuperficial))
```

**Punto 3**

Escriba una función recursiva para calcular la operación de la potencia.

```python
#Función recursiva para la función potencia
def potenciaRecursiva(n:int, x:int) -> int:
    if x == 0:
        return 1
    elif x == 1:
        return n
    else:
        return n * potenciaRecursiva(n, x-1)
    
if __name__ == '__main__':
    n = int(input("ingrese el número base: "))
    x = int(input("ingrese el exponente: "))
    pot = potenciaRecursiva(n, x)
    print("la potencia de " + str(n) + " elevado " + str(x) + " es: " + str(pot))
```

**Punto 4**

Utilice la siguiente plantilla de code para contar el tiempo:

```python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```
Desarrollo punto 4:

```python
#calcular fibonacci con iteración o con recursión
import timeit

def fibo(n : int )-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  start_time = timeit.default_timer()
  serieFibo = fibo(num)
  timer= timeit.default_timer() - start_time
  print(f"La serie de Fibonacci hasta {num} es {serieFibo}")
  
print(f"fibo se demoró {timer} en correr")




import timeit

def fiboRecursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fiboRecursivo(n-1)+fiboRecursivo(n-2) 


if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  start_time = timeit.default_timer()
  serieFibo = fiboRecursivo(num)
  timer= timeit.default_timer() - start_time
  print(f"La serie de Fibonacci hasta {num} es {serieFibo}")
  
print(f"fiboRecursivo se demoró {timer} en correr")
```


