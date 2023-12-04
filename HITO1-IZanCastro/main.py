from final_hito1 import *

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