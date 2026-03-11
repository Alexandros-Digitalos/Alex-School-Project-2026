from network import Switch 


my_switch = Switch("devnet-switch")

while True:
    command = input(f"{my_switch.hostname}#")
    if command == "":
        continue
    elif command == "exit":
        break
    elif command == "show mac adress-table" or command == "show mac addr":
        my_switch.show_mac_address_table()
    else:
        print("            ^")
        print("Invalid Input Detected.")