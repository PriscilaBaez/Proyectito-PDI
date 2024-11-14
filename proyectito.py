import pyautogui
import webbrowser
from time import sleep
import tkinter as tk
from tkinter import messagebox
import configparser

# Función para cargar la configuración desde el archivo INI
def cargar_configuracion():
    config = configparser.ConfigParser()
    config.read('config.ini')  # Lee el archivo config.ini

    # Obtener valores de configuración (si existen)
    numero = config.get('Configuracion', 'numero', fallback='')
    mensaje = config.get('Configuracion', 'mensaje', fallback='')
    cantidad = config.getint('Configuracion', 'cantidad', fallback=0)

    return numero, mensaje, cantidad

# Función para guardar la configuración en el archivo INI
def guardar_configuracion(numero, mensaje, cantidad):
    config = configparser.ConfigParser()

    # Establecer los valores en el archivo de configuración
    config['Configuracion'] = {
        'numero': numero,
        'mensaje': mensaje,
        'cantidad': str(cantidad)
    }

    # Guardar los cambios en el archivo config.ini
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

# Función para enviar mensajes
def enviar_mensajes():
    # Obtener los datos de la interfaz
    numero = entry_numero.get()
    mensaje = entry_mensaje.get()
    cantidad = int(entry_cantidad.get())

    # Abrir WhatsApp Web
    webbrowser.open(f'https://web.whatsapp.com/send?phone={numero}')
    
    # Esperar a que la página se cargue y el usuario esté logueado
    sleep(55)  # Ajusta el tiempo según sea necesario

    # Enviar mensajes
    for i in range(cantidad):
        pyautogui.typewrite(mensaje)
        pyautogui.press('enter')
        sleep(1)  # Pequeño retraso entre los mensajes

    # Guardar la configuración ingresada en el archivo INI
    guardar_configuracion(numero, mensaje, cantidad)

    messagebox.showinfo("Éxito", f"Se enviaron {cantidad} mensajes a {numero}.")

# Crear ventana principal
root = tk.Tk()
root.title("Enviar Mensajes por WhatsApp")
root.geometry("300x200")

# Leer los datos desde el archivo de configuración al iniciar la aplicación
numero, mensaje, cantidad = cargar_configuracion()

# Crear etiquetas y campos de entrada
tk.Label(root, text="Número de teléfono:").pack()
entry_numero = tk.Entry(root)
entry_numero.insert(0, numero)  # Establecer el valor por defecto
entry_numero.pack()

tk.Label(root, text="Mensaje a enviar:").pack()
entry_mensaje = tk.Entry(root)
entry_mensaje.insert(0, mensaje)  # Establecer el valor por defecto
entry_mensaje.pack()

tk.Label(root, text="Cantidad de mensajes:").pack()
entry_cantidad = tk.Entry(root)
entry_cantidad.insert(0, str(cantidad))  # Establecer el valor por defecto
entry_cantidad.pack()

# Botón para enviar mensajes
btn_enviar = tk.Button(root, text="Enviar Mensajes", command=enviar_mensajes)
btn_enviar.pack()

# Ejecutar la interfaz
root.mainloop()
