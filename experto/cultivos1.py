#

import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import os


HISTORIAL_ARCHIVO = "historial_consultas.txt"

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

    # Reglas del sistema experto actualizadas
    if suelo == "Arcilloso" and lluvia == "Alta" and temperatura >= 25:
        cultivo = "Arroz"
        explicacion = "El arroz requiere suelos arcillosos, alta humedad y temperaturas cálidas."
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
    elif suelo == "Arcilloso" and lluvia == "Alta" and temperatura > 28:
        cultivo = "Caña de azúcar"
        explicacion = "La caña necesita mucha humedad, calor y suelos arcillosos profundos."
    elif suelo == "Arenoso" and lluvia == "Baja" and temperatura > 30:
        cultivo = "Sorgo"
        explicacion = "El sorgo es resistente a la sequía y se adapta a suelos arenosos y calurosos."
    elif suelo == "Franco" and lluvia == "Media" and estacion == "Primavera":
        cultivo = "Soja"
        explicacion = "La soja crece mejor en suelos francos con lluvias moderadas en primavera."
    else:
        explicacion = "No se encontró una coincidencia exacta. Intente con otras combinaciones."

    resultado = f"Cultivo recomendado: {cultivo}\n\nMotivo: {explicacion}"
    messagebox.showinfo("Resultado", resultado)

      # Guardar en historial
    guardar_en_historial(suelo, lluvia, estacion, temperatura, cultivo, explicacion)

# ------------------------
def guardar_en_historial(suelo, lluvia, estacion, temperatura, cultivo, explicacion):
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entrada = (
        f"\n--- Consulta realizada el {fecha_hora} ---\n"
        f"Suelo: {suelo}\n"
        f"Lluvia: {lluvia}\n"
        f"Estación: {estacion}\n"
        f"Temperatura: {temperatura}°C\n"
        f"→ Cultivo recomendado: {cultivo}\n"
        f"→ Motivo: {explicacion}\n"
    )

    with open(HISTORIAL_ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(entrada)

# ------------------------
def mostrar_historial():
    if not os.path.exists(HISTORIAL_ARCHIVO):
        messagebox.showinfo("Historial", "No hay historial disponible todavía.")
        return

    with open(HISTORIAL_ARCHIVO, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    ventana_historial = tk.Toplevel(ventana)
    ventana_historial.title("Historial de Consultas")
    ventana_historial.geometry("500x400")

    text_area = tk.Text(ventana_historial, wrap=tk.WORD)
    text_area.pack(expand=True, fill="both")
    text_area.insert("1.0", contenido)
    text_area.config(state="disabled")

def limpiar_campos():
    suelo_var.set("")
    lluvia_var.set("")
    estacion_var.set("")
    temp_var.set("")

# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.title("Sistema Experto Agrícola")
ventana.geometry("500x450")
ventana.resizable(False, False)
ventana.configure(bg="#e8f5e9")

# Título
tk.Label(ventana, text="Sistema Experto Agrícola", font=("Helvetica", 16, "bold"), bg="#e8f5e9").pack(pady=10)

# Variables
suelo_var = tk.StringVar()
lluvia_var = tk.StringVar()
estacion_var = tk.StringVar()
temp_var = tk.StringVar()

# Tipo de suelo
tk.Label(ventana, text="Tipo de suelo:", bg="#e8f5e9").pack(pady=5)
ttk.Combobox(ventana, textvariable=suelo_var, values=["Arenoso", "Arcilloso", "Franco", "Limoso"], state="readonly").pack()

# Nivel de lluvia
tk.Label(ventana, text="Nivel de lluvias:", bg="#e8f5e9").pack(pady=5)
ttk.Combobox(ventana, textvariable=lluvia_var, values=["Baja", "Media", "Alta"], state="readonly").pack()

# Estación del año
tk.Label(ventana, text="Estación del año:", bg="#e8f5e9").pack(pady=5)
ttk.Combobox(ventana, textvariable=estacion_var, values=["Primavera", "Verano", "Otoño", "Invierno"], state="readonly").pack()

# Temperatura
tk.Label(ventana, text="Temperatura promedio (°C):", bg="#e8f5e9").pack(pady=5)
tk.Entry(ventana, textvariable=temp_var).pack()

# Botones
tk.Button(ventana, text="Recomendar cultivo", command=recomendar_cultivo, bg="#4caf50", fg="white").pack(pady=15)
tk.Button(ventana, text="Limpiar campos", command=limpiar_campos, bg="#f44336", fg="white").pack()
tk.Button(ventana, text="Ver historial de consultas", command=mostrar_historial, bg="#2196f3", fg="white").pack(pady=10)

ventana.mainloop()
