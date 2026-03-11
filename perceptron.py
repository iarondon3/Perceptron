import data
import plots

# ACTIVATION FUNCTIONS

# STEP FUNCTION

def step_function(input_value):
    if input_value > 0:
        return 1
    else:
        return 0
    
        
# SIGMOID FUNCTION

def sigmoid_function(input_value):
    euler = 2.718281828

    calculated_e = euler ** -input_value
    total_sum = 1 + calculated_e 
    sigmoid_value = 1 / total_sum

    # if sigmoid_value > 0:
    #     return 1 
    # else:
    #     return 0

    return sigmoid_value

# SET FUNCTIONS

def set_activation_function():

    valid_option = False
    selected_function = None
    
    while not valid_option:
        print('Activation Function')
        print('1. Step Function')
        print('2. Sigmoid Function')

        option = input('Select an activation function: ')

        if option == '1':
            selected_function = step_function
            break
        elif option == '2':
            selected_function = sigmoid_function
            break
        else:
            print('Invalid option. Please try again.')
     
    return selected_function

# INITIALIZE WEIGHTS

def initialize_weights(headers): 
    
        while True:
            try:
                b = float(input('Enter the bias value: '))
                break
            except ValueError:
                print('Please enter a valid number.')
        
        weights = []
        
        for header in headers[:-1]:
            while True:
                try:
                    w = float(input(f'Enter the weight for variable {header}: '))
                    weights.append(w)
                    break
                except ValueError:
                    print('Please enter a valid number.')

        print("Saved weights:", weights, '| Saved bias:', b)

        return weights, b 


# Z FUNCTION

def calculate_z(data_matrix, headers, weights, b, selected_function):

    inputs_history = []
    expected_history = []
    predicted_history = []
    errors_history = []  

    for row in data_matrix:
        z = b 
        inputs = (row[:-1])
        expected_value = row[-1]

        for value, w in zip(inputs, weights):
            z = z + (value * w)

        prediction = selected_function(z)
        
        error = expected_value - prediction

        print(f"Z: {z:.2f} | Expected: {expected_value} -> Prediction: {prediction:.1f}")

        inputs_history.append(inputs)
        expected_history.append(expected_value)
        predicted_history.append(prediction)
        errors_history.append(error)
        
    return inputs_history, expected_history, predicted_history, errors_history, weights, b, headers

# RUN PERCEPTRON

def run_perceptron(data_matrix, headers, chosen_function):
    print('Starting Perceptron...')

    weights_list, b_value = initialize_weights(headers)

    inputs, expected, predicted, errors, weights, b, headers = calculate_z(data_matrix, headers, weights_list, b_value, chosen_function)

    print("Calculation finished.")
       
    plots.plot_results(inputs, expected, predicted, errors, weights[0], weights[1], b, headers[0], headers[1])
       
    return inputs, expected, predicted, errors, weights, b, headers