import tkinter as tk
from tkinter import ttk, messagebox

# Lógica del sistema experto
def recomendar_cultivo():
    suelo = suelo_var.get()
    lluvia = lluvia_var.get()
    estacion = estacion_var.get()
    try:
        temperatura = float(temp_var.get())
    except ValueError:
        messagebox.showerror("Error", "La temperatura debe ser un número.")
        return

    cultivo = "No se encontró una recomendación."
    explicacion = ""

    # Reglas del sistema experto
    if suelo == "Arcilloso" and lluvia == "Alta" and temperatura >= 25:
        cultivo = "Arroz"
        explicacion = "El arroz requiere suelos arcillosos y alta humedad con temperaturas cálidas."
    elif suelo == "Franco" and lluvia == "Media" and 18 <= temperatura <= 30:
        cultivo = "Maíz"
        explicacion = "El maíz se adapta bien a suelos francos con lluvias medias y temperaturas moderadas."
    elif suelo == "Limoso" and lluvia == "Media" and estacion == "Otoño":
        cultivo = "Trigo"
        explicacion = "El trigo se cultiva mejor en suelos limosos durante el otoño."
    elif suelo == "Arenoso" and lluvia == "Baja" and temperatura > 20:
        cultivo = "Maní"
        explicacion = "El maní prospera en suelos arenosos y climas secos con calor moderado."
    elif suelo == "Franco" and lluvia == "Alta" and estacion == "Verano":
        cultivo = "Papa"
        explicacion = "La papa prefiere suelos francos, humedad alta y estaciones cálidas como el verano."
    else:
        explicacion = "No se encontró una coincidencia exacta. Intente con otras combinaciones."

    # Mostrar resultado
    resultado = f"Cultivo recomendado: {cultivo}\n\nMotivo: {explicacion}"
    messagebox.showinfo("Resultado", resultado)

# Interfaz con Tkinter
ventana = tk.Tk()
ventana.title("Sistema Experto Agrícola")
ventana.geometry("400x400")

# Variables
suelo_var = tk.StringVar()
lluvia_var = tk.StringVar()
estacion_var = tk.StringVar()
temp_var = tk.StringVar()

# Widgets
tk.Label(ventana, text="Tipo de suelo:").pack(pady=5)
ttk.Combobox(ventana, textvariable=suelo_var, values=["Arenoso", "Arcilloso", "Franco", "Limoso"]).pack()

tk.Label(ventana, text="Nivel de lluvias:").pack(pady=5)
ttk.Combobox(ventana, textvariable=lluvia_var, values=["Baja", "Media", "Alta"]).pack()

tk.Label(ventana, text="Estación del año:").pack(pady=5)
ttk.Combobox(ventana, textvariable=estacion_var, values=["Primavera", "Verano", "Otoño", "Invierno"]).pack()

tk.Label(ventana, text="Temperatura promedio (°C):").pack(pady=5)
tk.Entry(ventana, textvariable=temp_var).pack()

tk.Button(ventana, text="Recomendar cultivo", command=recomendar_cultivo).pack(pady=20)

ventana.mainloop()
