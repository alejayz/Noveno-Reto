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