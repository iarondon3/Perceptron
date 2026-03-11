import perceptron
import datos

matriz, titulos = datos.cargar_datos_csv()

funcion_elegida = perceptron.definir_funcion_de_activacion()

def main():

    while True:
        perceptron.iniciar_perceptron(matriz, titulos, funcion_elegida)
             
        while True:
            pregunta = input("\n¿Deseas probar con otros pesos? Por favor escribe 's' o 'n' ").lower()
            
            if pregunta == 's':
                print("-" * 35)
                break  
            elif pregunta == 'n':
                print("Perceptron finalizado. Gracias!")
                return 
            else:
                print("Invalid option. Please type 'y' or 'n'.")

if __name__ == "__main__":
    main()