#
# Program to calculate ratio for upscaling 3D models.
# Program should also output new dimensions of the model based on the scaler factor.
# Program will ask user for desired total height of the model, and ask user for original heigh of the model.


def header():
    print('\n\n============================================')
    print('\t3D MODEL RATIO SCALER')
    print('============================================')
    print('\n\nThis program will help you calculate the ratio for upscaling your 3D model.')
    print('-----------------------------------------------------------------------------------')
    print('\nPlease answer the following questions to get an estimate of the new dimensions and percentage ratio:')
    print('')

# Function for calculating the scaler ratio based on the original height and desired height of the model.
def print_ratio_calc():
    # calculating desired height in feet and converting to inches for easier calculations
    # convert inches to feet for easier calculations
    desired_height = float(input("Enter the desired height of the model (in feet): "))
    # convert desired height from feet to inches
    converted_desired_height = desired_height * 12

    # calculating original height in inches or mm based on user input, and converting to inches if necessary
    height_unit = input("Is the original height in inches or mm? (Enter 'inches' or 'mm'): ").strip().lower()
    if height_unit == 'mm':
        original_height = float(input("Enter the original height of the model (in mm): "))
        # convert original height from mm to inches
        converted_original_height = original_height / 25.4
        original_height = converted_original_height
    elif height_unit == 'inches':
        original_height = float(input("Enter the original height of the model (in inches): "))
    else:
        print("Invalid input. Please enter 'inches' or 'mm'.")
        return print_ratio_calc()

    desired_height = converted_desired_height

    ratio = desired_height / original_height
    percentage = ratio * 100

    print(f"\nThe scaling ratio is: {ratio:.2f}")
    print(f"The percentage increase is: {percentage:.2f}%")

    calculate_again()

# Main function to run the program and call the ratio calculation functions.
def calculate_again():
    while True:
        again = input("\nDo you want to calculate another ratio? (yes/no): ").strip().lower()
        if again == 'yes':
            print_ratio_calc()
        elif again == 'no':
            print("Thank you for using the 3D Model Ratio Scaler. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    header()
    print_ratio_calc()

if __name__ == "__main__":
    main()