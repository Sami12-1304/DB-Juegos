from tkinter import *
import json


registros = []


def cargar_registros():
    try:
        with open("registros.json", "r") as file:
            global registros
            registros = json.load(file)
        print("Registros cargados:", registros)
        mostrar_registros()
    except FileNotFoundError:
        print("No se encontró el archivo, se comenzará con una lista vacía.")
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON.")


def guardar_registros():
    try:
        with open("registros.json", "w") as file:
            json.dump(registros, file, indent=4)
        print("Datos guardados en el archivo JSON.")
    except Exception as e:
        print(f"Error al guardar en el archivo JSON: {e}")


def send_data():
    nombredeljuego_data = nombredeljuego.get().strip()
    materias_data = materias.get().strip()
    descripciones_data = descripciones.get().strip()

    if not nombredeljuego_data or not materias_data or not descripciones_data:
        print("Por favor, complete todos los campos.")
        return

    
    registros.append([nombredeljuego_data, materias_data, descripciones_data])
    print("Registro agregado:", registros[-1])

    
    guardar_registros()

    
    nombredeljuego_entry.delete(0, END)
    materias_entry.delete(0, END)
    descripciones_entry.delete(0, END)

    
    mostrar_registros()


def ordenar_registros():
    registros.sort(key=lambda x: x[0])  
    print("Registros ordenados:", registros)
    guardar_registros()

   
    mostrar_registros()


def buscar_registro(nombre):
    for registro in registros:
        if registro[0].lower() == nombre.lower():
            print("Registro encontrado:", registro)
            return registro
    print("Registro no encontrado.")
    return None


def eliminar_registro():
    nombre_a_eliminar = eliminar_entry.get().strip()

    if not nombre_a_eliminar:
        print("Por favor ingrese el nombre del juego para eliminar.")
        return

    global registros
    registros = [registro for registro in registros if registro[0].lower() != nombre_a_eliminar.lower()]

    
    guardar_registros()

    print(f"Registro de {nombre_a_eliminar} eliminado.")
    eliminar_entry.delete(0, END)

    
    mostrar_registros()


def mostrar_registros():
   
    for widget in lista_frame.winfo_children():
        widget.destroy()

    
    for registro in registros:
        Label(lista_frame, text=f"{registro[0]} - {registro[1]} - {registro[2]}", bg="#f0f0f0", anchor="w", width=60).pack(fill="x")


mywindow = Tk()
mywindow.geometry("650x650")
mywindow.title("REGISTRO DE VIDEOJUEGOS")
mywindow.resizable(False, False)
mywindow.config(background="#213141")

main_title = Label(text="Registro de videojuegos", font=("cambria", 13), bg="#56CD63", fg="white", width="550", height="2")
main_title.pack()


nombrejuego_label = Label(text="nombre del juego", bg="#FFEEDD")
nombrejuego_label.place(x=22, y=70)
materia_label = Label(text="materia", bg="#FFEEDD")
materia_label.place(x=22, y=130)
descripcion_label = Label(text="descripcion", bg="#FFEEDD")
descripcion_label.place(x=22, y=190)

nombredeljuego = StringVar()
materias = StringVar()
descripciones = StringVar()

nombredeljuego_entry = Entry(textvariable=nombredeljuego, width="40")
materias_entry = Entry(textvariable=materias, width="40")
descripciones_entry = Entry(textvariable=descripciones, width="40")

nombredeljuego_entry.place(x=22, y=100)
materias_entry.place(x=22, y=160)
descripciones_entry.place(x=22, y=220)


submite_btn = Button(mywindow, text="registro", command=send_data, width="30", height="2", bg="#00CD63")
submite_btn.place(x=22, y=320)

ordenar_btn = Button(mywindow, text="Ordenar Registros", command=ordenar_registros, width="30", height="2", bg="#007BFF")
ordenar_btn.place(x=22, y=370)


buscar_label = Label(text="Buscar por nombre del juego:", bg="#FFEEDD")
buscar_label.place(x=22, y=430)
buscar_entry = Entry(width="40")
buscar_entry.place(x=22, y=460)

buscar_btn = Button(mywindow, text="Buscar", command=lambda: buscar_registro(buscar_entry.get()), width="30", height="2", bg="#FFD700")
buscar_btn.place(x=22, y=500)


eliminar_label = Label(text="Eliminar por nombre del juego:", bg="#FFEEDD")
eliminar_label.place(x=22, y=540)
eliminar_entry = Entry(width="40")
eliminar_entry.place(x=22, y=570)

eliminar_btn = Button(mywindow, text="Eliminar", command=eliminar_registro, width="30", height="2", bg="#FF6347")
eliminar_btn.place(x=22, y=610)


lista_frame = Frame(mywindow, bg="#f0f0f0", width=600)
lista_frame.place(x=22, y=650)


cargar_registros()

mywindow.mainloop()

