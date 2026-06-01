#
# Simple port scanner using the socket library
# Author: @breakingpenji

# library imports
import socket
import re

# Banner
def banner():
    print('*******************************************************')
    print('\n\t\tSocket Scanner')
    print('\n*******************************************************')

# Main function
def main():
    banner()
    # Regulat expression pattern to recognize IPv4 addresses.
    ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

    # Regular expression pattern to recognize port ranges in the format "start-end".
    # For example, "20-80" would match ports 20 through 80.
    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
    
    # Define the minimum and maximum valid port numbers for validation purposes.
    # local variables
    port_min =0
    port_max = 65535
    open_ports = []

    # Prompt the user to enter a valid IP address and validate it using the regular expression pattern.
    while True:
        ip_add_entered = input("Enter the target IP address: ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"Valid IP address entered: {ip_add_entered}")
            break

    # Prompt the user to enter a valid port range and validate it using the regular expression pattern.
    while True:
        print("Please enter the range of ports you want to scan in format: <int>-<int> (e.g., 20-80)")
        port_range = input("Enter the port range: ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break

    # Looping over all ports in the specified range.
    for port in range(port_min, port_max + 1):
        try:
            # Attempt to create a socket connection to the target IP address and port.
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5) # Set a timeout for the connection attempt
                s.connect((ip_add_entered, port))
                # If the connection is successful, add the port to the list of open ports.
                open_ports.append(port)
        except:
            # If the connection attempt fails (e.g., the port is closed), we simply pass and continue to the next port.
            pass

    # Print the list of open ports found during the scan.
    for port in open_ports:
        print(f"Port {port} is open on {ip_add_entered}")

    # Option to output the results to a file
    output_choice = input("Do you want to save the results to a file? (y/n): ")
    if output_choice.lower() == 'y':
        with open(f"{ip_add_entered} open_ports.txt", "w") as f:
            for port in open_ports:
                f.write(f"Port {port} is open on {ip_add_entered}\n")
        print("Results saved to open_ports.txt")
    elif output_choice.lower() == 'n':
        print("Results not saved to a file.")
    else:
        print("Invalid choice. Results not saved to a file.")

if __name__ == "__main__":
    main()
