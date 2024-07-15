import re

# Regular expression pattern for IPv4 address
pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'

# Prompt user for input
ip_address = input("Enter an IPv4 address to validate: ")

# Check if the IP matches the pattern
match = re.match(pattern, ip_address)

if match:
    # Check each octet value
    valid_ip = True
    for octet in match.groups():
        if not (0 <= int(octet) <= 255):
            valid_ip = False
            break
    
    if valid_ip:
        print(f"{ip_address} is a valid IPv4 address.")
    else:
        print(f"{ip_address} is NOT a valid IPv4 address.")
else:
    print(f"{ip_address} is NOT a valid IPv4 ad
