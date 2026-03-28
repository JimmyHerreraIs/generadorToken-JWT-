from datetime import datetime

def log_event(evento: str, ip:str):
    with open("security_logs.txt", 'a') as apodo:
        apodo.write(f"{datetime.now()}- {ip} - {evento}\n")
# 2026-03-23 15:30:10.123456 - 192.168.1.5 - Login fallido