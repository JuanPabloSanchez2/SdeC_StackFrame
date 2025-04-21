from msl.loadlib import Server32
import ctypes

class Convertidor(Server32):
    def __init__(self, host='127.0.0.1', port=5000, **kwargs):
        super().__init__('intermedio.so', 'cdll', host=host, port=port, **kwargs)
        # Configura el tipo de retorno y argumentos
        self.lib.convertir_float.restype = ctypes.c_float
        self.lib.convertir_float.argtypes = [ctypes.c_float]

    def convertir_float_sv(self, valor):
        cvalor = ctypes.c_float(valor)
        return self.lib.convertir_float(cvalor)

# Inicia el servidor
if __name__ == "__main__":
    convertidor = Convertidor()
