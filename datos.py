def cargar_datos_csv(): 

    dataset = []

    while True:
        try:
            ruta_usuario = input("Por favor, ingresa la ruta completa del archivo ")
            ruta_del_archivo = ruta_usuario.strip('"').strip("'")

            with open(ruta_del_archivo, 'r', encoding='utf-8-sig') as archivo:

                titulos = next(archivo).strip().split(',')
                print(f"Encabezados encontrados: {titulos}")

                for linea in archivo:
                    linea_limpia = linea.strip()
                    if not linea_limpia:
                        continue

                    valores_texto = linea_limpia.split(',')

                    fila_numerica = []
                
                    for valor in valores_texto:
                        fila_numerica.append(float(valor))

                    dataset.append(fila_numerica)
            break

        except FileNotFoundError:
            print("No se encontro el archivo. Verifica la ruta e intenta de nuevo.")
            

    return dataset, titulos

##PRUEBA

if __name__ == "__main__":
    print("--- Probando carga de datos ---")
    
    mis_datos_prueba = cargar_datos_csv()
    
    print(mis_datos_prueba)