import matplotlib.pyplot as plt

def plot_results(inputs_list, expected_list, predicted_list, errors_list, w1, w2, b, x_label, y_label):

    x_axis = [row[0] for row in inputs_list]
    y_axis = [row[1] for row in inputs_list]

    colors = []
    for expected, error in zip(expected_list, errors_list):

        absolute_error = abs(error)

        if abs(expected) < 0.001:

            if absolute_error < 0.05:
                colors.append('green') 

            elif absolute_error < 0.15:
                colors.append('green') 

            else:
                colors.append('red')

    # IF THE EXPECTED VALUE IS NOT ZERO, CALCULATE THE ERROR PERCENTAGE

        else:
            error_percentage = absolute_error / abs(expected)

            if error_percentage < 0.05:
                colors.append('green')

            elif error_percentage < 0.15:
                colors.append('yellow')

            else:
                colors.append('red')

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

    line_x = []
    line_y = []
    

    if abs(w2) < 0.0001:
        print("Warning: w2 is almost 0. The line is vertical and might not display well.")
    else:
        x_min = min(x_axis) - 0.5 
        x_max = max(x_axis) + 0.5 
        
        line_x = [x_min, x_max]
        
        y_min = (-w1 * x_min - b) / w2
        y_max = (-w1 * x_max - b) / w2
        line_y = [y_min, y_max]

    line_style = {'color': 'black', 'linestyle': '--', 'linewidth': 2}

    # PLOT 1 - EXPECTED VALUE (ACTUAL)

    ax1.scatter(x_axis, y_axis, c=expected_list, cmap='coolwarm', s=100, edgecolors='k')
    if line_x: ax1.plot(line_x, line_y, **line_style)

    ax1.set_title("1. Expected Value (Actual)")
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label)
    ax1.grid(True, alpha=0.3)

    # PLOT 2 - PREDICTED VALUE (PERCEPTRON)
    ax2.scatter(x_axis, y_axis, c=predicted_list, cmap='coolwarm', s=100, edgecolors='k')
    if line_x: ax2.plot(line_x, line_y, **line_style)

    ax2.set_title("2. Predicted Value (Perceptron)")
    ax2.set_xlabel(x_label)
    ax2.set_ylabel(y_label)
    ax2.grid(True, alpha=0.3)

    # PLOT 3 - ERRORS
    ax3.scatter(x_axis, y_axis, c=colors, s=100, edgecolors='k')
    if line_x: ax3.plot(line_x, line_y, **line_style)

    ax3.set_title("3. Error Plot")
    ax3.set_xlabel(x_label)
    ax3.set_ylabel(y_label)
    ax3.grid(True, alpha=0.3)

    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='green', label='Low Error (<5%)'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='yellow', label='Medium Error (<15%)'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='red', label='High Error (>15%)'),
        Line2D([0], [0], color='black', linestyle='--', label='Boundary') 
    ]
    ax3.legend(handles=legend_elements)

    plt.tight_layout() 
    plt.show()



# import matplotlib.pyplot as plt

# def graficar_resultados(lista_inputs, lista_esperados, lista_predichos, lista_errores,  w1, w2, b, nombre_x, nombre_y):

#     eje_x = [fila[0] for fila in lista_inputs]
#     eje_y = [fila[1] for fila in lista_inputs]

#     colores = []
#     for esperados, errores in zip(lista_esperados, lista_errores):

#         distancia_error = abs(errores)

#         if abs(esperados) < 0.001:

#             if distancia_error < 0.05:
#                 colores.append('green') 

#             elif distancia_error < 0.15:
#                 colores.append('green') 

#             else:
#                 colores.append('red')

#     #SI EL VALOR ESPERADO NO ES CERO, CALCULO EL PORCENTAJE DE ERROR

#         else:
#             porcentaje_error = distancia_error / abs(esperados)

#             if porcentaje_error < 0.05:
#                 colores.append('green')

#             elif porcentaje_error < 0.15:
#                 colores.append('yellow')

#             else:
#                 colores.append('red')

#     fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

#     linea_x = []
#     linea_y = []
    

#     if abs(w2) < 0.0001:
#         print("Aviso: w2 es casi 0. La línea es vertical y podría no visualizarse bien.")
#     else:
#         x_min = min(eje_x) - 0.5 
#         x_max = max(eje_x) + 0.5 
        
#         linea_x = [x_min, x_max]
        
#         y_min = (-w1 * x_min - b) / w2
#         y_max = (-w1 * x_max - b) / w2
#         linea_y = [y_min, y_max]

#     estilo_linea = {'color': 'black', 'linestyle': '--', 'linewidth': 2}

#     #GRAFICO 1 - VALOR ESPERADO (REAL)

#     ax1.scatter(eje_x, eje_y, c=lista_esperados, cmap='coolwarm', s=100, edgecolors='k')
#     if linea_x: ax1.plot(linea_x, linea_y, **estilo_linea)

#     ax1.set_title("1. Valor Esperado (Real)")
#     ax1.set_xlabel(nombre_x)
#     ax1.set_ylabel(nombre_y)
#     ax1.grid(True, alpha=0.3)

#     #GRAFICO 2 - VALOR ESPERADO (PERCEPTRON)
#     ax2.scatter(eje_x, eje_y, c=lista_predichos, cmap='coolwarm', s=100, edgecolors='k')
#     if linea_x: ax2.plot(linea_x, linea_y, **estilo_linea)

#     ax2.set_title("2. Valor Predicho (Perceptrón)")
#     ax2.set_xlabel(nombre_x)
#     ax2.set_ylabel(nombre_y)
#     ax2.grid(True, alpha=0.3)

#     #GRAFICO 3 - ERRORES
#     ax3.scatter(eje_x, eje_y, c=colores, s=100, edgecolors='k')
#     if linea_x: ax3.plot(linea_x, linea_y, **estilo_linea)

#     ax3.set_title("3. Grafico de Errores")
#     ax3.set_xlabel(nombre_x)
#     ax3.set_ylabel(nombre_y)
#     ax3.grid(True, alpha=0.3)

#     from matplotlib.lines import Line2D
#     legend_elements = [
#         Line2D([0], [0], marker='o', color='w', markerfacecolor='green', label='Error Bajo (<5%)'),
#         Line2D([0], [0], marker='o', color='w', markerfacecolor='yellow', label='Error Medio (<15%)'),
#         Line2D([0], [0], marker='o', color='w', markerfacecolor='red', label='Error Alto (>15%)'),
#         Line2D([0], [0], color='black', linestyle='--', label='Frontera') 
#     ]
#     ax3.legend(handles=legend_elements)

#     plt.tight_layout() 
#     plt.show()