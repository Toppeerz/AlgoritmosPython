import os

class PerformanceLogger:
    FILE_NAME = "Tiempos_ejecucion.txt"

    @staticmethod
    def log_performance(algorithm_name, input_size, execution_time):
        with open(PerformanceLogger.FILE_NAME, 'a') as f:
            f.write(f"{algorithm_name}, {input_size}, {execution_time}\n")