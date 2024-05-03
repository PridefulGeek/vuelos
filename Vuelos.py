import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



class Vuelo:
    def __init__(self, origen, destino, fecha, horas, horal, precio):
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.horas = horas
        self.horal = horal
        self.precio = precio
        self.asientos_disponibles = 50  # Número de asientos disponibles por vuelo

    def mostrar_info(self):
        return f"Origen: {self.origen}, Destino: {self.destino}, Fecha: {self.fecha}, Hora de salida: {self.horas}, Hora de llegada: {self.horal}, Precio: {self.precio}, Asientos disponibles: {self.asientos_disponibles}"

def buscar_vuelos(origen, destino, fecha):
    vuelos_disponibles = []
    for vuelo in vuelos:
        if vuelo.origen == origen and vuelo.destino == destino and vuelo.fecha == fecha:
            vuelos_disponibles.append(vuelo)
    return vuelos_disponibles

def reservar_vuelo():
    global vuelos_encontrados  # Declarar la variable global
    origen = origen_var.get()
    destino = destino_var.get()
    fecha = fecha_var.get()

    vuelos_encontrados = buscar_vuelos(origen, destino, fecha)
    vuelos_combobox['values'] = [v.mostrar_info() for v in vuelos_encontrados]

    seleccion_var.set("")  # Limpiar la selección anterior

    if not vuelos_encontrados:
        messagebox.showerror("Error", "No se encontraron vuelos que coincidan con tu búsqueda.")


def confirmar_reserva():
    seleccion = seleccion_var.get()
    if seleccion:
        vuelo_seleccionado = vuelos_encontrados[vuelos_combobox.current()]
        asientos_deseados = int(asientos_spinbox.get())  # Convertir a entero
        
        if asientos_deseados <= vuelo_seleccionado.asientos_disponibles:
            confirmacion = tk.messagebox.askyesno("Confirmar Reserva", vuelo_seleccionado.mostrar_info() + "\n\n¿Confirmar reserva?")
            if confirmacion:
                vuelo_seleccionado.asientos_disponibles -= asientos_deseados
                tk.messagebox.showinfo("Reserva Exitosa", f"¡Reserva exitosa! Has reservado {asientos_deseados} asientos para el vuelo seleccionado.")
                # Limpiar los campos
                origen_var.set("")
                destino_var.set("")
                fecha_var.set("")
                vuelos_combobox.set("")
                asientos_spinbox.set(1)
        else:
            tk.messagebox.showerror("Error", "Lo siento, no hay suficientes asientos disponibles para tu solicitud.")
    else:
        tk.messagebox.showerror("Error", "Por favor, selecciona un vuelo antes de confirmar la reserva.")


# Crear ventana principal
root = tk.Tk()
root.title("Reserva de Vuelos")

# Crear mensaje de aeropuertos
aeropuertos_label = ttk.Label(root, text="Aeropuertos en: Ciudad de México, Nueva York, Los Ángeles y Chicago")
aeropuertos_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
# Crear mensaje de fechas
aeropuertos_label = ttk.Label(root, text="Fechas ya programadas: 2024-05-02 y 2024-05-03")
aeropuertos_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Crear widgets
origen_label = ttk.Label(root, text="Origen:")
origen_var = tk.StringVar()
origen_entry = ttk.Entry(root, textvariable=origen_var)

destino_label = ttk.Label(root, text="Destino:")
destino_var = tk.StringVar()
destino_entry = ttk.Entry(root, textvariable=destino_var)

fecha_label = ttk.Label(root, text="Fecha (YYYY-MM-DD):")
fecha_var = tk.StringVar()
fecha_entry = ttk.Entry(root, textvariable=fecha_var)

buscar_button = ttk.Button(root, text="Buscar Vuelos", command=reservar_vuelo)

vuelos_combobox = ttk.Combobox(root, state="readonly", width=130)
seleccion_var = tk.StringVar()
vuelos_combobox.config(textvariable=seleccion_var)

asientos_label = ttk.Label(root, text="Número de Asientos:")
asientos_spinbox = ttk.Spinbox(root, from_=1, to=50, wrap=True, state="readonly")

confirmar_button = ttk.Button(root, text="Confirmar Reserva", command=confirmar_reserva)

# Posicionar widgets en la ventana
origen_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
origen_entry.grid(row=2, column=1, padx=5, pady=5)

destino_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
destino_entry.grid(row=3, column=1, padx=5, pady=5)

fecha_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
fecha_entry.grid(row=4, column=1, padx=5, pady=5)

buscar_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

vuelos_combobox.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

asientos_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
asientos_spinbox.grid(row=7, column=1, padx=5, pady=5)

confirmar_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# Lista de vuelos de ejemplo
vuelos = [
    Vuelo(origen="Ciudad de México", destino="Nueva York", fecha="2024-05-02", horas="08:00", horal="10:00", precio="$10,000"),
    Vuelo(origen="Nueva York", destino="Ciudad de México", fecha="2024-05-02", horas="12:00", horal="14:00", precio="$10,000"),
    Vuelo(origen="Los Ángeles", destino="Chicago", fecha="2024-05-03", horas="10:00", horal="11:00", precio="$5,000"),
    Vuelo(origen="Chicago", destino="Los Ángeles", fecha="2024-05-03", horas="14:00", horal="15:00", precio="$5,000"),
    Vuelo(origen="Ciudad de México", destino="Nueva York", fecha="2024-05-02", horas="09:00", horal="11:00", precio="$10,000"),
    Vuelo(origen="Nueva York", destino="Ciudad de México", fecha="2024-05-02", horas="13:00", horal="15:00", precio="$10,000"),
    Vuelo(origen="Los Ángeles", destino="Chicago", fecha="2024-05-03", horas="11:00", horal="12:00", precio="$5,000"),
    Vuelo(origen="Chicago", destino="Los Ángeles", fecha="2024-05-03", horas="15:00", horal="16:00", precio="$5,000")
]

# Mostrar ventana
root.mainloop()
