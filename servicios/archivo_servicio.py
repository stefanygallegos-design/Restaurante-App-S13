import json


class ArchivoServicio:

    def leer_json(self, ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)

        except FileNotFoundError:
            print(f"No se encontró el archivo: {ruta}")
            return []

        except json.JSONDecodeError:
            print(f"El archivo no contiene un JSON válido: {ruta}")
            return []
