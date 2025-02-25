import tkinter as tk
from tkinter import messagebox
import re  

# Función para validar y enviar los datos
def enviar_datos():
    nombre = entrada_nombre.get().strip()
    correo = entrada_correo.get().strip()
    edad = entrada_edad.get().strip()
    escolaridad = escolaridad_var.get()

    # Validar nombre
    if not nombre:
        messagebox.showerror("Error", "El nombre no puede estar vacío.")
        return
    
    # Validar correo 
    patron_correo = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(patron_correo, correo):
        messagebox.showerror("Error", "El correo no es válido.")
        return

    # Validar edad
    if not edad.isdigit():
        messagebox.showerror("Error", "La edad debe ser un número.")
        return

    # Mensaje si es correcto
    messagebox.showinfo("Éxito", f"Datos enviados correctamente:\n\nNombre: {nombre}\nCorreo: {correo}\nEdad: {edad}\nEscolaridad: {escolaridad}")

# Función para limpiar el formulario
def limpiar_formulario():
    entrada_nombre.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    escolaridad_var.set("Selecciona tu escolaridad")

# Crear ventana
ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.geometry("400x350")
ventana.config(bg = "LightCyan")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Nombre:",bg="LightCyan", font="Arial").pack(pady=5)
entrada_nombre = tk.Entry(ventana, width=40)
entrada_nombre.pack()

tk.Label(ventana, text="Correo:",bg="LightCyan", font="Arial").pack(pady=5)
entrada_correo = tk.Entry(ventana, width=40)
entrada_correo.pack()

tk.Label(ventana, text="Edad:", bg="LightCyan", font="Arial").pack(pady=5)
entrada_edad = tk.Entry(ventana, width=40)
entrada_edad.pack()

tk.Label(ventana, text="Escolaridad máxima:", bg="LightCyan", font="Arial").pack(pady=5)
escolaridad_var = tk.StringVar(value="Selecciona tu escolaridad",)
opciones_escolaridad = ["Primaria", "Secundaria", "Preparatoria", "Universidad"]
menu_escolaridad = tk.OptionMenu(ventana, escolaridad_var, *opciones_escolaridad)
menu_escolaridad.pack(pady=5)

# Botones
boton_enviar = tk.Button(ventana, text="Enviar", font=("Arial", 12), command=enviar_datos)
boton_enviar.pack(pady=10)
boton_limpiar = tk.Button(ventana, text="Limpiar", font=("Arial", 12), command=limpiar_formulario)
boton_limpiar.pack(pady=5)

ventana.mainloop()

# Página de colores en HTML https://htmlcolorcodes.com/es/nombres-de-los-colores/ 
