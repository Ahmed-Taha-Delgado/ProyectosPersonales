import numpy as np
import sympy as sp
from tabulate import tabulate

def biseccion():

    #declarar la funcion
    x = sp.symbols('x')
    fString = input("Ingresa la funcion: ")
    f = sp.sympify(fString)
    if isinstance(f, (list, tuple)):
        f = f[0]

    #intervalo inicial
    a = int(input("Ingresa el valor de a: "))
    b = int(input("Ingresa el valor de b: "))

    #condicion de parada
    epsilon = float(input("Ingresa epsilon: "))
    iteraciones = int(input("Ingresa las iteraciones: "))
    
    #redondeo
    redondeo = int(input("Ingresa los decimales a redondear: "))

    def xmf(a, b):
        return (a + b) / 2
    
    #iteraciones e informacion para tabular
    xa = 0
    tabla = []
    encabezados = ["Iteracion", "a", "b", "f(a)", "f(b)", "xm", "f(xm)", "error"]  
    for i in range(0, iteraciones): 

        tablai = [str(i + 1),
                  str(round(a, redondeo)), 
                  str(round(b, redondeo)), 
                  str(round(float(f.subs(x, a)), redondeo)),
                  str(round(float(f.subs(x, b)), redondeo))]
        
        xm = xmf(a, b)
        if float(f.subs(x, a))*float(f.subs(x, xm)) < 0:
            b = xm
        else:
            a = xm

        error = abs(xm -xa)
        xa = xm

        tablaii = [str(round(xm, redondeo)),
                  str(round(float(f.subs(x, xm)), redondeo)),
                  str(round(error, redondeo))]

        tablai = tablai + tablaii
        tabla.append(tablai)

        if error < epsilon:
            break

    print(tabulate(tabla, headers=encabezados, tablefmt="grid"))    
    print("La raiz aproximada de xm es " + str(round(xm, redondeo)))


def reglaFalsa():

    #declarar la funcion
    x = sp.symbols('x')
    fString = input("Ingresa la funcion: ")
    f = sp.sympify(fString)
    if isinstance(f, (list, tuple)):
        f = f[0]

    #intervalo inicial
    a = int(input("Ingresa el valor de a: "))
    b = int(input("Ingresa el valor de b: "))

    #condicion de parada
    epsilon = float(input("Ingresa epsilon: "))
    iteraciones = int(input("Ingresa las iteraciones: "))
    
    #redondeo
    redondeo = int(input("Ingresa los decimales a redondear: "))

    def xrf(a, b):
        return float(b - ((f.subs(x, b)*(b - a)) / (f.subs(x, b) - f.subs(x,a))))
    
    #iteraciones e informacion para tabular
    xa = 0
    tabla = []
    encabezados = ["Iteracion", "a", "b", "f(a)", "f(b)", "xr", "f(xr)", "error"]  
    for i in range(0, iteraciones): 

        tablai = [str(i + 1),
                  str(round(a, redondeo)), 
                  str(round(b, redondeo)), 
                  str(round(float(f.subs(x, a)), redondeo)),
                  str(round(float(f.subs(x, b)), redondeo))]
        
        xr = xrf(a, b)
        if float(f.subs(x, a))*float(f.subs(x, xr)) < 0:
            b = xr
        else:
            a = xr

        error = abs(xr -xa)
        xa = xr

        tablaii = [str(round(xr, redondeo)),
                  str(round(float(f.subs(x, xr)), redondeo)),
                  str(round(error, redondeo))]

        tablai = tablai + tablaii
        tabla.append(tablai)

        if error < epsilon:
            break

    print(tabulate(tabla, headers=encabezados, tablefmt="grid"))    
    print("La raiz aproximada de xr es " + str(round(xr, redondeo)))


def puntoFijo():

    #Declaramos la funcion
    x = sp.symbols('x')
    fString = input("Ingresa la funcion despejada (g(xi)): ")
    gx = sp.sympify(fString)
    if isinstance(gx, (list, tuple)):
        gx = gx[0]

    convergencia = input("Quieres evaluar la convergencia del metodo? (si/no): ")

    if convergencia == "si":
        #intervalo de convergencia
        print("Ingresa un intervalo para verificar convergencia")
        a = int(input("Ingresa a: "))
        b = int(input("Ingresa b: "))

        #Derivando g(xi)
        dgx = sp.diff(gx, x)

        #Evaluando convergencia
        tabla = []
        encabezados = ["a", "b", "g(a) (∈[a,b])", "g(b) (∈[a,b])", "|g'(a)| (∈[0,1])", "|g'(b)| (∈[0,1])"]
        tabla = [[str(a), str(b), str(round(gx.subs(x,a),3)), str(round(gx.subs(x,b),3)), str(round(dgx.subs(x,a),3)), str(round(dgx.subs(x,b),3))]]
        print(tabulate(tabla, headers=encabezados, tablefmt="grid"))   

        if gx.subs(x,a) >= a and gx.subs(x,a) <= b and gx.subs(x,b) >= a and gx.subs(x,b) <= b and dgx.subs(x,a) >= 0 and dgx.subs(x,a) <= 1 and dgx.subs(x,b) >= 0 and dgx.subs(x,b) <= 1:
            print("El metodo converge")
        else:
            print("El metodo no converge")
            return
        
    #Condiciones de parada
    epsilon = float(input("Ingresa epsilon: "))
    iteraciones = int(input("Ingresa las iteraciones: "))
    
    #redondeo
    redondeo = int(input("Ingresa los decimales a redondear: "))

    #Valor inicial
    x0 = int(input("Ingresa un valor inicial: "))
    
    #Tabla y funcion recursiva
    encabezados2 = ["i", "xi", "error"]
    tabla2 = [[str(0), str(x0), "-"]]
    error = x0

    def puntoFijoRecursivo(xi, i, iteraciones, error):
        
        if i == 0 or error <= epsilon:
            return round(xi,redondeo)

        xii = gx.subs(x, xi)
        error = abs(xii - xi)
        tablai = [str(iteraciones - i + 1), str(round(xii,redondeo)), str(round(error,redondeo))]
        tabla2.append(tablai)

        return puntoFijoRecursivo(xii, i - 1, iteraciones, error)
    
    xAprox = puntoFijoRecursivo(x0, iteraciones, iteraciones, error)
    print(tabulate(tabla2, headers=encabezados2, tablefmt="grid"))   
    print("El valor aproximado es " + str(xAprox))


def newtonRaphson():

    #Declaramos la funcion
    x = sp.symbols('x')
    fString = input("Ingresa la funcion: ")
    f = sp.sympify(fString)
    if isinstance(f, (list, tuple)):
        f = f[0]

    #Derivamos
    derivada = sp.diff(f, x)

    #Expresion de newton-raphson
    n = x - (f/derivada)
    
    #Condiciones de parada
    iteraciones = int(input("Ingresa el numero de iteraciones: "))
    epsilon = float(input("Ingrese epsilon: "))

    #redondeo
    redondeo = int(input("Ingresa el redondeoa cuantos decimales: "))

    #Valor inicial
    punto = int(input("Ingresa el punto x0: "))

    #Tabla y funcion recursiva
    encabezados = ["i", "xi", "error"]
    tabla = [[str(0), str(punto), "-"]]
    error = punto

    def newtonRecursivo(punto, i, iteraciones, error):
        
        if i == 0 or error <= epsilon:
            return round(punto, redondeo)
        
        puntoi = n.subs(x, punto)
        error = np.abs(puntoi - punto)
        tablai = [str(iteraciones - i), str(round(puntoi, redondeo)), str(round(error, redondeo))]
        tabla.append(tablai)
        
        return newtonRecursivo(puntoi, i - 1, iteraciones, error)

    xAprox = newtonRecursivo(punto, iteraciones - 1, iteraciones, error)
    print(tabulate(tabla, headers=encabezados, tablefmt="grid"))   
    print("El valor aproximado es " + str(xAprox))


def lin():

    #Declaramos la funcion
    x = sp.symbols('x')
    fString = input("Ingresa el polinomio: ")
    f = sp.sympify(fString)
    if isinstance(f, (list, tuple)):
        f = f[0]
    polinomio = sp.Poly(f, x)

    #Datos iniciales
    grado = polinomio.degree()
    coeficientes = polinomio.all_coeffs() #De mayor grado a menor grado
    deltaP0 = coeficientes[-2] / coeficientes[-3]
    deltaQ0 = coeficientes[-1] / coeficientes[-3]

    #Redondeo
    redondeo = int(input("Ingresa a cuantos decimales el redondeo: "))

    #Condiciones de parada
    iteraciones = int(input("Ingresa cuantas iteraciones: "))
    epsilon = float(input("Ingresa epsilon: "))

    #Tablas iniciales
    tablasIniciales = []
    encabezados = ["Datos iniciales", "Valor"]
    tP0 = ["p0", 0]
    tQ0 = ["q0", 0]
    tablasIniciales.append(tP0)
    tablasIniciales.append(tQ0)
    for i in range(0, len(coeficientes)):
        tablasai = ["a" + str(i), coeficientes[i]]
        tablasIniciales.append(tablasai)
    tDeltaP0 = ["Δp0", round(deltaP0, redondeo)]
    tDeltaQ0 = ["Δq0", round(deltaQ0, redondeo)]
    tablasIniciales.append(tDeltaP0)
    tablasIniciales.append(tDeltaQ0)

    #Tablas de resultados
    tablaResultados = []
    encabezados2 = ["Parametro"]
    tPi = ["pi"]
    tQi = ["qi"]
    tablaResultados.append(tPi)
    tablaResultados.append(tQi)
    for i in range (0, len(coeficientes)):
        bx = "b" + str(i)  
        if i == len(coeficientes) - 2:
            bx = "R"
        elif i == len(coeficientes) - 1:
            bx = "S"
        tablai = [bx]
        tablaResultados.append(tablai)
    tDeltaPi = ["Δpi"]
    tDeltaQi = ["Δqi"]
    tError = ["Error"]
    tablaResultados.append(tDeltaPi)
    tablaResultados.append(tDeltaQi)
    tablaResultados.append(tError)

    #metodo de lin ahora si
    def linRecursivo(error, i, iteraciones):

        if i == 0 or error <= epsilon:
            return
        
        encabezados2.append("Iteracion " + str(iteraciones - i + 1))
        
        #Si es la primera iteracion
        if iteraciones == i:
            pi = deltaP0
            qi = deltaQ0
            tPi.append(round(pi,redondeo))
            tQi.append(round(qi,redondeo))
        #Si no es la primera iteraciones
        else:
            pi = tPi[-1]+tDeltaPi[-1]
            qi = tQi[-1]+tDeltaQi[-1]
            tPi.append(round(pi,redondeo))
            tQi.append(round(qi,redondeo))

        #Calculo de los bk tomando en cuenta b-1 = b-2 = 0
        for j in range(0, len(coeficientes) - 2):
            if j == 0:
                tablaResultados[2].append(round(coeficientes[j], redondeo)) 
            elif j == 1:
                tablaResultados[3].append(round(coeficientes[j] - tPi[-1]*tablaResultados[2][-1], redondeo))
            else:
                tablaResultados[2 + j].append(round(coeficientes[j] - tPi[-1]*tablaResultados[2 + j - 1][-1] - tQi[-1]*tablaResultados[2 + j - 2][-1], redondeo))

        #Calculo de R, S, los delta y el error
        R = coeficientes[-2] - tPi[-1]*tablaResultados[len(coeficientes) - 1][-1] - tQi[-1]*tablaResultados[len(coeficientes) - 2][-1]
        S = coeficientes[-1] - tQi[-1]*tablaResultados[len(coeficientes) - 1][-1] 
        
        deltaPi = R / tablaResultados[len(coeficientes) - 1][-1] 
        deltaQi = S / tablaResultados[len(coeficientes) - 1][-1] 

        error = np.hypot(float(R), float(S))

        tablaResultados[len(coeficientes)].append(round(R, redondeo))
        tablaResultados[len(coeficientes) + 1].append(round(S, redondeo))
        tDeltaPi.append(round(deltaPi, redondeo))
        tDeltaQi.append(round(deltaQi, redondeo))
        tError.append(round(error, redondeo))
        
        return linRecursivo(error, i - 1, iteraciones)

    #Impresion de las tablas
    print("Tabla de datos iniciales:")
    print(tabulate(tablasIniciales, headers=encabezados, tablefmt="grid"))   
    print("\nTabla de iteraciones:")
    linRecursivo(1, iteraciones, iteraciones)
    formato_decimales = f".{redondeo}f"
    print(tabulate(tablaResultados, headers=encabezados2, tablefmt="grid", floatfmt=formato_decimales)) 
    
    #Resultados
    print("Polinomio resultante:")
    #Obtendiendo las b
    b = []
    for i in range(2, len(tablaResultados) - 2):
        b.append(round(tablaResultados[i][-1], redondeo))
    gradoResultante = len(b) - 1
    polinomioResultante1 = x**2 + round(float(tPi[-1]),redondeo)*x + round(float(tQi[-1]),redondeo)
    polinomioResultante2 = 0
    for i in range (gradoResultante - 3, -1, -1):
        polinomioResultante2 += b[i]*(x**(gradoResultante - i - 3))
    
    print((polinomioResultante1)*(polinomioResultante2) + b[-3]*x + b[-2])

    #Raices
    raices = sp.solve(polinomioResultante1, x)
    raices2 = sp.solve(polinomioResultante2, x)

    print("Las raices aproximadas del polinomio son: ")
    for i in range(len(raices)):
        print(round(raices[i],redondeo))
    for i in range(len(raices2)):
        print(round(raices2[i],redondeo))


def polinomioLagrange():

    x = sp.symbols('x')


opcion = -1
while(opcion != 0):

    print("\n")
    print("----------------------------------------")
    print("Menu de metodos numericos")
    print("1- Metodo de biseccion")
    print("2- Metodo de la regla falsa (interpolacion lineal)")
    print("3- Metodo del punto fijo")
    print("4- Metodo de Newton-Raphson")
    print("5- Metodo de Lin")
    print("6- Interpolacion con Polinomios de Lagrange")
    print("7- Interpolacion con Polinomios de Newton")
    print("8- Derivacion numerica con polinomios de Newton")
    print("9- Integracion numerica con polinomios de Newton")
    print("10- Integracion numerica por Cuadratura Gaussiana")
    print("0- Salir")
    print("----------------------------------------")
    
    opcion = int(input("Ingresa una opcion: "))

    if opcion == 0:
        print("Saliendoooooo.....")

    if opcion == 1:
        print("\nElegiste método de bisección:\n")
        biseccion()

    if opcion == 2:
        print("\nElegiste metodo de regla falsa:\n")
        reglaFalsa()
    
    if opcion == 3:
        print("\nElegiste metodo de punto fijo:\n")
        puntoFijo()


    if opcion == 4:
        print("\nElegiste metodo de Newton-Raphson:\n")     
        newtonRaphson()


    if opcion == 5:
        print("\nElegiste metodo de Lin:\n")     
        lin()

    #if opcion == 6:


        
