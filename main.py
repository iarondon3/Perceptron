import perceptron
import data

data_matrix, headers = data.load_csv_data()

chosen_function = perceptron.set_activation_function()

def main():

    while True:
        perceptron.run_perceptron(data_matrix, headers, chosen_function)
             
        while True:
            question = input("\nDo you want to try with different weights? Please type 'y' or 'n': ").lower()
            
            if question == 'y':
                print("-" * 35)
                break  
            elif question == 'n':
                print("Perceptron finished. Thank you!")
                return 
            else:
                print("Invalid option. Please type 'y' or 'n'.")

if __name__ == "__main__":
    main()