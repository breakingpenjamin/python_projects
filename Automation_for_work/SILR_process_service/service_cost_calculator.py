#
# Process Service Cost Calculator Program
# This program calculates the total cost of a service based on user input.

def calculate_total_cost():
    # Local Variables
    service_cost = 85.0
    total_cost = 0.0
    rush_fee = 55.0
    mileage_multiplier = 0.7

    print("\nList of Service Types:")
    print("\n- Standard Service")
    print("- Subpoena")
    print("- Rush Service")

    service_type = input("Enter the type of service: ")
    if service_type.lower() == "standard service":
        total_cost = service_cost
    elif service_type.lower() == "subpoena":
        total_cost = service_cost + 10.0
    elif service_type.lower() == "rush service":
        total_cost = service_cost + rush_fee
    else:
        print("Invalid service type entered.")
        return
    
    distance = float(input("Enter the distance to be traveled (in miles): "))
    total_cost += (distance *2 ) * mileage_multiplier
    print(f"The total cost of the service is: ${total_cost:.2f}")

def banner():
    print("==========================================================")
    print("\n\t ---- Process Service Cost Calculator ----")
    print("\t---- SILR FORENSIC INVESTIGATIONS, LLC ----")
    print("\n==========================================================")

if __name__ == "__main__":
    banner()
    calculate_total_cost()