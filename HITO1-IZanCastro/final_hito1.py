import random
import string
# Definir la estructura de datos para clientes y compras
clientes = []   # Lista para almacenar información de clientes
compras = []    # Lista para almacenar información de compras
metodo_busqueda = None  # Definir la variable metodo_busqueda globalmente

# Función para cargar el último ID de cliente desde el archivo de texto
def cargar_ultimo_id_cliente():
    try:
        with open("ultimo_id_cliente.txt", "r") as archivo:
            ultimo_id = int(archivo.read())
            return ultimo_id
    except FileNotFoundError:
        return 1  # Si el archivo no existe, comenzar desde el ID 1

# Función para guardar el último ID de cliente en el archivo de texto
def guardar_ultimo_id_cliente(cliente_id):
    with open("ultimo_id_cliente.txt", "w") as archivo:
        archivo.write(str(cliente_id))

# Función para comprobar si el ID del cliente está duplicado en la lista de clientes
def cliente_id_duplicado(cliente_id):
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return True
    return False

# Función para generar un ID único para el cliente
def generar_cliente_id_unico():
    ultimo_id = cargar_ultimo_id_cliente()
    nuevo_id = ultimo_id
    while True:
        nuevo_id += 1
        if not cliente_id_duplicado(nuevo_id):
            return nuevo_id

# Función para registrar un cliente
def registrar_cliente():
    print("Registro de Cliente")
    nombre = input("Nombre: ")
    email = input("Correo electrónico: ")
    telefono = input("Número de teléfono: ")  # Nuevo campo para el número de teléfono
    direccion = input("Dirección de facturación: ")
    nacionalidad = input("Nacionalidad: ")

    # Cargar el último ID de cliente desde el archivo
    cliente_id = cargar_ultimo_id_cliente()

    # Generar un nuevo ID único para el cliente
    nuevo_id = generar_cliente_id_unico()

    # Crear un diccionario con la información del cliente
    cliente = {
        "id": nuevo_id,
        "nombre": nombre,
        "email": email,
        "telefono": telefono,  # Nuevo campo para el número de teléfono
        "direccion": direccion,
        "nacionalidad": nacionalidad
    }

    # Agregar el cliente a la lista de clientes
    clientes.append(cliente)
    guardar_clientes()  # Supongo que existe una función guardar_clientes() para guardar la lista de clientes

    # Actualizar el último ID con el nuevo ID generado
    cliente_id = nuevo_id
    guardar_ultimo_id_cliente(cliente_id)

    print("Cliente registrado con éxito. ID del cliente:", cliente["id"])

# Función para guardar la lista de clientes en un archivo de texto
def guardar_clientes():
    with open("clientes.txt", "w") as archivo:
        for cliente in clientes:
            archivo.write(f"ID: {cliente['id']}, Nombre: {cliente['nombre']}, Email: {cliente['email']}, Dirección: {cliente['direccion']}, Nacionalidad: {cliente['nacionalidad']}\n")

# Función para cargar clientes desde un archivo de texto
# Función para cargar clientes desde un archivo de texto
def cargar_clientes():
    try:
        with open("clientes.txt", "r") as archivo:
            for line in archivo:
                partes = line.strip().split(", ")
                if len(partes) == 5:
                    # Si la línea tiene exactamente 5 partes, se procede a crear un diccionario para representar al cliente
                    cliente = {
                        "id": int(partes[0].split(": ")[1]),          # Obtener el ID del cliente y convertirlo a entero
                        "nombre": partes[1].split(": ")[1],           # Obtener el nombre del cliente
                        "email": partes[2].split(": ")[1],            # Obtener el correo electrónico del cliente
                        "direccion": partes[3].split(": ")[1],        # Obtener la dirección del cliente
                        "nacionalidad": partes[4].split(": ")[1]      # Obtener la nacionalidad del cliente
                    }
                    clientes.append(cliente)
    except FileNotFoundError:
        print("Error: El archivo 'clientes.txt' no se encuentra.")
    except Exception as e:
        print(f"Error al cargar clientes: {e}")

# Función para visualizar todos los clientes
def visualizar_clientes():
    if not clientes:
        print("No hay clientes registrados.")
    else:
        print("Clientes Registrados:")
        for cliente in clientes:
            # Utilizar get para manejar la posibilidad de que 'telefono' no esté presente
            telefono = cliente.get('telefono', 'N/A')
            print(f"ID: {cliente['id']}, Nombre: {cliente['nombre']}, Email: {cliente['email']}, Teléfono: {telefono}, Dirección: {cliente['direccion']}, Nacionalidad: {cliente['nacionalidad']}")

# Función para buscar clientes por criterios
def buscar_clientes():
    global metodo_busqueda  # Acceder a la variable global

    if metodo_busqueda is None:
        print("Método de búsqueda:")
        print("1. Por ID")
        print("2. Por Nombre")
        print("3. Por Email")
        opcion_metodo = input("Seleccione el método de búsqueda (1/2/3): ")

        if opcion_metodo not in ["1", "2", "3"]:
            print("Método de búsqueda no válido.")
            return

        metodo_busqueda = opcion_metodo  # Almacenar el método de búsqueda globalmente

    valor = input("Introduce el valor a buscar: ")

    if metodo_busqueda == "1":
        resultados = [cliente for cliente in clientes if valor == str(cliente.get("id", ""))]
    elif metodo_busqueda == "2":
        resultados = [cliente for cliente in clientes if valor.lower() in cliente.get("nombre", "").lower()]
    elif metodo_busqueda == "3":
        resultados = [cliente for cliente in clientes if valor.lower() in cliente.get("email", "").lower()]

    if not resultados:
        print("No se encontraron clientes con los criterios proporcionados.")
    else:
        print("Clientes Encontrados:")
        for cliente in resultados:
            print(f"ID: {cliente['id']}, Nombre: {cliente['nombre']}, Email: {cliente['email']}, Dirección: {cliente['direccion']}, Nacionalidad: {cliente['nacionalidad']}")

# Función para buscar un cliente por ID
def buscar_cliente_por_id(cliente_id):
    cliente_id = int(cliente_id)  # Convertir a entero para comparar con los IDs en la lista
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return cliente
    return None

# Función para cargar productos desde un archivo de texto
def cargar_productos():
    productos = []
    try:
        with open("productos.txt", "r") as archivo:
            for line in archivo:
                partes = line.strip().split(", ")
                nombre = partes[0]
                # Excluir la palabra "Precio:" antes de convertir a float
                precio = float(partes[1].split(": ")[1].replace("$", ""))
                productos.append({"nombre": nombre, "precio": precio})
    except FileNotFoundError:
        print("Error: El archivo 'productos.txt' no se encuentra.")
    except Exception as e:
        print(f"Error al cargar productos: {e}")
    return productos

# Función para obtener el precio de un producto
def ver_productos_disponibles():
    productos = cargar_productos()
    if not productos:
        print("No hay productos disponibles.")
    else:
        print("Productos Disponibles:")
        for producto in productos:
            print(f"Producto: {producto['nombre']}, Precio: ${producto['precio']}")

# Función para obtener la tasa de impuesto según la nacionalidad
def obtener_tasa_impuesto(nacionalidad):
    try:
        with open("impuestos.txt", "r") as archivo:
            for line in archivo:
                pais, tasa = line.strip().split(": ")
                if pais.lower() == nacionalidad.lower():
                    return float(tasa)
    except FileNotFoundError:
        print("Error: El archivo 'impuestos.txt' no se encuentra.")
    except Exception as e:
        print(f"Error al cargar impuestos: {e}")
    return 0.0  # Si hay algún problema, se asume un impuesto del 0%

# ...

def realizar_compra():
    print("Realizar Compra")
    if not clientes:
        print("No hay clientes registrados. Debe registrar un cliente antes de realizar una compra.")
        return

    # Mostrar los clientes disponibles
    visualizar_clientes()

    id_cliente = input("Ingrese el ID del cliente que realiza la compra: ")
    cliente = buscar_cliente_por_id(id_cliente)

    if cliente is None:
        print("Cliente no encontrado. Por favor, ingrese un ID de cliente válido.")
        return

    # Obtener la nacionalidad del cliente
    nacionalidad_cliente = cliente.get("nacionalidad", "").strip()

    # Informar al cliente sobre el impuesto aplicable o la exención de impuestos
    tasa_impuesto = obtener_tasa_impuesto(nacionalidad_cliente)
    if tasa_impuesto > 0:
        print(f"Debido a su nacionalidad ({nacionalidad_cliente}), se aplicará un impuesto del {tasa_impuesto * 100}% a su compra.")
    else:
        print(f"No se aplicarán impuestos a su compra debido a su nacionalidad ({nacionalidad_cliente}).")

    # Mostrar los productos disponibles antes de ingresar los productos en la compra
    ver_productos_disponibles()

    compra = {
        "cliente": cliente,
        "productos": []
    }

    while True:
        producto_nombre = input("Ingrese el nombre del producto (o 'terminar' para finalizar la compra): ")
        if producto_nombre.lower() == "terminar":
            break

        # Verificar si el producto ingresado está en la lista de productos disponibles
        precio_producto = obtener_precio_producto(producto_nombre)

        if precio_producto is not None:
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad de este producto: "))
                    print(f"Se han comprado {cantidad} unidades del producto: {producto_nombre}")
                    break  # Sale del bucle si la conversión es exitosa
                except ValueError:
                    print("Error: Debes ingresar un número entero para la cantidad.")

            compra["productos"].append({"nombre": producto_nombre, "cantidad": cantidad})
        else:
            print("Producto no encontrado en la lista de productos disponibles. Inténtelo de nuevo.")

    if not compra["productos"]:
        print("La compra no tiene productos. No se ha realizado la compra.")
        return

    # Calcular el total de la compra incluyendo impuestos
    total_sin_impuesto = calcular_total_compra(compra)
    impuesto = total_sin_impuesto * tasa_impuesto
    total_con_impuesto = total_sin_impuesto + impuesto

    compra["total"] = total_con_impuesto


    # Generar y asignar el código de seguimiento
    codigo_seguimiento = generar_codigo_seguimiento()
    compra["codigo_seguimiento"] = codigo_seguimiento

    # Mensaje adicional con el impuesto añadido o la exención de impuestos
    compras.append(compra)
    guardar_compras()  # Agregar esta línea para guardar las compras con el código de seguimiento
    print("Compra realizada con éxito.")
    if tasa_impuesto > 0:
        print(
            f"Debido a su nacionalidad ({nacionalidad_cliente}), se aplicará un impuesto del {tasa_impuesto * 100}% a su compra.")
        print(f"Impuesto añadido: ${impuesto:.2f}")
    else:
        print("No se aplicaron impuestos a la compra.")

    # Llamar a la función de seguimiento justo después de imprimir el mensaje de éxito
    seguimiento_compra(compra)

    input("Presione Enter para continuar...")
# Función para calcular el total de una compra
def calcular_total_compra(compra):
    total = 0
    for producto in compra["productos"]:
        # Obtener el precio del producto desde la función obtener_precio_producto
        precio_producto = obtener_precio_producto(producto["nombre"])
        total += precio_producto * producto["cantidad"]
    return total

# Función para obtener el precio de un producto
def obtener_precio_producto(producto_nombre):
    productos_disponibles = cargar_productos()
    producto_nombre = producto_nombre.lower().strip()  # Convertir a minúsculas y eliminar espacios en blanco
    for producto in productos_disponibles:
        if producto["nombre"].lower() == producto_nombre:
            return producto["precio"]
    # Devolver None si el producto no se encuentra
    return None

# Función para guardar las compras en un archivo de texto
def guardar_compras():
    with open("compras.txt", "a") as archivo:
        nueva_compra = compras[-1]  # Obtener la última compra agregada
        cliente = nueva_compra["cliente"]
        productos = nueva_compra["productos"]
        total = nueva_compra["total"]
        codigo_seguimiento = nueva_compra.get("codigo_seguimiento", "")  # Obtener el código de seguimiento si existe

        archivo.write(f"{cliente['nombre']}:{cliente['id']}|")
        for producto in productos:
            archivo.write(f"{producto['nombre']}:{producto['cantidad']}|")
        archivo.write(f"{total}|{codigo_seguimiento}\n")

# Función para cargar compras desde un archivo de texto
def cargar_compras():
    compras.clear()  # Limpiar la lista de compras antes de cargar desde el archivo
    try:
        with open("compras.txt", "r") as archivo:
            lineas = archivo.readlines()
            i = 0
            while i < len(lineas):
                # Obtener información del cliente desde la línea correspondiente
                cliente_linea = lineas[i].strip().split(":")
                cliente_nombre = cliente_linea[0]
                cliente_id = int(cliente_linea[1])

                productos = []
                i += 1  # Moverse a la línea de productos
                while "Total:" not in lineas[i]:
                    # Obtener información de cada producto en la compra
                    producto_linea = lineas[i].strip().split(":")
                    producto_nombre = producto_linea[0]
                    producto_cantidad = int(producto_linea[1])
                    productos.append({"nombre": producto_nombre, "cantidad": producto_cantidad})
                    i += 1

                total = float(lineas[i].strip()[7:])
                i += 1  # Moverse a la línea de código de seguimiento
                codigo_seguimiento = lineas[i].strip().split(":")[1].strip()

                i += 2  # Moverse a la línea "----"
                # Construir el diccionario de la compra
                compra = {
                    "cliente": {"nombre": cliente_nombre, "id": cliente_id},
                    "productos": productos,
                    "total": total,
                    "codigo_seguimiento": codigo_seguimiento
                }
                compras.append(compra)
                i += 1  # Moverse a la siguiente línea después de "----"
    except FileNotFoundError:
        print("Error: El archivo 'compras.txt' no se encuentra.")
    except Exception as e:
        print(f"Error al cargar compras: {e}")
# Función para generar un código de seguimiento único
def generar_codigo_seguimiento():
    longitud_codigo = 10
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud_codigo))

# Función para enviar SMS al cliente
def enviar_sms(cliente, mensaje):
    # Aquí puedes implementar el envío de un mensaje SMS al cliente
    print(f"SMS enviado al número de teléfono del cliente {cliente['nombre']}: {mensaje}")

# Función para enviar correo al cliente
def enviar_correo(cliente, mensaje):
    # Aquí puedes implementar el envío de un correo electrónico al cliente
    print(f"Correo electrónico enviado a {cliente['nombre']} ({cliente['email']}): {mensaje}")

# Función para realizar el seguimiento de una compra
def seguimiento_compra(compra):
    # Generar un código de seguimiento único
    codigo_seguimiento = generar_codigo_seguimiento()

    # Mensaje de seguimiento que incluye el código de seguimiento
    mensaje = f"Su pedido con código de seguimiento {codigo_seguimiento} está en proceso."

    # Simular el envío de SMS
    enviar_sms(compra["cliente"], mensaje)

    # Simular el envío de correo electrónico
    enviar_correo(compra["cliente"], mensaje)

    # Asignar el código de seguimiento a la compra
    compra["codigo_seguimiento"] = codigo_seguimiento


    print("Compra realizada con éxito.")
    print(f"Código de Seguimiento: {codigo_seguimiento}")
    print("Mensaje de seguimiento enviado por SMS y correo electrónico.")

# Función para cargar compras desde un archivo de texto
def cargar_compras_desde_archivo():
    compras_desde_archivo = []
    try:
        with open("compras.txt", "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split("|")

                if len(partes) >= 3:  # Asegurarse de que haya al menos tres partes
                    cliente_partes = partes[0].split(":")
                    cliente_nombre = cliente_partes[0]
                    cliente_id = int(cliente_partes[1])

                    productos_partes = partes[1:-2]  # Excluir el total y el código de seguimiento
                    productos = []
                    for producto_parte in productos_partes:
                        producto_info = producto_parte.split(":")
                        producto_nombre = producto_info[0]
                        producto_cantidad = int(producto_info[1])
                        productos.append({"nombre": producto_nombre, "cantidad": producto_cantidad})

                    total = float(partes[-2])  # Último elemento antes del código de seguimiento
                    codigo_seguimiento = partes[-1] if partes[-1] else None

                    compra = {"cliente": {"nombre": cliente_nombre, "id": cliente_id},
                              "productos": productos, "total": total,
                              "codigo_seguimiento": codigo_seguimiento}
                    compras_desde_archivo.append(compra)
                else:
                    print(f"Advertencia: Se omitió la línea incorrecta en el archivo: {linea.strip()}")
    except FileNotFoundError:
        print("Error: El archivo 'compras.txt' no se encuentra.")
    except Exception as e:
        print(f"Error al cargar compras: {e}")

    return compras_desde_archivo

# Función para visualizar todas las compras
def visualizar_compras():
    compras_desde_archivo = cargar_compras_desde_archivo()

    if not compras_desde_archivo:
        print("No hay compras registradas.")
        return

    print("Compras Realizadas:")
    for compra in compras_desde_archivo:
        cliente = compra.get("cliente", {})
        print(f"Cliente: {cliente.get('nombre', '')} (ID: {cliente.get('id', '')})")

        productos = compra.get("productos", [])
        print("Productos:")
        for producto in productos:
            print(f"Nombre: {producto.get('nombre', '')}, Cantidad: {producto.get('cantidad', '')}")

        total = compra.get("total", 0.0)
        print(f"Total: ${total:.2f}")

        # Agregar esta línea para mostrar el código de seguimiento
        codigo_seguimiento = compra.get("codigo_seguimiento", "")
        print(f"Código de Seguimiento: {codigo_seguimiento}")

        print("----")

# Cargar clientes y productos al iniciar el programa
cargar_clientes()
cargar_compras()

# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Registrar Cliente")
    print("2. Visualizar Clientes")
    print("3. Buscar Clientes")
    print("4. Realizar Compra")
    print("5. Visualizar Compras")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        visualizar_clientes()
    elif opcion == "3":
        buscar_clientes()
    elif opcion == "4":
        realizar_compra()
    elif opcion == "5":
        visualizar_compras()
    elif opcion == "6":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")