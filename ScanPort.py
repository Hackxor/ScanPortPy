import socket
import subprocess

def nombre_puerto(puerto):
    try:
        nombre_servicio = socket.getservbyport(puerto)
        return nombre_servicio
    except OSError:
        return "Desconocido"

def escanear(direccion_ip, rango_inicial, rango_final):
    print(f"Escaneando puertos en {direccion_ip}... \n")
    for puerto in range(rango_inicial, rango_final + 1):
        conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexion.settimeout(3)  # Tiempo de espera para la conexión en segundos
        resultado = conexion.connect_ex((direccion_ip, puerto))
        if resultado == 0:
            nombre_servicio = nombre_puerto(puerto)
            print(f"Puerto {puerto}: ABIERTO - Servicio: {nombre_servicio}")
       
        conexion.close()

# entradas
bandera = True
while bandera == True:
    print('1. Explorar dispositivos en la red')
    print('2. Escanear un objetivo')
    print('3. Salir \n')
    opcion = int(input('Selecciona una opcion : '))
    if opcion == 1 :
        # Ejecutar un comando de Bash
        interfaz_red = input('Ingresa tu interfaz de red, ejemplo - eth0 : ')
        comando = f"sudo arp-scan -I {interfaz_red} --localnet"
        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        salida, error = proceso.communicate()
        # Imprimir la salida del comando
        print("Explorando hosts... \n")
        print(salida)

    elif opcion == 2 :
        direccion_ip = input("Ingresa la direccion ip local objetivo : ") 
        rango_inicio = 1
        rango_final = 1024
        escanear(direccion_ip, rango_inicio, rango_final)

    elif opcion == 3 :
        bandera = False
