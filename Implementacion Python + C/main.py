import requests
import ctypes

def get_valor_api():
    # URL de la API del Banco Mundial para el índice GINI de Argentina (2011-2020)
    url = "https://api.worldbank.org/v2/en/country/ARG/indicator/SI.POV.GINI?format=json&date=2011:2020"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # La estructura de la respuesta es [metadata, datos]
        if len(data) >= 2 and data[1]:
            for item in data[1]:
                if item['value'] is not None:
                    return float(item['value'])  # Devuelve el primer valor válido encontrado
        raise ValueError("No se encontraron datos válidos para el índice GINI de Argentina")
    
    except Exception as e:
        print(f"Error al obtener datos de la API: {e}")
        return 0.0  # Valor por defecto en caso de error

def main():
    valor = get_valor_api()
    print(f"Valor del índice GINI obtenido: {valor}")

    # Cargar la librería compartida
    lib = ctypes.CDLL("./intermedio.so")
    lib.convertir.argtypes = [ctypes.c_float]
    lib.convertir.restype = ctypes.c_int

    resultado = lib.convertir(ctypes.c_float(valor))
    print(f"Resultado procesado (entero + 1): {resultado}")

if __name__ == "__main__":
    main()