# 
# Design a program to calculate the appx. cost a civil or criminal case will be.
# Should output: Est. hours, Est. total cost.
# Take into consideration discovery amount, travel, interviewing, forensic work, and etc.


# Import necessary libraries
import sys # Importing sys to use sys.exit() for exiting the program gracefully

# GLOABAL VARIABLES
HOURLY_RATE = 225  # Average hourly rate for attorneys, can be adjusted based on location and experience
TRIAL_APPEARANCE_RATE = 300  # Additional hourly rate for trial appearances, can be adjusted based on location and experience
TRAVEL_COST = 0
DISCOVERY_COST = 0
INTERVIEW_COST = 0
FORENSIC_COST = 0
SURVEILLANCE_COST = 0


# Function for start up and instructions
def start_up_menu():
     print('\n\n============================================')
     print('\tSILR CASE COST ESTIMATOR')
     print('============================================')
     print('\n\nThis program will help you estimate the cost of a civil or criminal case.')
     print('-----------------------------------------------------------------------------------')
     

# Function for case type selection (i.e. civil or criminal case, and etc.)
def case_type_menu():
    print('\n\nPlease select the type of case you want to estimate the cost for:')
    print('1). Civil Case')
    print('2). Criminal Case')
    case_type_choice = input('\nEnter your choice (1 or 2): ').strip()
    print('-----------------------------------------------------------------------------------')
    if case_type_choice == '1':
        return 'civil'
    elif case_type_choice == '2':
        return 'criminal'
    else:
        print('Invalid choice. Please enter "1" for Civil Case or "2" for Criminal Case.')
        return case_type_menu()
        

# Selection Menu for cost calulations
def cost_calculation_menu():
    print('\nPlease select "Calculate Costs" to proceed with cost estimation:')
    print('1). Calculate Costs')
    print('2). Display Estimation Summary')
    print('3). Exit')


# Function for cost calculation (i.e. travel, discovery, interviewing, forensic work, and etc.)
def cost_calculator():
    # mileage rate variable
    mileage_rate = .71  # Average mileage rate for travel, can be adjusted based on location and current IRS rates

    # user input for each cost component
    # Travel cost calculation
    miles_traveled = float(input('\nEnter the estimates miles we may travel for the case: '))
    travel_hours = float(input('Enter the estimated hours spent on travel: '))
    TRAVEL_COST = (mileage_rate * miles_traveled) + (HOURLY_RATE * travel_hours)
    print(f'\nTravel Cost: ${TRAVEL_COST:.2f}')

    # discovery cost calculation
    discovery_hours = float(input('\nEnter the estimated hours spent on discovery: '))
    DISCOVERY_COST = HOURLY_RATE * discovery_hours
    print(f'\nDiscovery Cost: ${DISCOVERY_COST:.2f}')

    # interview cost calculation
    interview_hours = float(input('\nEnter the estimated hours spent on interviewing: '))
    INTERVIEW_COST = HOURLY_RATE * interview_hours
    print(f'\nInterviewing Cost: ${INTERVIEW_COST:.2f}')

    # forensic work cost calculation
    forensic_hours = float(input('\nEnter the estimated hours spent on forensic work: '))
    FORENSIC_COST = HOURLY_RATE * forensic_hours
    print(f'\nForensic Work Cost: ${FORENSIC_COST:.2f}')

    # surveillance cost calculation
    surveillance_hours = float(input('\nEnter the estimated hours spent on surveillance: '))
    SURVEILLANCE_COST = HOURLY_RATE * surveillance_hours  
    print(f'\nSurveillance Cost: ${SURVEILLANCE_COST:.2f}')

    # Total cost estimation
    print('\n--------------------------------------------------------------------------------')
    print('\nCalculating total estimated cost...')
    total_cost = TRAVEL_COST + DISCOVERY_COST + INTERVIEW_COST + FORENSIC_COST + SURVEILLANCE_COST
    print(f'\nTotal Estimated Cost: ${total_cost:.2f}')

    # Retainer fee calculation
    retainer_fee = total_cost * 0.25  # Assuming retainer fee is 25% of total cost
    print(f'Retainer Fee: ${retainer_fee:.2f}')
    print('\n------------------------------------------------------------------------------------')    

    return total_cost, retainer_fee


# Function to display estimation summary (i.e. case type, total cost, retainer fee, and etc.)
def display_estimation(case_type, total_cost, retainer_fee):
    print('\n\n============================================')
    print('\tSILR CASE COST ESTIMATION SUMMARY')
    print('============================================')
    print(f'\nCase Type: {case_type.capitalize()}')
    print(f'\nTotal Estimated Cost: ${total_cost:.2f}')
    print(f'Retainer Fee: ${retainer_fee:.2f}')
    print('\nPlease note that these are estimates and actual costs may vary based on specifics of the case and any unforeseen circumstances.')

    exit()  # Call continue function to ask user if they want to perform another estimation or exit the program


# Continue Function for case type selection (i.e. civil or criminal case, and etc.)
def exit():
    while True:
        continue_choice = input('\nDo you want to perform another estimation? (yes/no): ').strip().lower()
        if continue_choice == 'yes':
            main()
            break
        elif continue_choice == 'no':
            print('Thank you for using the SILR Case Cost Estimator. Goodbye!')
            sys.exit()
        else:
            print('Invalid choice. Please enter "yes" or "no".')


# Function for total cost estimation (i.e. sum of all costs, and etc.)
def main():
    start_up_menu()
    total_cost = 0
    retainer_fee = 0
    case_type = None
    keep_going = 'yes'
    while keep_going == 'yes':
        cost_calculation_menu()
        choice = input('\nEnter your choice (1, 2, or 3): ').strip()
        if choice == '1':
            case_type = case_type_menu()
            total_cost, retainer_fee = cost_calculator()
        elif choice == '2':
            if case_type is not None:
                display_estimation(case_type, total_cost, retainer_fee)
            else:
                print('Please calculate costs first by selecting option 1.')
                print('-----------------------------------------------------------------------------------')
        elif choice == '3':
            keep_going = exit()
        else:
            print('Invalid choice. Please enter "1", "2", or "3".')


# Call functions to calculate each cost component and sum them up for total cost estimation
if __name__ == "__main__":
    main()

