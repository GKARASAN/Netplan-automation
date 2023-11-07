import subprocess
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()

print("\n*** Showing IP address ***\n")
subprocess.run(["ip","addr"])

print("\n\n*** Collecting some data ***")
print(""" Make sure the given data is correct, 
    and if it is wrong, you can manually edit it or 
            run the program again.""")

Interface = input("\n\nEnter the interface : ")
IPadd = input("Enter the IP address with CIDR : ")
Gate = input("Enter Gateway address : ")

print("\nPlease wait few seconds...")

def Netplan(apply):

    file = open('00-network-manager-all.yaml', 'a')

    # Append new lines to the file
    file.write(" network:\n")
    file.write("    version: 2\n")
    file.write("    renderer: networkd\n")
    file.write("    ethernets:\n")
    file.write(f"     {Interface}:\n")
    file.write("      addresses:\n")
    file.write(f"        - {IPadd}\n")
    file.write(f"      gateway4: {Gate}\n")

    # Close the file
    file.close()

Netplan(apply=subprocess.run(["sudo","netplan","apply"]))

print("\nNetplan successfully configured")
