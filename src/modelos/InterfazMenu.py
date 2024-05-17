import tkinter as tk
from tkinter import messagebox
from .CalculadoraDeTiempos import CalculadoraTiempos

class InterfazMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú de Opciones")
        self.geometry("750x500")

        opciones_label = tk.Label(self, text="1. Calcular tiempos de ejecución de los algoritmos con matrices de tamaño 16x16\n\n"
                                              "2. Calcular tiempos de ejecución de los algoritmos con matrices de tamaño 32x32\n\n"
                                              "3. Calcular tiempos de ejecución de los algoritmos con matrices de tamaño 64x64\n\n"
                                              "4. Calcular tiempos de ejecución de los algoritmos con matrices de tamaño 128x128\n\n"
                                              "5. Calcular tiempos de ejecución de los algoritmos con matrices de tamaño 256x256\n\n"
                                              "6. Calcular tiempos de ejecución de los algoritmos con matrices de tamaño 512x512\n\n"
                                              "7. Calcular tiempos de ejecución de los algoritmos con matrices de tamaño 1024x1024\n\n"
                                              "8. Calcular tiempos de ejecución de los algoritmos con matrices de tamaño 2048x2048",
                                  justify=tk.LEFT)
        opciones_label.pack(pady=10)

        self.opcion_entrada = tk.Entry(self, width=15)
        self.opcion_entrada.pack(pady=5)

        boton_ok = tk.Button(self, text="OK", command=self.procesar_opcion)
        boton_ok.pack(pady=5)

    def procesar_opcion(self):
        opcion = self.opcion_entrada.get()
        if not opcion:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una opción")
            return

        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 8:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un número entre 1 y 8")
            return

        opcion = int(opcion)
        self.opcion_entrada.delete(0, tk.END)

        tamanio_matriz = [16, 32, 64, 128, 256, 512, 1024, 2048][opcion - 1]
        CalculadoraTiempos.calcular_tiempos(tamanio_matriz)

# Aquí debes importar y definir la clase CalculadoraTiempos

if __name__ == "__main__":
    app = InterfazMenu()
    app.mainloop()