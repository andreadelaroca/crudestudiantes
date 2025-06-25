import dao.operaciones as o

def menu():
    print("MENÚ DE INICIO")
    print("1. Agregar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")

def main():
    while True:
        menu()
        opcion = input("Digite una opción: ")
        if opcion == "1":
            usuario = input("Usuario: ")
            clave = input("Contraseña: ")
            o.agregar_usuario(usuario, clave)
            print("Usuario agregado exitosamente.\n")
        elif opcion == "2":
            if o.inicio():
                print("Bienvenido al sistema.")
            else:
                print("Error en el inicio de sesión.")
                print("Si su usuario no está registrado, selecciona la opción 1 para registrarse.")
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")     
    main()
