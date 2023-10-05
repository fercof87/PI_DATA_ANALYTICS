import pandas as pd

ERROR_LOG        = "Logs/errores_json_gz.log"
GRAL_LOG         = "Logs/generalLog.log"

'''-------------------------------------------------------------------------------------
Autor:      Ing. Fernando G. Cofone
Fecha:      26 de Septiembre de 2023
Objetivo:   Realiza la apertura y lectura de un archivo en formato Excel (XLSX).
Entrada:    - Ruta Al archivo
            - Nombre del Archivo
            - Hoja del Archivo
            - Lineas a ignorar del Excel (Opcional)
Salida:     - Data Frame de Pandas con el contenido del Excel.
-------------------------------------------------------------------------------------'''
def leerExcel(raiz, nombre, hoja, ignorar_lineas=0):
    nombre = raiz + nombre
    errores = []

    try:
        # Usar el parámetro skiprows para omitir las primeras n líneas
        df = pd.read_excel(nombre, sheet_name=hoja, skiprows=ignorar_lineas)
        return df
    
    except FileNotFoundError as e:
        errores.append(f"Error: El archivo '{nombre}' no se encuentra. {str(e)}")
    except Exception as e:
        errores.append(f"Error inesperado: {str(e)}")

    if errores:
        with open(ERROR_LOG, "a", encoding="UTF-8") as log_file:
            for error in errores:
                log_file.write(error + "\n")

    return None

'''-------------------------------------------------------------------------------------
Autor:      Ing. Fernando G. Cofone
Fecha:      29 de Septiembre de 2023
Objetivo:   Realiza Exportacion a CSV de un DF de Pandas.
Entrada:    - Data Frame
            - Nombre Destino
Salida:     - True si la exportación fue exitosa, False en caso contrario.
-------------------------------------------------------------------------------------'''
def exportarDf(df, raiz, nombre_dest):
    errores = []
    extension = '.csv'
    nombre = raiz + nombre_dest + extension
    try:
        df.to_csv(nombre, index=False, sep='|')
        return True
    
    except Exception as e:
        errores.append(f"Error inesperado al exportar el DataFrame: {str(e)}")

    if errores:
        with open(ERROR_LOG, "a", encoding="UTF-8") as log_file:
            for error in errores:
               log_file.write(error + "\n")
        return False