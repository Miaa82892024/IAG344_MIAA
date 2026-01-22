# ui.py
# Capa de interfaz gráfica (Tkinter)

import tkinter as tk
from tkinter import messagebox, filedialog
from controller import procesar_instruccion
from processor import process_excel_safe

archivo_excel=None

def iniciar_app():
    global archivo_excel
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
    
    def seleccionar_excel():
        global archivo_excel
        archivo_excel=filedialog.askopenfile(
            title="Seleccionar archivo Excel",
            filetypes=[("Archivos Excel", "*.xlsx")])
        if archivo_excel:
            messagebox.showinfo(
                "Archivo seleccionado",
                f"Archivo cargado correctamente:\n{archivo_excel}"
            )

    def ejecutar():
        if not archivo_excel:
            messagebox.showerror(
                "Error",
                "Debe seleccionar un archivo Excel primero"
            )
            return
        
        texto = entrada.get().strip()
        if not texto:
            messagebox.showerror(
                "Error",
                "Debe escribir una instrucción"
            )
            return
        
        exito, mensaje = procesar_instruccion(texto)

        if exito:
            messagebox.showinfo("Resultado", mensaje)
        else:
            messagebox.showerror("Error", mensaje)

    #def seleccionar_excel():
     #   return filedialog.askopenfilename(
      #      title="Seleccionar archivo Excel",
       #     filetypes=[("Archivos Excel", "*.xlsx")]
        #)

    def on_clic_procesar():
        if not archivo_excel:
            messagebox.showerror(
                "Error"
                "Debe selecciona un archivo Excel primero"
            )
            return
        
        exito, mensaje = process_excel_safe(archivo_excel)
        if exito:
            messagebox.showinfo("Proceso completado", mensaje)
        else:
            messagebox.showerror("Error", mensaje)
            
    # Botón para seleccionar y procesar Excel
    tk.Button(
        root,
        text="Seleccionar archivo Excel",
        command=seleccionar_excel,
        width=30,
        #height=2
    ).pack(pady=20)
    
    #Botón instrucciones IA
    tk.Button(
        root,
        text="Ejecutar Instrucción",
        command=ejecutar,
        width=30
    ).pack(pady=8)

    # Botón para instrucciones en lenguaje natural
    tk.Button(
        root,
        text="Ejecutar instrucción",
        command=on_clic_procesar,
        width=30,
        height=2
    ).pack(pady=15)

    root.mainloop()

