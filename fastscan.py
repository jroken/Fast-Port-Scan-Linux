import os
while True:
    os.system("cls")
    ip = input("Enter Website Or İp :  ")
    os.system(f"nmap {ip}")
    input("")
    os.system("cls")
