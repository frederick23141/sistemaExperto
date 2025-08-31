# 🌱 Sistema Experto Agrícola con CLIPS

Este proyecto implementa un **sistema experto agrícola** que recomienda cultivos adecuados en función de las condiciones de **suelo**, **lluvia**, **estación del año** y **temperatura**.  

El motor de inferencia se desarrolla con **CLIPS** (a través de la librería `clips` en Python) y la interfaz gráfica con **Tkinter**.

---

## 🚀 Características
- Interfaz gráfica sencilla y amigable para ingresar datos de entorno.  
- Motor de inferencia basado en **reglas CLIPS**.  
- Recomendación de cultivos junto con el **motivo de la decisión**.  
- Historial de consultas guardado en un archivo de texto (`historial_consultas.txt`).  
- Visualización de:
  - ✅ Reglas cargadas.  
  - ✅ Hechos activos en el motor CLIPS.  
  - ✅ Historial de consultas anteriores.  

---

## 📦 Requisitos

- Python **3.10+** (se recomienda evitar 3.12 en caso de incompatibilidades con `clips`).  
- Librerías necesarias:

```bash
pip install clips

python agricola.py


#📊 Funcionamiento

El usuario selecciona:

Tipo de suelo (Arenoso, Arcilloso, Franco, Limoso).

Nivel de lluvias (Baja, Media, Alta).

Estación del año (Primavera, Verano, Otoño, Invierno).

Temperatura promedio (número en °C).

El sistema envía un hecho a CLIPS, activa las reglas y genera una recomendación.

La salida incluye:

Cultivo recomendado.

Motivo de la recomendación.

Toda consulta se almacena automáticamente en historial_consultas.txt con fecha y hora.

📂 Archivos del Proyecto

agricola.py → Código principal de la interfaz y lógica.

reglas.clp → Archivo con las reglas de producción en CLIPS.

historial_consultas.txt → Archivo que almacena el historial de consultas.
