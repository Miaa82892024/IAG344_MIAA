# ui.py
# Capa de interfaz gráfica (Tkinter)

import tkinter as tk
from tkinter import messagebox, filedialog
from controller import procesar_instruccion
from processor import process_excel_safe


def iniciar_app():
    # Ventana principal
    root = tk.Tk()
    root.title("Procesador Excel con IA")
    root.geometry("500x300")

    # Etiqueta
    tk.Label(
        root,
        text="Escriba una instrucción en lenguaje natural"
    ).pack(pady=10)

    # Campo de texto
    entrada = tk.Entry(root, width=60)
    entrada.pack(pady=5)

    def ejecutar():
        texto = entrada.get()
        exito, mensaje = procesar_instruccion(texto)

        if exito:
            messagebox.showinfo("Resultado", mensaje)
        else:
            messagebox.showerror("Error", mensaje)

    def seleccionar_excel():
        return filedialog.askopenfilename(
            title="Seleccionar archivo Excel",
            filetypes=[("Archivos Excel", "*.xlsx")]
        )

    def on_clic_procesar():
        archivo = seleccionar_excel()
        if not archivo:
            return

        exito, mensaje = process_excel_safe(archivo)
        if exito:
            messagebox.showinfo("Proceso completado", mensaje)
        else:
            messagebox.showerror("Error", mensaje)

    # Botón para instrucciones en lenguaje natural
    tk.Button(
        root,
        text="Ejecutar instrucción",
        command=ejecutar,
        width=25
    ).pack(pady=10)

    # Botón para seleccionar y procesar Excel
    tk.Button(
        root,
        text="Seleccionar y procesar archivo Excel",
        command=on_clic_procesar,
        width=30,
        height=2
    ).pack(pady=20)

    root.mainloop()

