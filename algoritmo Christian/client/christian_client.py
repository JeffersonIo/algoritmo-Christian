import requests
import time
from datetime import datetime

def synchronize_time(server_url):
    # Paso 1: Marca el tiempo de salida (T1)
    T1 = time.time()

    # Paso 2: Solicita la hora al servidor
    response = requests.get(f"{server_url}/time")
    T_server = response.json()['server_time']

    # Paso 3: Marca el tiempo de llegada (T2)
    T2 = time.time()

    # Paso 4: Calcula el tiempo ajustado para el cliente
    T_client = T_server + ((T2 - T1) / 2)

    print(f"Hora del servidor: {datetime.utcfromtimestamp(T_server)} UTC")
    print(f"Hora ajustada del cliente: {datetime.utcfromtimestamp(T_client)} UTC")
    return T_client

if __name__ == '__main__':
    server_url = "http://time_server:5000"  # URL del servidor de tiempo en Docker Compose
    synchronize_time(server_url)
