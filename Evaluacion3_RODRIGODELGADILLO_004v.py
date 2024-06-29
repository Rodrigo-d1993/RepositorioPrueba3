import datetime
import json

# Catálogo de pizzas con sus precios según tamaño
Tipos_de_pizza = {"1": 6000,
                   "2": 5500,
                   "3": 7000}

# Registro de ventas (inicialmente vacío)
ventas = []

def Menu_ventas():
    print("""
1. Registrar una venta
2. Mostrar todas la ventas
3. Buscar venta por cliente
4. Guardar ventas en archivo
5. Cargar las ventas desde un archivo
6. Generar boleta
7. Anular venta
8. Salir del programa""")

def registrar_venta():
    pizzaTipo = input("\nElija el tipo de pizza:\n1.Hawaiana\n2.Napolitana\n3.Jamon y tocino\n : ")
    if pizzaTipo=="1":
        print("Registrado")
    elif pizzaTipo=="2":
        print("Registrado")
    elif pizzaTipo=="3":
        print("Registrado") 
    else:
        print("Pizza no existente")
        

    if pizzaTipo in Tipos_de_pizza:
        precio = Tipos_de_pizza	[pizzaTipo]
    else:
        print("Pizza no válido.")
        return
    
    tipo_cliente = input("\nIngrese el tipo de usuario (Estudiante/Trabajador,Socio): ").lower()
    descuento = 0.0

    if tipo_cliente == "estudiante":
        descuento = 0.15
    elif tipo_cliente == "trabajador":
        descuento = 0.10
    elif tipo_cliente == "administrativo":
        descuento = 0.20
    else:
        print("Tipo de usuario no válido.")
        return
    
    total_descuento = precio * descuento
    precio_final = precio - total_descuento

    venta = {
        "cliente": NombreUsu,
        "precio_final": precio_final,
        "fecha_hora": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    ventas.append(venta)
    print("Venta registrada satisfactoriamente.")
    
def mostrar_ventas():
    if ventas:
        for idx, venta in enumerate(ventas, start=1):
            print(f"\nVenta {idx}:")
            print(f"Cliente: {venta['cliente']}")
            print(f"Precio final: ${venta['precio_final']:.2f}")
            print(f"Fecha y hora: {venta['fecha_hora']}")
    else:
        print("No hay ventas registradas.")

def buscar_clientes():
    buscar=input("\nIngrese el nombre del Cliente: ")
    cliente_encontrado=False
    for venta in ventas:
        if venta["cliente"].lower()==buscar.lower():    
            print(f"\nCliente: {venta['cliente']}")
            print("-------------------------------------------")
            print(f"Compañia    : {venta['empresa']}")
            print(f"Consola     : {venta['consola']}")
            print(f"Genero      : {venta['genero']}")
            print(f"Juego       : {venta['juego']}")
            print("-------------------------------------------")
            cliente_encontrado=True
            break
    if not cliente_encontrado:
            print(f"Cliente {buscar} no tiene ningun pedido realizado.")

def guardar_datos():
    ruta_archivo='C:\\Users\\RODRIGO_D\\Desktop\\tienda\\ventas.json'

    with open(ruta_archivo, 'w') as file:
        json.dump(ventas, file, indent=4)
    print(f"Ventas guardadas en '{ruta_archivo}'.")

def cargar_datos():
    ruta_archivo='C:\\Users\\RODRIGO_D\\Desktop\\tienda\\ventas.json'
    try:
        with open(ruta_archivo, 'r') as file:
            global ventas
            ventas = json.load(file)
        print(f"ventas cargadas desde '{ruta_archivo}'.")
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")

def generar_boleta():
    boleta=input("\nIngrese el nombre del Cliente: ")
    for venta in ventas:
        if venta["cliente"].lower()==boleta.lower():    
            print("\n------------ Boleta de Venta -----------")
            print(f"Fecha y hora: {venta['fecha_hora']}")
            print(f"Cliente: {venta['cliente']}")
            print("----------------------------------------")
            print(f"Pizza    : {venta}")
            print(f"Precio final: ${venta['precio_final']:.2f}")
            print("----------------------------------------")
            cliente_encontrado=True
            break
    if not cliente_encontrado:
            print(f"Cliente {boleta} no tiene ningun pedido realizado.")

while True:
        Menu_ventas()
        opcion = input("\tOpción: ")

        if opcion == '1':
            registrar_venta()

        elif opcion == '2':
            mostrar_ventas()

        elif opcion == '3':
            buscar_clientes()  

        elif opcion == '4':
            guardar_datos()

        elif opcion == '5':
            cargar_datos()

        elif opcion == '6':
            generar_boleta()
        
        elif opcion == '7':
            print("Anulando compra...")
        
        elif opcion == '8':
            print("Saliendo del Programa...") 
            break          
        else:
            print("Opcion no valida...")