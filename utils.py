import re

def filtrar_numeros(valor):
        numeros = re.findall(r'-?\d+\.?\d*', valor)
        if len(numeros) == 0:
            return 0.0
        if float(numeros[0]) > 0:
            return float(numeros[0])
        return 0