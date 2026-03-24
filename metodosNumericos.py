import numpy as np
import sympy as sp

def biseccion(a, b, i, epsilon, redondeo):

    def f(x):
        return np.exp(x) + x - 2

    def xmf(a, b):
        return (a + b) / 2
    xa = 0
    for i in range(1, i):
        print("Iteracion " + str(i))
        print("a = " + str(round(a, redondeo)) + ",b = " + str(round(b,redondeo)))
        print("f(a) = " + str(round(f(a), redondeo)))
        print("f(b) = " + str(round(f(b), redondeo)))
        xm = xmf(a, b)
        print("xm" + str(round(xm, redondeo)))
        #Evaluacion de cambio de signos
        if f(a)*f(xm) < 0:
            b = xm
        elif f(b)*f(xm) < 0:
            a = xm
        else:
            print("La raiz es xm (no hay cambio de signos)")
            break
        print("f(xm) = " + str(round(f(xm), redondeo)))
        error = abs(xm -xa)
        print("error = " + str(round(error, redondeo)))
        xa = xm
        if error < epsilon:
            break
    print("La raiz aproximada de xm es " + str(round(xm, redondeo)))

#def reglaFalsa():

#utilizando una funcion aln(x) + bx + c = 0
def puntoFijo(a, b, c, i, resultado):
    
    if i == 0:
        return resultado

    resultado = -(c + a*np.log(resultado))/b
    print("Iteracion " + str(i) + ": " + str(resultado))
    return puntoFijo(a, b, c, i - 1, resultado)
    
def newtonRaphson():

    x = sp.symbols('x')

    fString = input("Ingresa la funcion: ")
    f = sp.sympify(fString)

    if isinstance(f, (list, tuple)):
        f = f[0]

    derivada = sp.diff(f, x)

    n = x - (f/derivada)
    
    iteraciones = int(input("Ingresa el numero de iteraciones: "))
    epsilon = float(input("Ingrese epsilon: "))
    punto = int(input("Ingresa el punto X0: "))

    def newtonRecursivo(n, iteraciones, i, punto, epsilon, error):
        
        

        puntoi = n.subs(x, punto).evalf()
        error = np.abs(puntoi - punto)

        print("Iteracion: " + str(i - iteraciones + 2) + "| valor: " + str(round(puntoi,8)) + "| error: " + str(round(error,8)))

        if iteraciones == 0 or error <= epsilon:
            return 
        
        return newtonRecursivo(n, iteraciones - 1, i, puntoi, epsilon, error)

    print("Iteracion: 0 | valor: " + str(punto) + "| error: -")
    newtonRecursivo(n, iteraciones, iteraciones - 1, punto, epsilon, 1.0)



def lin(i, grados, iteraciones):


    if i == 0:
        return

    if i == iteraciones:
        b1 = b2 = 0
        p0 = q0 = 0

    if i == iteraciones - 1:
        bi = 0


def polinomioLagrange():

    x = sp.symbols('x')


opcion = 0
while(opcion != 3):

    print("Menu de metodos numericos")
    print("1- Metodo de biseccion")
    print("2- Metodo de la regla falsa")
    print("3- Metodo del punto fijo (para problemas de tipo aln(x) + bx + c = 0)")
    print("4- Metodo de Newton Raphson")
    print("5- Metodo de Lin")
    print("6- Metodo de Polinomios de Lagrange")
    print("0- Salir")
    
    opcion = int(input("Ingresa una opcion: "))
    print("TE AMO MAXIMO EMBARAZAME")

    if opcion == 0:
        print("Saliendoooooo..... \n Te amo maximo y kindred y tista")

    if opcion == 1:

        iteraciones = int(input("Ingresa el numero de iteraciones: "))
        a = int(input("Ingresa el valor de a: "))
        b = int(input("Ingresa el valor de b: "))
        epsilon = float(input("Ingresa el valor de epsilon: "))
        redondeo = int(input("Ingresa las cifras decimales del redondeo: "))

        biseccion(a,b, iteraciones, epsilon, redondeo)
    
    if opcion == 3:

        iteraciones = int(input("Ingresa el numero de iteraciones: "))
        a = float(input("Ingresa el valor de a: "))
        b = float(input("Ingresa el valor de b: "))
        c = float(input("Ingresa el valor de c: "))
        inicial = float(input("Ingresa un valor inicial: "))

        aproximacion = puntoFijo(a, b, c, iteraciones, inicial)

        print("Resultado final: " + str(aproximacion))

    if opcion == 4:

        newtonRaphson()


    if opcion == 5:

        grados = []

        iteraciones = int(input("Ingresa el numero de iteraciones: "))
        grado = int(input("Ingresa el grado del polinomio: "))
        for i in range(0,grado):
            grados.append(int(input("Ingresa el coeficiente del grado " +  str(i) + ": ")))

        print(grado)  
        
        lin(iteraciones, grado)

    #if opcion == 6:


        
