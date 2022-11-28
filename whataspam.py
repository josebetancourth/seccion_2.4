import pandas as pd
archivo_excel = pd.read_excel('/ruta/ExcelEjemplo.xlsx')
print(archivo_excel.columns)
values = archivo_excel['Identificador'].values
print(values)