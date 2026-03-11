def load_csv_data(): 

    dataset = []

    while True:
        try:
            user_path = input("Please enter the full file path: ")
            file_path = user_path.strip('"').strip("'")

            with open(file_path, 'r', encoding='utf-8-sig') as file:

                headers = next(file).strip().split(',')
                print(f"Headers found: {headers}")

                for line in file:
                    clean_line = line.strip()
                    if not clean_line:
                        continue

                    text_values = clean_line.split(',')

                    numeric_row = []
                
                    for value in text_values:
                        numeric_row.append(float(value))

                    dataset.append(numeric_row)
            break

        except FileNotFoundError:
            print("File not found. Please check the path and try again.")
            

    return dataset, headers

## TESTING

if __name__ == "__main__":
    print("--- Testing data load ---")
    
    test_data = load_csv_data()
    
    print(test_data)

