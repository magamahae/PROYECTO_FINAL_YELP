# Librerias
import json
import pandas as pd

#---------------Fc open chekin.json-----------------#
def yeld_json(archivo):
    comb_json = []  # Lista para almacenar los objetos JSON combinados

    with open(archivo) as file:
        for line in file:
            try:
                obj = json.loads(line)
                comb_json.append(obj)
            except json.JSONDecodeError as e:
                print(f"Error al leer JSON en: {archivo}: {str(e)}")

    df_chekin = pd.DataFrame(comb_json)  # Crear DataFrame
    return df_chekin

#----------------------verificar_tipo_datos-------------------------------------#
def verificar_tipo_datos(df):
    diccionario = {"Columna": [], "Tipo": [], "NO_nulos_%": [], "Nulos_%": [], "Nulos": []}

    for columna in df.columns:
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        diccionario["Columna"].append(columna)
        diccionario["Tipo"].append(df[columna].apply(type).unique())
        diccionario["NO_nulos_%"].append(round(porcentaje_no_nulos, 2))
        diccionario["Nulos_%"].append(round(100-porcentaje_no_nulos, 2))
        diccionario["Nulos"].append(df[columna].isnull().sum())

    df_info = pd.DataFrame(diccionario)
        
    return df_info