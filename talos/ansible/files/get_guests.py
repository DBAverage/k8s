import sys
import yaml

guest_base = sys.argv[1]

with open('/tmp/talos_guests.yaml', 'r') as file:
    vm_guests = yaml.safe_load(file)
    
guests = []
for guest in vm_guests:
    
    if guest['guest_name'].startswith(guest_base):
        guests.append(guest['guest_name'])

print(guests)