import pwinput
import os

def agregar_usuario(usuario, clave):
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario}, {clave}\n")
        
def cargar_usuarios():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                usuario, clave = linea.strip().split(", ")
                usuarios[usuario] = clave
    return usuarios

def inicio():
    print("INICIO DE SESIÓN")
    usuarios = cargar_usuarios()
    usuario = input("Usuario: ")
    clave_ingresada = pwinput.pwinput(prompt= "Contraseña: ", mask="*")
    if usuario in usuarios and usuarios[usuario] == clave_ingresada:
        print("Acceso permitido\n")
        return True
    else:
        print("Contraseña incorrecta. Acceso denegado.\n")
        return False
    