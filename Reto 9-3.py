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