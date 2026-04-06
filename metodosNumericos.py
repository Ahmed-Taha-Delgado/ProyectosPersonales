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
                  str(a), 
                  str(b), 
                  str(float(f.subs(x, a))),
                  str(float(f.subs(x, b)))]
        
        xm = xmf(a, b)
        if float(f.subs(x, a))*float(f.subs(x, xm)) < 0:
            b = xm
        else:
            a = xm

        error = abs(xm -xa)
        xa = xm

        tablaii = [str(xm),
                  str(float(f.subs(x, xm))),
                  str(error)]

        tablai = tablai + tablaii
        tabla.append(tablai)

        if error < epsilon:
            break

    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))     
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
                  str(a), 
                  str(b), 
                  str(float(f.subs(x, a))),
                  str(float(f.subs(x, b)))]
        
        xr = xrf(a, b)
        if float(f.subs(x, a))*float(f.subs(x, xr)) < 0:
            b = xr
        else:
            a = xr

        error = abs(xr -xa)
        xa = xr

        tablaii = [str(xr),
                  str(float(f.subs(x, xr))),
                  str(error)]

        tablai = tablai + tablaii
        tabla.append(tablai)

        if error < epsilon:
            break

    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))     
    print("La raiz aproximada de xr es " + str(round(xr, redondeo)))


def puntoFijo():

    #Declaramos la funcion
    x = sp.symbols('x')
    fString = input("Ingresa la funcion despejada (g(xi)): ")
    gx = sp.sympify(fString)
    if isinstance(gx, (list, tuple)):
        gx = gx[0]

    #redondeo
    redondeo = int(input("Ingresa los decimales a redondear: "))

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
        tabla = [[str(a), str(b), str(gx.subs(x,a)), str(gx.subs(x,b)), str(dgx.subs(x,a)), str(dgx.subs(x,b))]]
        formato_decimales = f".{redondeo}f"
        print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))      

        if gx.subs(x,a) >= a and gx.subs(x,a) <= b and gx.subs(x,b) >= a and gx.subs(x,b) <= b and dgx.subs(x,a) >= 0 and dgx.subs(x,a) <= 1 and dgx.subs(x,b) >= 0 and dgx.subs(x,b) <= 1:
            print("El metodo converge")
        else:
            print("El metodo no converge")
            return
        
    #Condiciones de parada
    epsilon = float(input("Ingresa epsilon: "))
    iteraciones = int(input("Ingresa las iteraciones: "))
    
    #Valor inicial
    x0 = int(input("Ingresa un valor inicial: "))
    
    #Tabla y funcion recursiva
    encabezados2 = ["i", "xi", "error"]
    tabla2 = [[str(0), str(x0), "-"]]
    error = x0

    def puntoFijoRecursivo(xi, i, iteraciones, error):
        
        if i == 0 or error <= epsilon:
            return round(xi,redondeo)

        xii = float(gx.subs(x, xi))
        error = abs(xii - xi)
        tablai = [iteraciones - i + 1, xii, f"{error:.{redondeo}f}"]
        tabla2.append(tablai)

        return puntoFijoRecursivo(xii, i - 1, iteraciones, error)
    
    xAprox = puntoFijoRecursivo(x0, iteraciones, iteraciones, error)
    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla2, headers=encabezados2, tablefmt="grid", floatfmt=formato_decimales))      
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
        
        puntoi = float(n.subs(x, punto))
        error = np.abs(puntoi - punto)
        tablai = [iteraciones - i, puntoi, f"{error:.{redondeo}f}"]
        tabla.append(tablai)
        
        return newtonRecursivo(puntoi, i - 1, iteraciones, error)

    xAprox = newtonRecursivo(punto, iteraciones - 1, iteraciones, error)
    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))      
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
    tDeltaP0 = ["Δp0", deltaP0]
    tDeltaQ0 = ["Δq0", deltaQ0]
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
            tPi.append(pi)
            tQi.append(qi)
        #Si no es la primera iteraciones
        else:
            pi = tPi[-1]+tDeltaPi[-1]
            qi = tQi[-1]+tDeltaQi[-1]
            tPi.append(pi)
            tQi.append(qi)

        #Calculo de los bk tomando en cuenta b-1 = b-2 = 0
        for j in range(0, len(coeficientes) - 2):
            if j == 0:
                tablaResultados[2].append(coeficientes[j]) 
            elif j == 1:
                tablaResultados[3].append(coeficientes[j] - tPi[-1]*tablaResultados[2][-1])
            else:
                tablaResultados[2 + j].append(coeficientes[j] - tPi[-1]*tablaResultados[2 + j - 1][-1] - tQi[-1]*tablaResultados[2 + j - 2][-1])

        #Calculo de R, S, los delta y el error
        R = coeficientes[-2] - tPi[-1]*tablaResultados[len(coeficientes) - 1][-1] - tQi[-1]*tablaResultados[len(coeficientes) - 2][-1]
        S = coeficientes[-1] - tQi[-1]*tablaResultados[len(coeficientes) - 1][-1] 
        
        deltaPi = R / tablaResultados[len(coeficientes) - 1][-1] 
        deltaQi = S / tablaResultados[len(coeficientes) - 1][-1] 

        error = np.hypot(float(R), float(S))

        tablaResultados[len(coeficientes)].append(R)
        tablaResultados[len(coeficientes) + 1].append(S)
        tDeltaPi.append(deltaPi)
        tDeltaQi.append(deltaQi)
        tError.append(error)
        
        return linRecursivo(error, i - 1, iteraciones)

    #Impresion de las tablas
    print("Tabla de datos iniciales:")
    formato_decimales = f".{redondeo}f"
    print(tabulate(tablasIniciales, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))      
    print("\nTabla de iteraciones:")
    linRecursivo(1, iteraciones, iteraciones)
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

    #Declaramos la variable simbolica
    x = sp.symbols('x')
    
    #Redondeo
    redondeo = int(input("Ingresa a cuantos decimales el redondeo: "))

    #Tabla inicial
    caso = input("Deseas ingresar la funcion o los valores evaluados de la funcion? (1/2): ")
    puntos = int(input("Ingresa cuantos puntos tendra tu tabla: "))
    valorInicial = float(input("Ingresa el valor inicial: "))
    tabla = []
    encabezados = ["x", "f(x)"]

    if caso == "1":

        #Recibimos la funcion
        fString = input("Ingresa la funcion: ")
        f = sp.sympify(fString)
        if isinstance(f, (list, tuple)):
            f = f[0]

        #Tabla de datos
        for i in range(0, puntos):
            xi = float(input("Ingresa la x" + str(i+1) + ": "))
            yi = f.subs(x, xi).evalf()
            tablai = [xi, yi]
            tabla.append(tablai)
        
    else:

        #Tabla de datos
        for i in range(0, puntos):
            xi = float(input("Ingresa la x" + str(i+1) + ": "))
            yi = float(input("Ingresa la y" + str(i+1) + ": "))
            tablai = [xi, yi]
            tabla.append(tablai)

    #Interpolacion
    interpolacion = 0
    for i in range(0, puntos ):
        productoria = 1

        for j in range(0, puntos):
            if i != j:
                xj = sp.sympify(tabla[j][0])
                xi = sp.sympify(tabla[i][0])
                # x - xj
                numerador = x - xj
                # xi - xj
                denominador = xi - xj
                #productoria
                productoria *= numerador / denominador

        interpolacion += tabla[i][1] * productoria

    interpolacion = sp.expand(interpolacion)
    aproximacion = interpolacion.subs(x, valorInicial)
    interpolacion = interpolacion.xreplace({n: round(n, redondeo) for n in interpolacion.atoms(sp.Number)})

    print("Tu tabla de datos: ")
    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))  
    print("Tu polinomio simbolico es: " + str(interpolacion)) 
    print("El valor de la interpolacion de Lagrange en el punto " + str(valorInicial) + " es " + str((round(float(aproximacion), redondeo))))


def polinomioNewton():

    #Declaramos la variable simbolica
    x = sp.symbols('x')
    
    #Redondeo
    redondeo = int(input("Ingresa a cuantos decimales el redondeo: "))

    #Tabla inicial
    caso = input("Deseas ingresar la funcion o los valores evaluados de la funcion? (1/2): ")
    puntos = int(input("Ingresa cuantos puntos tendra tu tabla: "))
    valorInicial = float(input("Ingresa el valor inicial: "))
    tabla = []
    encabezados = ["xi", "yi"]

    if caso == "1":

        #Recibimos la funcion
        fString = input("Ingresa la funcion: ")
        f = sp.sympify(fString)
        if isinstance(f, (list, tuple)):
            f = f[0]

        #Tabla de datos
        for i in range(0, puntos):
            xi = float(input("Ingresa la x" + str(i+1) + ": "))
            yi = f.subs(x, xi).evalf()
            tablai = [xi, yi]
            tabla.append(tablai)
        
    else:

        #Tabla de datos
        for i in range(0, puntos):
            xi = float(input("Ingresa la x" + str(i+1) + ": "))
            yi = float(input("Ingresa la y" + str(i+1) + ": "))
            tablai = [xi, yi]
            tabla.append(tablai)

    #Diferencias
    for i in range(0, puntos - 1):
        encabezados.append("Δ^(" + str(i + 1) + ")yi")
        for j in range(0, puntos - 1 - i):
            #Δ^k yi = Δ^k-1 yi+1 - Δ^k yi
            deltayi = tabla[j + 1][i + 1] - tabla[j][i + 1]
            tabla[j].append(deltayi)

    #Calculo de h y k
    #h = x1 - x0
    h = tabla[1][0] - tabla[0][0]
    #k = (x - x0) / h
    k = (x - tabla[0][0]) / h

    #combinaciones
    #kCi = [k(k-1)...(k-i+1)]/i!
    combinaciones = []
    for i in range(1, puntos):
        combinacioni = sp.binomial(k, i)
        combinaciones.append(combinacioni)

    #Polinomio de newton 
    #yk = kC1Δy0 + kC2Δ^2y0 + ... + kCjΔ^jy0
    interpolacion = 0
    for i in range(0, puntos):
        if i == 0:
            interpolacion = tabla[0][1]
        else:
            interpolacion += combinaciones[i - 1] * tabla[0][i + 1]
 
    interpolacion = sp.expand_func(interpolacion)
    interpolacion = sp.expand(interpolacion)
    aproximacion = interpolacion.subs(x, valorInicial)
    interpolacion = interpolacion.xreplace({n: round(n, redondeo) for n in interpolacion.atoms(sp.Number)})

    print("Tu tabla de datos: ")
    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))  
    print("Tu polinomio simbolico es: " + str(interpolacion)) 
    print("El valor de la interpolacion de Newton en el punto " + str(valorInicial) + " es " + str((round(float(aproximacion), redondeo))))


def derivacionNumerica():

    #Declaramos la variable simbolica
    x = sp.symbols('x')
    
    #Redondeo
    redondeo = int(input("Ingresa a cuantos decimales el redondeo: "))

    #Tabla inicial
    caso = input("Deseas ingresar la funcion o los valores evaluados de la funcion? (1/2): ")
    puntos = int(input("Ingresa cuantos puntos tendra tu tabla: "))
    valorInicial = float(input("Ingresa el valor inicial: "))
    tabla = []
    encabezados = ["xi", "yi"]

    if caso == "1":

        #Recibimos la funcion
        fString = input("Ingresa la funcion: ")
        f = sp.sympify(fString)
        if isinstance(f, (list, tuple)):
            f = f[0]

        #Tabla de datos
        for i in range(0, puntos):
            xi = float(input("Ingresa la x" + str(i+1) + ": "))
            yi = f.subs(x, xi).evalf()
            tablai = [xi, yi]
            tabla.append(tablai)
        
    else:

        #Tabla de datos
        for i in range(0, puntos):
            xi = float(input("Ingresa la x" + str(i+1) + ": "))
            yi = float(input("Ingresa la y" + str(i+1) + ": "))
            tablai = [xi, yi]
            tabla.append(tablai)

    #Diferencias
    for i in range(0, puntos - 1):
        encabezados.append("Δ^(" + str(i + 1) + ")yi")
        for j in range(0, puntos - 1 - i):
            #Δ^k yi = Δ^k-1 yi+1 - Δ^k yi
            deltayi = tabla[j + 1][i + 1] - tabla[j][i + 1]
            tabla[j].append(deltayi)

    #Calculo de h y k
    #h = x1 - x0
    h = tabla[1][0] - tabla[0][0]
    #k = (x - x0) / h
    k = (x - tabla[0][0]) / h

    #combinaciones
    #kCi = [k(k-1)...(k-i+1)]/i!
    combinaciones = []
    for i in range(1, puntos):
        combinacioni = sp.binomial(k, i)
        combinaciones.append(combinacioni)

    #Polinomio de newton 
    #yk = kC1Δy0 + kC2Δ^2y0 + ... + kCjΔ^jy0
    interpolacion = 0
    for i in range(0, puntos):
        if i == 0:
            interpolacion = tabla[0][1]
        else:
            interpolacion += combinaciones[i - 1] * tabla[0][i + 1]
 
    interpolacion = sp.expand_func(interpolacion)
    interpolacion = sp.expand(interpolacion)

    #Calculo de la derivada
    orden = int(input("Ingresa el orden de la derivada: "))
    derivada = sp.diff(interpolacion, x, orden)

    aproximacion = derivada.subs(x, valorInicial)
    derivada = derivada.xreplace({n: round(n, redondeo) for n in derivada.atoms(sp.Number)})

    print("Tu tabla de datos: ")
    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))  
    print("Tu derivada simbolica en forma de polinomio es: " + str(derivada)) 
    print("El valor de la derivada en el punto " + str(valorInicial) + " es " + str((round(float(aproximacion), redondeo))))


def richardson():

    #Declaramos la variable simbolica
    x = sp.symbols('x')
    
    #Redondeo
    redondeo = int(input("Ingresa a cuantos decimales el redondeo: "))

    #Tabla inicial
    caso = input("Deseas ingresar la funcion o los valores evaluados de la funcion? (1/2): ")
    puntos = int(input("Ingresa cuantos puntos tendra tu tabla: "))
    valorInicial = float(input("Ingresa el valor inicial: "))
    tabla1 = []
    tabla2 = []
    encabezados = ["xi", "yi"]

    if caso == "1":

        #Recibimos la funcion
        fString = input("Ingresa la funcion: ")
        f = sp.sympify(fString)
        if isinstance(f, (list, tuple)):
            f = f[0]

        #Tabla de datos
        print("Para h1")
        for i in range(0, puntos):
            xi = float(input("Ingresa la x" + str(i+1) + ": "))
            yi = f.subs(x, xi).evalf()
            tablai = [xi, yi]
            tabla1.append(tablai)
        
        print("Para h2")
        for i in range(0, puntos):
            xi = float(input("Ingresa la x" + str(i+1) + ": "))
            yi = f.subs(x, xi).evalf()
            tablai = [xi, yi]
            tabla2.append(tablai)

    else:

        #Tabla de datos
        print("Para h1")
        for i in range(0, puntos):
            xi = float(input("Ingresa la x" + str(i+1) + ": "))
            yi = float(input("Ingresa la y" + str(i+1) + ": "))
            tablai = [xi, yi]
            tabla1.append(tablai)

        print("Para h2")
        for i in range(0, puntos):
            xi = float(input("Ingresa la x" + str(i+1) + ": "))
            yi = float(input("Ingresa la y" + str(i+1) + ": "))
            tablai = [xi, yi]
            tabla2.append(tablai)

    #Diferencias
    for i in range(0, puntos - 1):
        encabezados.append("Δ^(" + str(i + 1) + ")yi")
        for j in range(0, puntos - 1 - i):
            #Δ^k yi = Δ^k-1 yi+1 - Δ^k yi
            deltayi = tabla1[j + 1][i + 1] - tabla1[j][i + 1]
            tabla1[j].append(deltayi)
    
    for i in range(0, puntos - 1):
        encabezados.append("Δ^(" + str(i + 1) + ")yi")
        for j in range(0, puntos - 1 - i):
            #Δ^k yi = Δ^k-1 yi+1 - Δ^k yi
            deltayi = tabla2[j + 1][i + 1] - tabla2[j][i + 1]
            tabla2[j].append(deltayi)

    #Calculo de h y k
    #h = x1 - x0
    h1 = tabla1[1][0] - tabla1[0][0]
    h2 = tabla2[1][0] - tabla2[0][0]
    #k = (x - x0) / h
    k1 = (x - tabla1[0][0]) / h1
    k2= (x - tabla2[0][0]) / h2

    #combinaciones
    #kCi = [k(k-1)...(k-i+1)]/i!
    combinaciones1 = []
    for i in range(1, puntos):
        combinacioni = sp.binomial(k1, i)
        combinaciones1.append(combinacioni)
    
    combinaciones2 = []
    for i in range(1, puntos):
        combinacioni = sp.binomial(k2, i)
        combinaciones2.append(combinacioni)

    #Polinomio de newton 
    #yk = kC1Δy0 + kC2Δ^2y0 + ... + kCjΔ^jy0
    interpolacion1 = 0
    for i in range(0, puntos):
        if i == 0:
            interpolacion1 = tabla1[0][1]
        else:
            interpolacion1 += combinaciones1[i - 1] * tabla1[0][i + 1]

    interpolacion2 = 0
    for i in range(0, puntos):
        if i == 0:
            interpolacion2 = tabla2[0][1]
        else:
            interpolacion2 += combinaciones2[i - 1] * tabla2[0][i + 1]
 
    interpolacion1 = sp.expand_func(interpolacion1)
    interpolacion1 = sp.expand(interpolacion1)

    interpolacion2 = sp.expand_func(interpolacion2)
    interpolacion2 = sp.expand(interpolacion2)

    #Calculo de la derivada
    orden = int(input("Ingresa el orden de la derivada: "))
    derivada1 = sp.diff(interpolacion1, x, orden)
    derivada2 = sp.diff(interpolacion2, x, orden)

    aproximacion1 = derivada1.subs(x, valorInicial)
    aproximacion2 = derivada2.subs(x, valorInicial)

    derivada = derivada2 + (derivada2 - derivada1) / (((h1/h2)**2) - 1)
    derivada = sp.expand(derivada)
    aproximacion = derivada.subs(x, valorInicial)

    derivada = derivada.xreplace({n: round(n, redondeo) for n in derivada.atoms(sp.Number)})

    formato_decimales = f".{redondeo}f"
    print("Tabla de h1:")
    print(tabulate(tabla1, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))  
    print("Tabla de h2:")
    print(tabulate(tabla2, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))  
    print("El valor de Dh1 es " + str(round(aproximacion1, redondeo)) + ", el valor de Dh2 es " + str(round(aproximacion2, redondeo)))
    print("Tu derivada mejorada simbolica en forma de polinomio es: " + str(derivada)) 
    print("El valor de la derivada mejorada en el punto " + str(valorInicial) + " es " + str((round(float(aproximacion), redondeo))))


def integracionNumerica():

    #Declaramos la funcion
    x = sp.symbols('x')

    #Intervalo de integracion
    a = float(input("Ingresa el valor de a: "))
    b = float(input("Ingresa el valor de b: "))

    #redondeo
    redondeo = int(input("Ingresa el redondeo a cuantos decimales: "))

    #Tabla 
    encabezados = ["i", "xi", "yi"]
    tabla = []

    #Tabla inicial
    caso = input("Deseas ingresar la funcion o los valores evaluados de la funcion? (1/2): ")
    puntos = int(input("Ingresa cuantos puntos tendra tu tabla: "))

    if caso == "1":

        #Recibimos la funcion
        fString = input("Ingresa la funcion: ")
        f = sp.sympify(fString)
        if isinstance(f, (list, tuple)):
            f = f[0]

        #Tabla de datos
        for i in range(0, puntos):
            xi = float(input("Ingresa la x" + str(i+1) + ": "))
            yi = f.subs(x, xi).evalf()
            tablai = [i, xi, yi]
            tabla.append(tablai)
        
    else:

        #Tabla de datos
        for i in range(0, puntos):
            xi = float(input("Ingresa la x" + str(i+1) + ": "))
            yi = float(input("Ingresa la y" + str(i+1) + ": "))
            tablai = [i, xi, yi]
            tabla.append(tablai)

    h = tabla[1][1] - tabla[0][1]
    formula = input("Quieres aproximar con integracion trapecial, Simpson 1/3 o Simpson 3/8? (1/2/3): ")

    integral = 0
    #trapecial
    if formula == "1":
        #y0 + yn
        integral =  tabla[0][2] + tabla[-1][2]
        #2sum(yi)
        for i in range(1, puntos - 1):
            integral += 2*tabla[i][2]
        #h/2
        integral *= h / 2

    #simpson 1/3
    elif formula == "2":
        #y0 + yn
        integral =  tabla[0][2] + tabla[-1][2]
        #4sum(yimpar)+2sum(ypar)
        for i in range(1, puntos - 1):
            if i % 2 == 0:
                integral += 2*tabla[i][2]
            else:
                integral += 4*tabla[i][2]
        #h/3
        integral *= h / 3
    
    #simpson 3/8
    elif formula == "3":
        #y0 + yn
        integral =  tabla[0][2] + tabla[-1][2]
        #2sum(ymult3)+3sum(yrestante)
        for i in range(1, puntos - 1):
            if i % 3 == 0:
                integral += 2*tabla[i][2]
            else:
                integral += 3*tabla[i][2]
        #3h/8
        integral *= (3 * h) / 8

    print("Tu tabla de datos: ")
    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))  
    print("El valor aproximado de tu integral en el intervalo ["+ str(a) + ", " + str(b) + "] es " + str(round(integral, redondeo)))


def integracionGaussiana():
    
    #Declaramos la funcion
    x = sp.symbols('x')
    fString = input("Ingresa la funcion: ")
    f = sp.sympify(fString)
    if isinstance(f, (list, tuple)):
        f = f[0]

    #Intervalo de integracion
    a = float(input("Ingresa el valor de a: "))
    b = float(input("Ingresa el valor de b: "))

    #redondeo
    redondeo = int(input("Ingresa el redondeoa cuantos decimales: "))

    #grado
    grado = int(input("Ingresa el grado de la cuadratura: "))

    #Tabla de cuadratura
    tablaGauss = [
        [[0],[2]],
        [[-sp.sqrt(sp.Rational(1, 3)), sp.sqrt(sp.Rational(1, 3))],[1,1]],
        [[0, -sp.sqrt(sp.Rational(3, 5)), sp.sqrt(sp.Rational(3, 5))],[8/9, 5/9, 5/9]],
        [[-sp.sqrt((3 - 2*sp.sqrt(sp.Rational(6, 5))) / 7), sp.sqrt((3 - 2*sp.sqrt(sp.Rational(6, 5))) / 7), -sp.sqrt((3 + 2*sp.sqrt(sp.Rational(6, 5))) / 7), sp.sqrt((3 + 2*sp.sqrt(sp.Rational(6, 5))) / 7)],
         [(18 + sp.sqrt(30)) / 36, (18 + sp.sqrt(30)) / 36, (18 - sp.sqrt(30)) / 36, (18 - sp.sqrt(30)) / 36]],
        [[0, -sp.Rational(1, 3) * sp.sqrt(5 - 2*sp.sqrt(sp.Rational(10, 7))), sp.Rational(1, 3) * sp.sqrt(5 - 2*sp.sqrt(sp.Rational(10, 7))), -sp.Rational(1, 3) * sp.sqrt(5 + 2*sp.sqrt(sp.Rational(10, 7))), sp.Rational(1, 3) * sp.sqrt(5 + 2*sp.sqrt(sp.Rational(10, 7)))],
         [128/225, (322 + 13*sp.sqrt(70)) / 900, (322 + 13*sp.sqrt(70)) / 900, (322 - 13*sp.sqrt(70)) / 900, (322 - 13*sp.sqrt(70)) / 900]],
    ]

    #Cuadratura gaussiana
    integral = 0
    for i in range(0, grado):
        integral += tablaGauss[grado - 1][1][i] * f.subs(x, ((b-a)/2)*tablaGauss[grado - 1][0][i] + (a+b)/2)
    
    integral *= (b-a)/2

    print("El valor aproximado de tu integral en el intervalo ["+ str(a) + ", " + str(b) + "] es " + str(round(integral, redondeo)))



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
    print("9- Extrapolacion de Richardson")
    print("10- Integracion numerica (Trapecial, S.1/3, S.3/8)")
    print("11- Integracion numerica por Cuadratura Gaussiana")
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

    if opcion == 6:
        print("\nElegiste interpolacion de Lagrange:\n")     
        polinomioLagrange()

    if opcion == 7:
        print("\nElegiste interpolacion de Newton:\n")     
        polinomioNewton()

    if opcion == 8:
        print("\nElegiste Derivacion Numerica:\n")     
        derivacionNumerica()

    if opcion == 9:
        print("\nElegiste Extrapolacion de Richardson:\n")     
        richardson()

    if opcion == 10:
        print("\nElegiste Integracion Numerica:\n")     
        integracionNumerica()
    
    if opcion == 11:
        print("\nElegiste Integracion por Cuadratura Gaussiana:\n")     
        integracionGaussiana()

        
