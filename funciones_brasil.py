import pandas as pd

def abrir_csv(ruta):
    df = pd.read_csv(ruta, encoding='ISO-8859-1', sep = ";")
    return df