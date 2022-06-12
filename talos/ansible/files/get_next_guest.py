import sys
import yaml

guest_base = sys.argv[1]

with open('/tmp/talos_guests.yaml', 'r') as file:
    vm_guests = yaml.safe_load(file)
    
top_guest = 0
for guest in vm_guests:
    
    if guest['guest_name'].startswith(guest_base):
        try:
            if int(guest['guest_name'][-2:]) > top_guest:
                top_guest = int(guest['guest_name'][-2:])
        except ValueError:
            try:
                if int(guest['guest_name'][-1]) > top_guest:
                    top_guest = int(guest['guest_name'][-1])
            except ValueError:
                pass

guest_number = top_guest + 1

print(guest_base + str(guest_number))
