import tkinter as tk

def bayesCompleto():
    
    def seleccionar():
        
        for widget in subVentana.winfo_children():  
            widget.destroy()
        
        listaProbabilidades.clear()
        listaProbabilidadesCondicionales.clear()

        valor = int(texto.get())
        for i in range(0, valor):

            pATexto = tk.Label(subVentana, text = "P(A" + str(i+1) + ")= ")
            pA = tk.Entry(subVentana, width = 15)
            pATexto.grid(row = i, column = 0, padx = 3, pady = 6)
            pA.grid(row = i, column = 1, padx = 10, pady = 6)

            pABTexto = tk.Label(subVentana, text = "P(B|A" + str(i+1) + ")= ")
            pAB = tk.Entry(subVentana, width = 15)
            pABTexto.grid(row = i, column = 2, padx = 3, pady = 6)
            pAB.grid(row = i, column = 3, padx = 10, pady = 6)

            listaProbabilidades.append(pA)
            listaProbabilidadesCondicionales.append(pAB)

        textoSeleccion = tk.Label(subVentana, text = "Calcular bayes del \nconjunto A():")
        textoSeleccion.grid(row = valor, column = 0, columnspan=3, padx = 10, pady = 10)
        global seleccion
        seleccion = tk.Spinbox(subVentana, from_ = 1, to = 10, width = 5)
        seleccion.grid(row = valor, column = 1, columnspan = 4, padx = 10, pady = 10)
        
        boton = tk.Button(subVentana, text = "Calcular", command = leer)
        boton.grid(row=valor + 1 , column = 0, columnspan = 4, pady = valor + 10)

        regresar = tk.Button(subVentana, text = "Regresar", command = menu)
        regresar.grid(sticky = "e")


        global bayes
        bayes = int(seleccion.get())

    def leer():

        valor = int(texto.get())
        suma = 0

        for i in range(0, valor):

            entrada1 = listaProbabilidades[i].get()
            entrada2 = listaProbabilidadesCondicionales[i].get()
            
            
            if entrada1 == '' or entrada2 == '':
                error = tk.Label(ventana, text = "Sin datos suficientes")
                error.pack()
                return
            else:
                numero = float(entrada1)
                numero2 = float(entrada2)
                suma += numero

                if numero <= 0 or numero > 1 or numero2 <= 0 or numero2 > 1 or numero2 > numero:
                    error = tk.Label(ventana, text = "Datos invalidos")
                    error.pack()
                    return
                
        suma = round(suma)
        if suma != 1:
            error = tk.Label(ventana, text = "Datos invalidos, suma de probabilidad diferente a 1")
            error.pack()
            return
        
        for i in range(0, valor):
            numero = float(listaProbabilidades[i].get())
            numero2 = float(listaProbabilidadesCondicionales[i].get())
            listaProbabilidades[i] = numero
            listaProbabilidadesCondicionales[i] = numero2

        for widget in ventana.winfo_children():  
            widget.destroy() 

        ventanaResultados = tk.Frame(ventana)

        probabilidadTotal = 0


        for i in range(0, len(listaProbabilidades)):     
            
            

            probabilidadInterseccion = listaProbabilidades[i] * listaProbabilidadesCondicionales[i]
            pI = tk.Label(ventanaResultados, font = (20),text = "P(A" + str(i) + "∩B) = " + str(probabilidadInterseccion) + "\n P(A" + str(i) + "∩B') = " + str(listaProbabilidades[i]-probabilidadInterseccion))
            pI.grid(row = i, column = 0, padx = 10, pady = 6)
            probabilidadTotal += probabilidadInterseccion; 

        pTotal = tk.Label(ventanaResultados, font = (20), text = "Probabilidad Total P(B)= " + str(probabilidadTotal) + "\nProbabilidad Total Negada P(B')= " + str(1 - probabilidadTotal))
        pTotal.grid(row = 1, column = 1, padx = 10, pady = 6)

        probabilidadBayes = (listaProbabilidades[bayes] * listaProbabilidadesCondicionales[bayes]) / probabilidadTotal

        pBayes = tk.Label(ventanaResultados, font = (20), text = "Probabilidad Buscada P(B|A" + str(bayes) + ")= " + str(probabilidadBayes))
        pBayes.grid(row = 2, column = 1, padx = 10, pady = 6)
        
        ventanaResultados.pack(pady = 20)
        
        regresar = tk.Button(ventana, text = "Regresar", command = menu)
        regresar.pack()

        
                   

    for widget in ventana.winfo_children():  
        widget.destroy()

    listaProbabilidades = []
    listaProbabilidadesCondicionales = []

    cuanto = tk.Label(ventana, text = "Ingresa cuantos datos deseas calcular", pady = 20)
    texto = tk.Spinbox(ventana, from_ = 2, to = 10)
    aceptar = tk.Button(ventana, text = "Aceptar", command = seleccionar)

    subVentana = tk.Frame(ventana)
    subVentana.pack_propagate(False)    
    
    cuanto.pack()
    texto.pack()
    aceptar.pack()
    subVentana.pack(pady = 10)
    
    

def menu():

    for widget in ventana.winfo_children():  
        widget.destroy()

    elegir = tk.Label(ventana, text ="Cual es el caso que se te presenta?", font = (20))

    boton1 = tk.Button(ventana, text = "Bayes con todos los datos", command = bayesCompleto)
    boton2 = tk.Button(ventana, text = "Bayes con datos incompletos")

    elegir.pack(pady = 35)
    boton1.pack(pady = 15)
    boton2.pack(pady = 15)


ventana = tk.Tk()
ventana.geometry("900x700")
ventana.title("Teorema de Bayes")
ventana.resizable(False, False)
ventana.configure(bg = "gray")

menu()

ventana.mainloop()