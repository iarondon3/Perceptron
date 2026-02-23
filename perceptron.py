import datos
import grafico

#FUNCIONES DE ACTIVACION

#FUNCION ESCALONADA

def funcion_escalonada(entrada):
    if entrada > 0:
        return 1
    else:
        return 0
    
        
#FUNCION SIGMOIDE

def funcion_sigmoide(entrada):
    euler = 2.718281828

    e_calculado = euler ** -entrada
    suma_total = 1 + e_calculado 
    valor_sigmoide = 1/suma_total

    # if valor_sigmoide > 0:
    #     return 1 
    # else:
    #     return 0

    return valor_sigmoide

#DEFINIR FUNCIONES

def definir_funcion_de_activacion():

    opcion_valida = False
    funcion_seleccionada = None
    
    while not opcion_valida:
        print('Funcion de activacion')
        print('1. Funcion Escalonada')
        print('2. Funcion Sigmoide')

        opcion = input('Selecciona una funcion de activacion ')

        if opcion == '1':
            funcion_seleccionada = funcion_escalonada
            break
        elif opcion == '2':
            funcion_seleccionada = funcion_sigmoide
            break
        else:
            print('Opcion no valida. Intente otra vez')
     
    return funcion_seleccionada

#DEFINIR PESOS

def definir_pesos(encabezados): 
    
        while True:
            try:
                b = float(input('Ingresa el valor del sesgo / bias '))
                break
            except ValueError:
                print('Inserta un valor valido')
        
        pesos = []
        
        for header in encabezados[:-1]:
            while True:
                try:
                    w = float(input(f'Ingresa el peso para la variable {header}: '))
                    pesos.append(w)
                    break
                except ValueError:
                    print('Inserta un valor valido')

        print("Pesos guardados", pesos, 'Sesgo guardado', b)

        return pesos, b 


#FUNNCION Z

def calcular_z(matriz_datos, encabezados, pesos, b, funcion_seleccionada):

    historial_inputs = []
    historial_esperados = []
    historial_predichos = []
    historial_errores = []  

    for fila in matriz_datos:
        z = b 
        entradas = (fila[:-1])
        valor_esperado = fila[-1]

        for dato, w in zip(entradas, pesos):
            z = z + (dato * w)

        prediccion = funcion_seleccionada(z)
        
        error = valor_esperado - prediccion

        print(f"Z: {z:.2f} | Esperado: {valor_esperado} -> Predicción: {prediccion:.1f}")

        historial_inputs.append(entradas)
        historial_esperados.append(valor_esperado)
        historial_predichos.append(prediccion)
        historial_errores.append(error)
    return historial_inputs, historial_esperados, historial_predichos, historial_errores, pesos, b, encabezados

#EJECUCION PERCEPTRON

def iniciar_perceptron(matriz, titulos, funcion_elegida):
    print('Iniciando Perceptron')

    lista_pesos, valor_b = definir_pesos(titulos)

    inputs, esperados, predichos, errores, pesos, b, encabezados = calcular_z(matriz, titulos, lista_pesos, valor_b, funcion_elegida)

    print("Calculo finalizado.")
       
    grafico.graficar_resultados(inputs, esperados, predichos, errores, pesos[0], pesos[1], b, encabezados[0], encabezados[1])
       
    return inputs, esperados, predichos, errores, pesos, b, encabezados
