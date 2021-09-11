import os
while True:
    os.system("clear")
    ip = input("Enter Website Or İp :  ")
    os.system(f"nmap {ip}")
    print("")
    print("Press enter to continue")
    input("")
    os.system("clear")
