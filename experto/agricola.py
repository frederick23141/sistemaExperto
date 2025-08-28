import tkinter as tk
from tkinter import ttk, messagebox
import clips
import datetime, os

HISTORIAL_ARCHIVO = "historial_consultas.txt"
REGLAS_ARCHIVO = "reglas.clp"

# Cargar entorno CLIPS
env = clips.Environment()
env.load(REGLAS_ARCHIVO)

def recomendar_cultivo():
    suelo = suelo_var.get().lower()
    lluvia = lluvia_var.get().lower()
    estacion = estacion_var.get().lower()
    try:
        temperatura = float(temp_var.get())
    except ValueError:
        messagebox.showerror("Error", "La temperatura debe ser un número.")
        return

    #Enviar datos a CLIPS como un hecho
    env.reset()
    hecho = f'(entorno (suelo {suelo}) (lluvia {lluvia}) (estacion {estacion}) (temperatura {temperatura}))'
    env.assert_string(hecho)
    env.run()

    cultivo, motivo = "No recomendado", "No se encontró una coincidencia con las condiciones ingresadas."

    #Buscar la recomendación generada por CLIPS
    for fact in env.facts():
        if fact.template.name == "recomendacion":
            cultivo = fact["cultivo"]
            motivo = fact["motivo"]
            break

    resultado = f"Cultivo recomendado: {cultivo.upper()}\n\nMotivo: {motivo}"
    messagebox.showinfo("Resultado", resultado)
    guardar_en_historial(suelo, lluvia, estacion, temperatura, cultivo, motivo)

#Guardar el historial en el archivo txt. para ir generando una base de datos de consutlas
def guardar_en_historial(suelo, lluvia, estacion, temperatura, cultivo, motivo):
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entrada = (
        f"\n--- Consulta: {fecha_hora} ---\n"
        f"Suelo: {suelo.capitalize()}, Lluvia: {lluvia.capitalize()}, Estación: {estacion.capitalize()}, Temperatura: {temperatura}°C\n"
        f"→ Cultivo recomendado: {cultivo.upper()}\n"
        f"→ Motivo: {motivo}\n\n"
    )
    with open(HISTORIAL_ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(entrada)

#Mostrar ventana con el historia de busquedas realizado
def mostrar_historial():
    if not os.path.exists(HISTORIAL_ARCHIVO):
        messagebox.showinfo("Historial", "No hay historial disponible.")
        return
    with open(HISTORIAL_ARCHIVO, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    ventana_historial = tk.Toplevel(ventana)
    ventana_historial.title("Historial de Consultas")
    ventana_historial.geometry("500x400")
    text_area = tk.Text(ventana_historial, wrap="word")
    text_area.insert("1.0", contenido)
    text_area.pack(expand=True, fill="both")
    text_area.config(state="disabled")

#Mostrar reglas
def mostrar_reglas():
    reglas = env.rules()
    texto = "Reglas cargadas:\n\n"
    for regla in reglas:
        texto += f"- {regla.name}\n\n"

    ventana_reglas = tk.Toplevel(ventana)
    ventana_reglas.title("Nombres de las reglas")
    ventana_reglas.geometry("300x400")

    text_area = tk.Text(ventana_reglas, wrap="word")
    text_area.insert("1.0", texto)
    text_area.pack(expand=True, fill="both")
    text_area.config(state="disabled") 


#mostrar hechos
def mostrar_hechos():
    hechos = env.facts()
    texto = "Hechos activos:\n\n"
    for hecho in hechos:
        # hecho es un objeto Fact, usamos str para mostrar su contenido
        texto += f"- {str(hecho)}\n\n"

    ventana_hechos = tk.Toplevel(ventana)
    ventana_hechos.title("Hechos Activos")
    ventana_hechos.geometry("400x400")

    text_area = tk.Text(ventana_hechos, wrap="word")
    text_area.insert("1.0", texto)
    text_area.pack(expand=True, fill="both")
    text_area.config(state="disabled")    

#limpiar los campos de la interfaz
def limpiar_campos():
    suelo_var.set("")
    lluvia_var.set("")
    estacion_var.set("")
    temp_var.set("")

# GUI
ventana = tk.Tk()
ventana.title("Sistema Experto Agrícola con CLIPS")
ventana.geometry("500x500")
ventana.configure(bg="#f1f8e9")

tk.Label(ventana, text="Sistema Experto Agrícola", font=("Helvetica", 16, "bold"), bg="#f1f8e9").pack(pady=10)

suelo_var = tk.StringVar()
lluvia_var = tk.StringVar()
estacion_var = tk.StringVar()
temp_var = tk.StringVar()

#Variable control para tipo de suelo
tk.Label(ventana, text="Tipo de suelo:", bg="#f1f8e9").pack()
ttk.Combobox(ventana, textvariable=suelo_var, values=["Arenoso", "Arcilloso", "Franco", "Limoso"], state="readonly").pack()

#Varianle control para niveles de lluvia
tk.Label(ventana, text="Nivel de lluvias:", bg="#f1f8e9").pack()
ttk.Combobox(ventana, textvariable=lluvia_var, values=["Baja", "Media", "Alta"], state="readonly").pack()

#Variable control para estacion del año
tk.Label(ventana, text="Estación del año:", bg="#f1f8e9").pack()
ttk.Combobox(ventana, textvariable=estacion_var, values=["Primavera", "Verano", "Otoño", "Invierno"], state="readonly").pack()

#variable control para temperatura promedio
tk.Label(ventana, text="Temperatura promedio (°C):", bg="#f1f8e9").pack()
tk.Entry(ventana, textvariable=temp_var).pack()

#botones de acciones
tk.Button(ventana, text="Recomendar cultivo", command=recomendar_cultivo, bg="#4caf50", fg="white").pack(pady=10)
tk.Button(ventana, text="Limpiar", command=limpiar_campos, bg="#f44336", fg="white").pack()
tk.Button(ventana, text="Ver historial", command=mostrar_historial, bg="#2196f3", fg="white").pack(pady=10)
tk.Button(ventana, text="Ver Reglas", command=mostrar_reglas, bg="#ff5100", fg="white").pack(pady=10)
tk.Button(ventana, text="Mostrar hechos", command=mostrar_hechos, bg="#397500", fg="white").pack(pady=10)

ventana.mainloop()
