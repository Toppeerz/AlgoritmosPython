import matplotlib.pyplot as plt
import numpy as np
import os

class ChartGenerator:
    @staticmethod
    def generate_bar_chart(categories, values, chart_title, x_axis_title, y_axis_title, i):
        # Crea un nuevo gráfico de barras
        plt.figure(figsize=(20, 9))

        # Añade la serie de datos al gráfico
        bars = plt.bar(categories, values, width=0.7)

        # Configura el título del gráfico y los títulos de los ejes
        plt.title(chart_title)
        plt.xlabel(x_axis_title)
        plt.ylabel(y_axis_title)

        # Ajusta la rotación de las etiquetas del eje X
        plt.xticks(rotation=15)

        # Añade el valor exacto encima de cada barra
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, round(yval, 2), ha='center', va='bottom')


        # Guarda el gráfico como una imagen PNG
        filename = f"src/imagenes/Grafico{i}x{i}.png"
        plt.savefig(filename)

        plt.close()
        # Muestra el gráfico
        # plt.show()
