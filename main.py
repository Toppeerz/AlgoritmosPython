import sys
from src.modelos.InterfazMenu import InterfazMenu

import numpy as np 
import os
import time


def main():
    interfaz = InterfazMenu()
    interfaz.mainloop()
    print('The window is closed.')

if __name__ == "__main__":
    main()
    