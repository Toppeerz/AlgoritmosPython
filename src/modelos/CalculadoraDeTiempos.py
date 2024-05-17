import time
import matplotlib.pyplot as plt
from .ChartGenerator import ChartGenerator
from .Algoritmos.III3SequentialBlock import multiply_III3SequentialBlock
from .DocumentoMatrices import load_matrix_from_file
from .TiempoEjecucion import PerformanceLogger
from .Algoritmos.III4ParallelBlock import multiply_III4ParallelBlock
from .Algoritmos.III5EnhancedParallelBlock import multiply_III5EnhancedParallelBlock
from .Algoritmos.IV3SequentialBlock import multiply_IV3SequentialBlock
from .Algoritmos.IV4ParallelBlock import multiply_IV4ParallelBlock
from .Algoritmos.IV5EnhancedParallelBlock import multiply_IV5EnhancedParallelBlock
from .Algoritmos.V3SequentialBlock import multiply_V3SequentialBlock
from .Algoritmos.V4ParallelBlock import multiply_V4ParallelBlock
from .Algoritmos.NaivLoopUnrollingFour import multiply_NaivLoopUnrollingFour
from .Algoritmos.NaivLoopUnrollingTwo import multiply_NaivLoopUnrollingTwo
from .Algoritmos.NaivOnArray import multiply_NaivOnArray
from .Algoritmos.StrassenNaiv import multiply_StrassenNaiv
from .Algoritmos.StrassenWinograd import multiply_StrassenWinograd
from .Algoritmos.WinogradOriginal import winograd_original_multiply
from .Algoritmos.WinogradScaled import multiply_WinogradScaled

class CalculadoraTiempos:
    categorias = []
    tiempos_ejecucion = []

    @staticmethod
    def calcular_tiempos(i):
        a = load_matrix_from_file(f"src/matrices/matriz{i}.txt")
        b = load_matrix_from_file(f"src/matrices/matriz{i}(2).txt")
        n = len(a)
        p = len(b)
        m = len(b[0])

        CalculadoraTiempos.calcular_naiv_on_array(a, b)
        CalculadoraTiempos.calcular_naiv_loop_unrolling_two(a, b)
        CalculadoraTiempos.calcular_naiv_loop_unrolling_four(a, b)
        CalculadoraTiempos.calcular_winograd_original(a, b, n, p, m)
        CalculadoraTiempos.calcular_winograd_scaled(a, b, n, p, m)
        CalculadoraTiempos.calcular_strassen_naiv(a, b)
        CalculadoraTiempos.calcular_strassen_winograd(a, b, n, p, m)
        CalculadoraTiempos.calcular_iii3_sequential_block(a, b, i, i//4)
        CalculadoraTiempos.calcular_iii4_parallel_block(a, b,i,i//4)
        CalculadoraTiempos.calcular_iii5_enhanced_parallel_block(a, b,i,i//4)
        CalculadoraTiempos.calcular_iv3_sequential_block(a, b, i, i//4)
        CalculadoraTiempos.calcular_iv4_parallel_block(a, b,i,i//4)
        CalculadoraTiempos.calcular_iv5_enhanced_parallel_block(a, b,i,i//4)
        CalculadoraTiempos.calcular_v3_sequential_block(a, b, i, i//4)
        CalculadoraTiempos.calcular_v4_parallel_block(a, b, i, i//4)

        ChartGenerator.generate_bar_chart(CalculadoraTiempos.categorias, CalculadoraTiempos.tiempos_ejecucion,
                                           f"Tiempos de ejecución de los algoritmos con matrices de tamaño {i}", "Algoritmo",
                                           "Tiempo de ejecución (ms)", i)

        CalculadoraTiempos.categorias.clear()
        CalculadoraTiempos.tiempos_ejecucion.clear()

    @staticmethod
    def calcular_naiv_on_array(a, b):
        start = time.time()
        multiply_NaivOnArray(a, b)
        end = time.time()
        execution_time = (end - start) * 1000  # Convertir a milisegundos
        CalculadoraTiempos.categorias.append("NaivOnArray")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución NaivOnArray: {execution_time} milisegundos")
        PerformanceLogger.log_performance("NaivOnArray", len(a), execution_time)

    @staticmethod
    def calcular_naiv_loop_unrolling_two(a, b):
        start = time.time()
        multiply_NaivLoopUnrollingTwo(a, b)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("NaivLoopUnrollingTwo")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución NaivLoopUnrollingTwo: {execution_time} milisegundos")
        PerformanceLogger.log_performance("NaivLoopUnrollingTwo", len(a), execution_time)

    @staticmethod
    def calcular_naiv_loop_unrolling_four(a, b):
        start = time.time()
        multiply_NaivLoopUnrollingFour(a, b)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("NaivLoopUnrollingFour")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución NaivLoopUnrollingFour: {execution_time} milisegundos")
        PerformanceLogger.log_performance("NaivLoopUnrollingFour", len(a), execution_time)

    @staticmethod
    def calcular_winograd_original(a, b, n, p, m):
        start = time.time()
        winograd_original_multiply(a, b, n, p, m)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("WinogradOriginal")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución WinogradOriginal: {execution_time} milisegundos")
        PerformanceLogger.log_performance("WinogradOriginal", len(a), execution_time)

    @staticmethod
    def calcular_winograd_scaled(a, b, n, p, m):
        start = time.time()
        multiply_WinogradScaled(a, b, n, p, m)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("WinogradScaled")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución WinogradScaled: {execution_time} milisegundos")
        PerformanceLogger.log_performance("WinogradScaled", len(a), execution_time)

    @staticmethod
    def calcular_strassen_naiv(a, b):
        start = time.time()
        multiply_StrassenNaiv(a, b)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("StrassenNaiv")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución StrassenNaiv: {execution_time} milisegundos")
        PerformanceLogger.log_performance("StrassenNaiv", len(a), execution_time)

    @staticmethod
    def calcular_strassen_winograd(a, b, n, p, m):
        start = time.time()
        multiply_StrassenWinograd(a, b, n, p, m)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("StrassenWinograd")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución StrassenWinograd: {execution_time} milisegundos")
        PerformanceLogger.log_performance("StrassenWinograd", len(a), execution_time)

    @staticmethod
    def calcular_iii3_sequential_block(a, b, i, j):
        start = time.time()
        multiply_III3SequentialBlock(a, b, i, j)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("III3.SequentialBlock")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución III3.SequentialBlock: {execution_time} milisegundos")
        PerformanceLogger.log_performance("III3.SequentialBlock", len(a), execution_time)

    @staticmethod
    def calcular_iii4_parallel_block(a, b, i, j):
        start = time.time()
        multiply_III4ParallelBlock(a, b, i, j)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("III4.ParallelBlock")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución III4.ParallelBlock: {execution_time} milisegundos")
        PerformanceLogger.log_performance("III4.ParallelBlock", len(a), execution_time)

    @staticmethod
    def calcular_iii5_enhanced_parallel_block(a, b, i, j):
        start = time.time()
        multiply_III5EnhancedParallelBlock(a, b, i, j)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("III5.EnhancedParallelBlock")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución III5.EnhancedParallelBlock: {execution_time} milisegundos")
        PerformanceLogger.log_performance("III5.EnhancedParallelBlock", len(a), execution_time)

    @staticmethod
    def calcular_iv3_sequential_block(a, b, i, j):
        start = time.time()
        multiply_IV3SequentialBlock(a, b, i, j)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("IV3.SequentialBlock")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución IV3.SequentialBlock: {execution_time} milisegundos")
        PerformanceLogger.log_performance("IV3.SequentialBlock", len(a), execution_time)

    @staticmethod
    def calcular_iv4_parallel_block(a, b, i, j):
        start = time.time()
        multiply_IV4ParallelBlock(a, b, i, j)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("IV4.ParallelBlock")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución IV4.ParallelBlock: {execution_time} milisegundos")
        PerformanceLogger.log_performance("IV4.ParallelBlock", len(a), execution_time)

    @staticmethod
    def calcular_iv5_enhanced_parallel_block(a, b, i, j):
        start = time.time()
        multiply_IV5EnhancedParallelBlock(a, b, i, j)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("IV5.EnhancedParallelBlock")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución IV5.EnhancedParallelBlock: {execution_time} milisegundos")
        PerformanceLogger.log_performance("IV5.EnhancedParallelBlock", len(a), execution_time)

    @staticmethod
    def calcular_v3_sequential_block(a, b, i, j):
        start = time.time()
        multiply_V3SequentialBlock(a, b, i, j)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("V3.SequentialBlock")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución V3.SequentialBlock: {execution_time} milisegundos")
        PerformanceLogger.log_performance("V3.SequentialBlock", len(a), execution_time)

    @staticmethod
    def calcular_v4_parallel_block(a, b, i, j):
        start = time.time()
        multiply_V4ParallelBlock(a, b, i, j)
        end = time.time()
        execution_time = (end - start) * 1000
        CalculadoraTiempos.categorias.append("V4.ParallelBlock")
        CalculadoraTiempos.tiempos_ejecucion.append(execution_time)
        print(f"Tiempo de ejecución V4.ParallelBlock: {execution_time} milisegundos")
        PerformanceLogger.log_performance("V4.ParallelBlock", len(a), execution_time)
