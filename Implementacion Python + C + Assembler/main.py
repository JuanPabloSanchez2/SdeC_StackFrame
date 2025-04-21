from msl.loadlib import Client64
import requests

def get_valor_api():
    # URL de la API del Banco Mundial para el índice GINI de Argentina (2011-2020)
    url = "https://api.worldbank.org/v2/en/country/ARG/indicator/SI.POV.GINI?format=json&date=2011:2020"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # La estructura de la respuesta es [metadata, datos]
        if len(data) >= 2 and data[1]:
            # Tomamos el valor más reciente disponible (último año con datos)
            for item in data[1]:
                if item['value'] is not None:
                    return float(item['value'])
            
        raise ValueError("No se encontraron datos válidos para el índice GINI de Argentina")
    
    except Exception as e:
        print(f"Error al obtener datos de la API: {e}")
        return 0.0  # Valor por defecto en caso de error

def main():
    valor = get_valor_api()
    print(f"Valor del índice GINI obtenido: {valor}")

    # Conectarse al servidor 32-bit especificando el módulo Python que contiene la clase
    cliente = Client64(
        module32='mi_servidor' # sin .py
    )

    resultado = cliente.request32('convertir_float_sv', valor)

    print(f"Valor convertido (32-bit): {resultado}")
    print(f"Diferencia: {valor - resultado + 1}")  # Debería ser ~0


if __name__ == "__main__":
    main()