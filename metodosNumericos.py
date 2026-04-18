import numpy as np
import sympy as sp
from tabulate import tabulate

#Declaramos la variable simbolica
x = sp.symbols('x')
y = sp.symbols('y')
t = sp.symbols('t')

#funciones auxiliar para pedir datos:
def obtenerFuncion():
    while True:
        fString = input("Ingresa la funcion f(x): ")
        try:
            f = sp.sympify(fString, locals={'x': x})
            if isinstance(f, (list, tuple)):
                f = f[0]
            f.subs(x, 1).evalf()
            if f.free_symbols - {x}:
                print("Error, solo puedes usar la variable 'x'")
                continue
            return f
        except Exception:
            print("Error al ingresar la funcion")
            print("Ejemplo: Usa '2*x' en lugar de '2x', y 'x**2' en lugar de 'x^2'")

def obtenerFuncionDosVariables():
    while True:
        fString = input("Ingresa la funcion f(x,y): ")
        try:
            f = sp.sympify(fString, locals={'x': x, 'y': y})
            if isinstance(f, (list, tuple)):
                f = f[0]

            if f.free_symbols - {x, y}:
                print("Error, solo puedes usar las variables 'x' y 'y")
                continue
            return f
        except Exception:
            print("Error al ingresar la funcion")
            print("Ejemplo: Usa '2*x' en lugar de '2x', y 'x**2' en lugar de 'x^2'")

def obtenerEntero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error, el numero debe ser entero")

def obtenerFlotante(mensaje):
    while True:
        entrada = input(mensaje).strip()
        try:
            flotante = sp.sympify(entrada)
        
            if flotante.free_symbols:
                print("Error, el numero debe ser entero o decimal")
                continue
                
            # Lo evaluamos (.evalf) y lo forzamos a ser flotante de Python
            return float(flotante.evalf())
        except ValueError:
            print("Error, el numero debe ser entero o decimal")

def obtenerIteraciones():
    while True:
        try:
            iteraciones = obtenerEntero("Ingresa las iteraciones (ej. 5): ")
            if iteraciones <= 0:
                print("Ingresa al menos 1 iteracion")
                continue
            if iteraciones > 1000:
                print("Demasiadas iteraciones")
                continue
            break
        except ValueError:
            print("Error al ingresar las condiciones de parada")
    return iteraciones

def obtenerEpsilon():
    while True:
        try:
            epsilon = obtenerFlotante("Ingresa epsilon (ej. 0.001): ")
            if epsilon <= 0:
                print("Epsilon debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("Error al ingresar las condiciones de parada")
    return epsilon

def obtenerCondicionesDeParada():
    return obtenerEpsilon(), obtenerIteraciones()

def obtenerIntervalo():
    while True:
        try:
            a = obtenerFlotante("Ingresa el valor de a: ")
            b = obtenerFlotante("Ingresa el valor de b: ")
            if a == b:
                print("a y b no pueden ser iguales")
                continue
            if a > b:
                print("a no puede ser mayor que b")
                continue
            return a, b
        except ValueError:
            print("Error al ingresar el intervalo")

def obtenerRedondeo():
    while True:
        try:
            redondeo = obtenerEntero("Ingresa los decimales a redondear: ")
            if redondeo <= 0:
                print("El redondeo debe ser de al menos un decimal")
                continue
            return redondeo
        except ValueError:
            print("Error al ingresar el redondeo")

def obtenerPuntos():
    while True:
        try:
            puntos = obtenerEntero("Ingresa cuantos puntos tendra tu tabla: ")
            if puntos < 1:
                print("Debe haber al menos 1 punto")
                continue
            return puntos
        except ValueError:
            print("Error al ingresar los puntos")

def obtenerOrden():
    while True:
        try:
            orden = obtenerEntero("Ingresa el orden de la derivada: ")
            if orden < 1:
                print("El orden debe ser al menos de 1")
                continue
            return orden
        except ValueError:
            print("Error al ingresar el orden de la derivada")

def obtenerGrado():
    while True:
        try:
            grado = obtenerEntero("Ingresa el grado de la cuadraturaGaussiana: ")
            if grado < 1 or grado > 5:
                print("El grade debe estar entre 1 y 5")
                continue
            return grado
        except ValueError:
            print("Error al ingresar el grado de la cuadratura")

def obtenerPreguntaCaso(pregunta):
    while True:
        respuesta = input(pregunta).strip().lower()
        if respuesta in ['si', 'sí', 's'] or respuesta == "1":
            return "1"
        elif respuesta in ['no', 'n'] or respuesta == "2":
            return "2"
        elif respuesta == "3":
            return "3"
        else:
            print("Elige alguna de las opciones")

def obtenerTabla(puntos, caso, f):
    tabla = [] 
    for i in range(0, puntos):
        if caso == "1":
            xi = obtenerFlotante("Ingresa la x" + str(i+1) + ": ")
            yi = f.subs(x, xi).evalf()
        else:
            xi = obtenerFlotante("Ingresa la x" + str(i+1) + ": ")
            yi = obtenerFlotante("Ingresa la y" + str(i+1) + ": ")
        tablai = [xi, yi]
        tabla.append(tablai)           
    return tabla

def obtenerTablaConstante(puntos, caso, f):

    tabla = [] 
    h = abs(obtenerFlotante("Ingresa el valor de h: "))
    x0 = obtenerFlotante("Ingresa x0: ")
    for i in range(0, puntos):
        xi = x0 + i*h
        if caso == "1":
            yi = f.subs(x, xi).evalf()
        else:
            yi = obtenerFlotante("Ingresa la y" + str(i+1) + ": ")
        tablai = [xi, yi]
        tabla.append(tablai)           
    return tabla, h

def obtenerSistemaEcuacionesDiferenciales():
    #Datos iniciales
    print("Toma en cuenta los siguientes cambios de variable: ")
    print("x → t (variable independiente)")
    print("y' → ẋ")

    orden = obtenerOrden()
    print("Convierte tu ED de orden n en un sistema de ecuaciones de orden n")
    print("Ingresaras los componentes de tu vector: ")
    #Crear n variables dimamicas
    
    variables = sp.symbols(f'x1:{orden+1}')
    diccionarioVariables = {'t': t}
    for i in range(orden):
        diccionarioVariables[f'x{i+1}'] = variables[i]

    sistema = []
    for i in range(orden):
        while True:
            fString = input(f"Ingresa ẋ{i+1} = ")
            try:
                f = sp.sympify(fString, locals=diccionarioVariables)
                simbolosIngresados = f.free_symbols
                simbolosPermitidos = set(variables) | {t}
                
                if  simbolosIngresados - simbolosPermitidos:
                    print("Error: Usaste una letra que no está permitida")
                    print("Puedes usar 't' y las 'xi' correspondientes")
                    continue
                    
                sistema.append(f)
                break                 
            except Exception:
                print("Error al ingresar la funcion")
                print("Ejemplo: Usa '2*x' en lugar de '2x', y 'x**2' en lugar de 'x^2'")

    return orden,variables, sistema


#Algoritmos numericos
def biseccion():
    
    #Recibimos datos iniciales
    f = obtenerFuncion()
    a, b = obtenerIntervalo()
    epsilon, iteraciones = obtenerCondicionesDeParada()
    redondeo = obtenerRedondeo()

    def xmf(a, b):
        return (a + b) / 2
    
    #iteraciones e informacion para tabular
    xa = 0
    tabla = []
    encabezados = ["Iteracion", "a", "b", "f(a)", "f(b)", "xm", "f(xm)", "error"]  
    for i in range(0, iteraciones): 

        tablai = [str(i + 1), str(a), str(b), str(float(f.subs(x, a))), str(float(f.subs(x, b)))]
        
        xm = xmf(a, b)
        if float(f.subs(x, a))*float(f.subs(x, xm)) < 0:
            b = xm
        else:
            a = xm

        error = abs(xm -xa)
        xa = xm

        tablaii = [str(xm), str(float(f.subs(x, xm))), str(error)]

        tablai = tablai + tablaii
        tabla.append(tablai)

        if error < epsilon:
            break
        
    #impresion de resultados
    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))     
    print("La raiz aproximada de xm es " + str(round(xm, redondeo)))


def reglaFalsa():

    #Recibimos datos iniciales
    f = obtenerFuncion()
    a, b = obtenerIntervalo()
    epsilon, iteraciones = obtenerCondicionesDeParada()
    redondeo = obtenerRedondeo()

    def xrf(a, b):
        return float(b - ((f.subs(x, b)*(b - a)) / (f.subs(x, b) - f.subs(x,a))))
    
    #iteraciones e informacion para tabular
    xa = 0
    tabla = []
    encabezados = ["Iteracion", "a", "b", "f(a)", "f(b)", "xr", "f(xr)", "error"]  
    for i in range(0, iteraciones): 

        tablai = [str(i + 1), str(a), str(b), str(float(f.subs(x, a))), str(float(f.subs(x, b)))]
        
        xr = xrf(a, b)
        if float(f.subs(x, a))*float(f.subs(x, xr)) < 0:
            b = xr
        else:
            a = xr

        error = abs(xr -xa)
        xa = xr

        tablaii = [str(xr), str(float(f.subs(x, xr))), str(error)]

        tablai = tablai + tablaii
        tabla.append(tablai)

        if error < epsilon:
            break
    
    #impresion de resultados
    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))     
    print("La raiz aproximada de xr es " + str(round(xr, redondeo)))


def puntoFijo():

    #Recibimos datos iniciales
    print("Para este metodo ingresa la funcion despejada")
    gx = obtenerFuncion()
    redondeo = obtenerRedondeo()
    epsilon, iteraciones = obtenerCondicionesDeParada()
    x0 = obtenerFlotante("Ingresa el valor inicial: ")
    convergencia = obtenerPreguntaCaso("Quieres evaluar la convergencia del metodo? (si/no): ")

    if convergencia == "1":
        #intervalo de convergencia
        print("Ingresa un intervalo para verificar convergencia")
        a, b = obtenerIntervalo()

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

    #Recibimos datos iniciales
    f = obtenerFuncion()
    epsilon, iteraciones = obtenerCondicionesDeParada()
    redondeo = obtenerRedondeo()
    punto = obtenerFlotante("Ingresa el valor inicial: ")

    #Derivamos
    derivada = sp.diff(f, x)

    #Expresion de newton-raphson
    n = x - (f/derivada)

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

    #Recibimos datos iniciales
    f = obtenerFuncion()
    redondeo = obtenerRedondeo()
    epsilon, iteraciones = obtenerCondicionesDeParada()

    #Calculos iniciales
    polinomio = sp.Poly(f, x)
    grado = polinomio.degree()
    coeficientes = polinomio.all_coeffs() #De mayor grado a menor grado
    deltaP0 = coeficientes[-2] / coeficientes[-3]
    deltaQ0 = coeficientes[-1] / coeficientes[-3]

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
    
    print(str((polinomioResultante1)*(polinomioResultante2)) + " + " + str(+ b[-2]  + round(float(b[-3].evalf()), redondeo)*x ))

    #Raices
    raices = sp.solve(polinomioResultante1, x)
    raices2 = sp.solve(polinomioResultante2, x)

    print("Las raices aproximadas del polinomio son: ")
    for i in range(len(raices)):
        print(round(raices[i],redondeo))
    for i in range(len(raices2)):
        print(round(raices2[i],redondeo))


def polinomioLagrange():
    
    #Recibimos datos iniciales
    redondeo = obtenerRedondeo()
    puntos = obtenerPuntos()
    valorInicial = obtenerFlotante("Ingresa el punto de evaluacion: ")

    #Tabla inicial
    encabezados = ["x", "f(x)"]
    caso = obtenerPreguntaCaso("Deseas ingresar las xi y la funcion o las (xi, yi)? (1/2): ")

    f = obtenerFuncion() if caso == "1" else None
    tabla = obtenerTabla(puntos, caso, f)

    #Interpolacion
    interpolacion = 0
    for i in range(0, puntos):
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
    
    #Recibimos datos iniciales
    redondeo = obtenerRedondeo()
    puntos = obtenerPuntos()
    valorInicial = obtenerFlotante("Ingresa el punto de evaluacion: ")

    #Tabla inicial
    caso = obtenerPreguntaCaso("Deseas ingresar las xi y la funcion o las xi, yi? (1/2): ")
    encabezados = ["xi", "yi"]

    f = obtenerFuncion() if caso == "1" else None
    tabla, h = obtenerTablaConstante(puntos, caso, f)

    #Diferencias
    for i in range(0, puntos - 1):
        encabezados.append("Δ^(" + str(i + 1) + ")yi")
        for j in range(0, puntos - 1 - i):
            #Δ^k yi = Δ^k-1 yi+1 - Δ^k yi
            deltayi = tabla[j + 1][i + 1] - tabla[j][i + 1]
            tabla[j].append(deltayi)

    #Calculo de k
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

    #Recibimos datos iniciales
    redondeo = obtenerRedondeo()
    puntos = obtenerPuntos()
    valorInicial = obtenerFlotante("Ingresa el punto de evaluacion: ")

    #Tabla inicial o tablas iniciales
    caso = obtenerPreguntaCaso("Deseas ingresar las xi y la funcion o las xi, yi? (1/2): ")
    encabezados = ["xi", "yi"]

    richardson = obtenerPreguntaCaso("Deseas que tu aproximacion sea mejorada con la extrapolacion de Richardson? (si/no): ")

    f = obtenerFuncion() if caso == "1" else None
    tabla, h = obtenerTablaConstante(puntos, caso, f)
    print("Para la tabla 2:")
    if richardson == "1": tabla2, h2 = obtenerTablaConstante(puntos, caso, f)
        
    #Diferencias
    for i in range(0, puntos - 1):
        encabezados.append("Δ^(" + str(i + 1) + ")yi")
        for j in range(0, puntos - 1 - i):
            #Δ^k yi = Δ^k-1 yi+1 - Δ^k yi
            deltayi = tabla[j + 1][i + 1] - tabla[j][i + 1]
            tabla[j].append(deltayi)
    
    if richardson == "1":
        for i in range(0, puntos - 1):
            for j in range(0, puntos - 1 - i):
                #Δ^k yi = Δ^k-1 yi+1 - Δ^k yi
                deltayi = tabla2[j + 1][i + 1] - tabla2[j][i + 1]
                tabla2[j].append(deltayi)

    #Calculo de k
    #k = (x - x0) / h
    k = (x - tabla[0][0]) / h
    if richardson == "1":
        k2 = (x - tabla2[0][0]) / h2

    #combinaciones
    #kCi = [k(k-1)...(k-i+1)]/i!
    combinaciones = []
    for i in range(1, puntos):
        combinacioni = sp.binomial(k, i)
        combinaciones.append(combinacioni)
    if richardson == "1":
        combinaciones2 = []
        for i in range(1, puntos):
            combinacioni = sp.binomial(k2, i)
            combinaciones2.append(combinacioni)

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

    if richardson == "1":
        interpolacion2 = 0
        for i in range(0, puntos):
            if i == 0:
                interpolacion2 = tabla2[0][1]
            else:
                interpolacion2 += combinaciones2[i - 1] * tabla2[0][i + 1]

        interpolacion2 = sp.expand_func(interpolacion2)
        interpolacion2 = sp.expand(interpolacion2)

    #Calculo de la derivada
    orden = obtenerOrden()
    derivada = sp.diff(interpolacion, x, orden)
    aproximacion = derivada.subs(x, valorInicial)
    derivada = derivada.xreplace({n: round(n, redondeo) for n in derivada.atoms(sp.Number)})
    if richardson == "1": 
        derivada2 = sp.diff(interpolacion2, x, orden)
        aproximacion2 = derivada2.subs(x, valorInicial)
        derivada2 = derivada2.xreplace({n: round(n, redondeo) for n in derivada2.atoms(sp.Number)})
    
    print("Tu tabla de datos: ")
    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))  
    print("Tu derivada simbolica en forma de polinomio es: " + str(derivada)) 
    print("El valor de la derivada en el punto " + str(valorInicial) + " es " + str((round(float(aproximacion), redondeo))))
    if richardson == "1":
        print("Tu segunda tabla de datos (h2): ")
        print(tabulate(tabla2, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))  
        print("Tu derivada simbolica en forma de polinomio es: " + str(derivada2)) 
        print("El valor de la derivada en el punto " + str(valorInicial) + " es " + str((round(float(aproximacion2), redondeo))))
        mejora = derivada2 + (derivada2 - derivada) / (((h/h2)**2) - 1)
        print("\nEl valor de la derivada mejorada con Richardson es " + str((round(float(mejora.subs(x, valorInicial)), redondeo))))
 

def integracionNumerica():

    #Recibimos datos iniciales
    redondeo = obtenerRedondeo()
    puntos = obtenerPuntos()

    #Tabla 
    encabezados = ["xi", "yi"]
    caso = obtenerPreguntaCaso("Deseas ingresar la funcion o los valores evaluados de la funcion? (1/2): ")

    f = obtenerFuncion() if caso == "1" else None
    tabla, h = obtenerTablaConstante(puntos, caso, f)

    h = tabla[1][0] - tabla[0][0]
    formula = obtenerPreguntaCaso("Quieres aproximar con integracion trapecial, Simpson 1/3 o Simpson 3/8? (1/2/3): ")

    integral = 0
    #trapecial
    if formula == "1":
        #y0 + yn
        integral =  tabla[0][1] + tabla[-1][1]
        #2sum(yi)
        for i in range(1, puntos - 1):
            integral += 2*tabla[i][1]
        #h/2
        integral *= h / 2

    #simpson 1/3
    elif formula == "2":
        #y0 + yn
        integral =  tabla[0][1] + tabla[-1][1]
        #4sum(yimpar)+2sum(ypar)
        for i in range(1, puntos - 1):
            if i % 2 == 0:
                integral += 2*tabla[i][1]
            else:
                integral += 4*tabla[i][1]
        #h/3
        integral *= h / 3
    
    #simpson 3/8
    elif formula == "3":
        #y0 + yn
        integral =  tabla[0][1] + tabla[-1][1]
        #2sum(ymult3)+3sum(yrestante)
        for i in range(1, puntos - 1):
            if i % 3 == 0:
                integral += 2*tabla[i][1]
            else:
                integral += 3*tabla[i][1]
        #3h/8
        integral *= (3 * h) / 8

    print("Tu tabla de datos: ")
    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))  
    print("El valor aproximado de tu integral en el intervalo [" + str(tabla[0][0]) + ", " + str(tabla[-1][0]) + "] es " + str(round(integral, redondeo)))


def integracionGaussiana():
    
    #Recibimos datos iniciales
    f = obtenerFuncion()
    a, b = obtenerIntervalo()
    redondeo = obtenerRedondeo()

    #grado
    grado = obtenerGrado()

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

def RK():
    
    #Formulas de RK
    def RK1(yi, xi, h, i, f):
        yTabla = []
        yTabla.append(yi)
        for _ in range (0, i):
            k1 = h * float(f.subs({x: xi, y: yi}))
            yi = yi + k1
            xi = xi + h
            yTabla.append(yi)
        return yTabla

    def RK2(yi, xi, h, i, f):
        yTabla = []
        yTabla.append(yi)
        for _ in range (0, i):
            k1 = h * float(f.subs({x: xi, y: yi}))
            k2 = h * float(f.subs({x: xi + h, y: yi + k1}))
            yi = yi + (1/2) * (k1 + k2)
            xi = xi + h
            yTabla.append(yi)
        return yTabla

    def RK3(yi, xi, h, i, f):
        yTabla = []
        yTabla.append(yi)
        for _ in range (0, i):
            k1 = h * float(f.subs({x: xi, y: yi}))
            k2 = h * float(f.subs({x: xi + 0.5*h, y: yi + 0.5*k1}))
            k3 = h * float(f.subs({x: xi + h, y: yi - k1 + 2*k2}))
            yi = yi + (1/6) * (k1 + 4*k2 + k3)
            xi = xi + h
            yTabla.append(yi)
        return yTabla

    def RK4(yi, xi, h, i, f):
        yTabla = []
        yTabla.append(yi)
        for _ in range (0, i):
            k1 = h * float(f.subs({x: xi, y: yi}))
            k2 = h * float(f.subs({x: xi + 0.5*h, y: yi + 0.5*k1}))
            k3 = h * float(f.subs({x: xi + 0.5*h, y: yi + 0.5*k2}))
            k4 = h * float(f.subs({x: xi + h, y: yi + k3})) 
            yi = yi + (1/6) * (k1 + 2*(k2 + k3) + k4)
            xi = xi + h
            yTabla.append(yi)
        return yTabla
    
    def EDAnalitica(f, x0, y0):

        #Construimos la ED
        funcion = sp.Function('y')(x) 
        fResolver = f.subs(y, funcion)
        ED = sp.Eq(funcion.diff(x), fResolver)
        
        #Intentamos resoverla
        try:
            condicionesIniciales = {funcion.subs(x, x0): y0}
            solucion = sp.dsolve(ED, funcion, ics=condicionesIniciales, simplify=False)
            print("\nTu ED si tiene solucion analitica")
            return solucion.rhs
        except NotImplementedError:
            print("\nSympy no pudo resolver esta ED analiticamente")
            return None

    def SolAnalitica(xi, i, fA):
        yTabla = []
        for _ in range(0, i+1):
            yi = fA.subs({x: xi})
            xi = xi + h
            yTabla.append(yi)
        return yTabla


    #recibimos la ED
    print("Acomoda tu ED de la forma y'=f(x,y)")
    f = obtenerFuncionDosVariables()

    print("Por ahora solo hay hasta RK4")
    #orden = 0
    #while orden > 4:
    #    orden = obtenerOrden()
    #    if orden > 4:
    #        print("Solo he programado hasta RK4 :(")

    #Datos iniciales
    print("Ingresa las condiciones iniciales")
    y0 = obtenerFlotante("Ingresa y0: ")
    x0 = obtenerFlotante("Ingresa x0: ")

    h = abs(obtenerFlotante("Ingresa el valor de h: "))
    redondeo = obtenerRedondeo()
    iteraciones = obtenerIteraciones()

    #Intentando resolver analiticamente
    analitica = EDAnalitica(f, x0, y0   )

    #tabla
    tabla = []
    encabezados = ["x", "yRK1", "yRK2", "yRK3", "yRK4"]
    #Si tiene solucion analitica, la obtenemos 
    if analitica != None: 
        encabezados.extend(["yA", "eRK1", "eRK2", "eRK3", "eRK4"])
        tYA = SolAnalitica(x0, y0, iteraciones, analitica)

    tRK1 = RK1(y0, x0, h, iteraciones, f)
    tRK2 = RK2(y0, x0, h, iteraciones, f)
    tRK3 = RK3(y0, x0, h, iteraciones, f)
    tRK4 = RK4(y0, x0, h, iteraciones, f)
    for i in range (0, iteraciones+1):
        tablai = [x0 + i*h, tRK1[i], tRK2[i], tRK3[i], tRK4[i]]
        #Con la solucion analitica comparamos los resultados de RK
        if analitica != None:
            tablai.extend([tYA[i], abs(tYA[i]-tRK1[i]), abs(tYA[i]-tRK2[i]), abs(tYA[i]-tRK3[i]), abs(tYA[i]-tRK4[i])])
        tabla.append(tablai)

    print("Tu tabla de datos: ")
    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))  
  
def RKVectorial():

    #Formulas de RK
    def RK1(xi, ti, h, iteraciones, sistema, orden):
        tabla = []
        tabla.append(list(xi))
        for _ in range (iteraciones):
            #Agregamos a un diccionario, los valores de las variables del vector
            diccionarioK1 = {t: ti}
            for i in range(0, orden):
                diccionarioK1[variables[i]] = xi[i]
            #Calculamos k1
            k1 = []
            for i in range(0, orden):
                k1.append(h * float(sistema[i].subs(diccionarioK1)))
            #Calculamos xi+1
            for i in range(0, orden):
                xi[i] = xi[i] + k1[i]
            #Incrementamos ti
            ti = ti + h
            tabla.append(list(xi))
        return tabla

    def RK2(xi, ti, h, iteraciones, sistema, orden):
        tabla = []
        tabla.append(list(xi))
        for _ in range (iteraciones):
            #Crearemos un diccionario para cada k, modificando sus valores de evaluacion
            diccionarioK1 = {t: ti}
            for i in range(0, orden):
                diccionarioK1[variables[i]] = xi[i]
            #Calculamos k1
            k1 = []
            for i in range(0, orden):
                k1.append(h * float(sistema[i].subs(diccionarioK1)))
            
            #Para k2
            diccionarioK2 = {t: ti + h}
            for i in range(0, orden):
                diccionarioK2[variables[i]] = xi[i] + k1[i]
            k2 = []
            for i in range(0, orden):
                k2.append(h * float(sistema[i].subs(diccionarioK2)))

            #Calculamos xi+1
            for i in range(0, orden):
                xi[i] = xi[i] + (1/2)*(k1[i]+k2[i])
            #Incrementamos ti
            ti = ti + h
            tabla.append(list(xi))
        return tabla

    def RK3(xi, ti, h, iteraciones, sistema, orden):
        tabla = []
        tabla.append(list(xi))
        for _ in range (iteraciones):
            #Crearemos un diccionario para cada k, modificando sus valores de evaluacion
            diccionarioK1 = {t: ti}
            for i in range(0, orden):
                diccionarioK1[variables[i]] = xi[i]
            #Calculamos k1
            k1 = []
            for i in range(0, orden):
                k1.append(h * float(sistema[i].subs(diccionarioK1)))
            
            #Para k2
            diccionarioK2 = {t: ti + 0.5 * h}
            for i in range(0, orden):
                diccionarioK2[variables[i]] = xi[i] + 0.5 * k1[i]
            k2 = []
            for i in range(0, orden):
                k2.append(h * float(sistema[i].subs(diccionarioK2)))

            #Para k3
            diccionarioK3 = {t: ti + h}
            for i in range(0, orden):
                diccionarioK3[variables[i]] = xi[i] - k1[i] + 2*k2[i]
            k3 = [] 
            for i in range(0, orden):
                k3.append(h * float(sistema[i].subs(diccionarioK3)))

            #Calculamos xi+1
            for i in range(0, orden):
                xi[i] = xi[i] + (1/6)*(k1[i] + 4*k2[i] + k3[i])
            #Incrementamos ti
            ti = ti + h
            tabla.append(list(xi))
        return tabla

    def RK4(xi, ti, h, iteraciones, sistema, orden):
        tabla = []
        tabla.append(list(xi))
        for _ in range (iteraciones):
            #Crearemos un diccionario para cada k, modificando sus valores de evaluacion
            diccionarioK1 = {t: ti}
            for i in range(0, orden):
                diccionarioK1[variables[i]] = xi[i]
            #Calculamos k1
            k1 = []
            for i in range(0, orden):
                k1.append(h * float(sistema[i].subs(diccionarioK1)))
            
            #Para k2
            diccionarioK2 = {t: ti + 0.5*h}
            for i in range(0, orden):
                diccionarioK2[variables[i]] = xi[i] + 0.5 * k1[i]
            k2 = []
            for i in range(0, orden):
                k2.append(h * float(sistema[i].subs(diccionarioK2)))

            #Para k3
            diccionarioK3 = {t: ti + 0.5*h}
            for i in range(0, orden):
                diccionarioK3[variables[i]] = xi[i] + 0.5*k2[i]
            k3 = [] 
            for i in range(0, orden):
                k3.append(h * float(sistema[i].subs(diccionarioK3)))
            
            #Para k4
            diccionarioK4 = {t: ti + h}
            for i in range(0, orden):
                diccionarioK4[variables[i]] = xi[i] + k3[i]
            k4 = [] 
            for i in range(0, orden):
                k4.append(h * float(sistema[i].subs(diccionarioK4)))

            #Calculamos xi+1
            for i in range(0, orden):
                xi[i] = xi[i] + (1/6)*(k1[i] + 2*k2[i] + 2*k3[i]+ k4[i])
            #Incrementamos ti
            ti = ti + h
            tabla.append(list(xi))
        return tabla

    #Datos iniciales
    orden, variables, sistema = obtenerSistemaEcuacionesDiferenciales()

    print("Por ahora solo hay hasta RK4")

    #Datos iniciales
    print("Ingresa las condiciones iniciales")
    t0 = obtenerFlotante("Ingresa t0: ")
    xIniciales = []
    #Vector inicial
    for i in range(0, orden):
        xi = obtenerFlotante("Ingresa x"+str(i+1) + " en t0: " )
        xIniciales.append(xi)
        
    h = abs(obtenerFlotante("Ingresa el valor de h: "))
    redondeo = obtenerRedondeo()
    iteraciones = obtenerIteraciones()

    tRK1 = RK1(list(xIniciales), t0, h, iteraciones, sistema, orden)
    tRK2 = RK2(list(xIniciales), t0, h, iteraciones, sistema, orden)
    tRK3 = RK3(list(xIniciales), t0, h, iteraciones, sistema, orden)
    tRK4 = RK4(list(xIniciales), t0, h, iteraciones, sistema, orden)
    
    #tabla
    tabla = []
    encabezados = ["t", "xRK1", "xRK2", "xRK3", "xRK4"]
   
    for i in range (0, iteraciones+1):
        vr1 = [round(num, redondeo) for num in tRK1[i]]
        vr2 = [round(num, redondeo) for num in tRK2[i]]
        vr3 = [round(num, redondeo) for num in tRK3[i]]
        vr4 = [round(num, redondeo) for num in tRK4[i]]
        tablai = [t0 + i*h, vr1, vr2, vr3, vr4]
        tabla.append(tablai)

    print("Tu tabla de datos: ")
    formato_decimales = f".{redondeo}f"
    print(tabulate(tabla, headers=encabezados, tablefmt="grid", floatfmt=formato_decimales))  

    
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
    print("8- Derivacion numerica con polinomios de Newton + Extrapolacion de Richardson")
    print("9- Integracion numerica (Trapecial, S.1/3, S.3/8)")
    print("10- Integracion numerica por Cuadratura Gaussiana")
    print("11- Runge-Kutta para ecuaciones diferenciales de orden 1")
    print("12- Runge-Kutta para ecuaciones diferenciales de orden n")
    print("0- Salir")
    print("----------------------------------------")
    
    opcion = obtenerEntero("Ingresa una opcion: ")

    if opcion == 0:
        print("Saliendoooooo.....")

    elif opcion == 1:
        print("\nElegiste método de bisección:\n")
        biseccion()

    elif opcion == 2:
        print("\nElegiste metodo de regla falsa:\n")
        reglaFalsa()
    
    elif opcion == 3:
        print("\nElegiste metodo de punto fijo:\n")
        puntoFijo()


    elif opcion == 4:
        print("\nElegiste metodo de Newton-Raphson:\n")     
        newtonRaphson()


    elif opcion == 5:
        print("\nElegiste metodo de Lin:\n")     
        lin()

    elif opcion == 6:
        print("\nElegiste interpolacion de Lagrange:\n")     
        polinomioLagrange()

    elif opcion == 7:
        print("\nElegiste interpolacion de Newton:\n")     
        polinomioNewton()

    elif opcion == 8:
        print("\nElegiste Derivacion Numerica:\n")     
        derivacionNumerica()

    elif opcion == 9:
        print("\nElegiste Integracion Numerica:\n")     
        integracionNumerica()
    
    elif opcion == 10:
        print("\nElegiste Integracion por Cuadratura Gaussiana:\n")     
        integracionGaussiana()

    elif opcion == 11:
        print("\nElegiste metodo de Runge-Kutta:\n")     
        RK()
    
    elif opcion == 12:
        print("\nElegiste Metodo de Runge-Kutta vectorial:\n")     
        RKVectorial()
    
    else:
        print("Ingresa el numero de alguna opcion")

        
