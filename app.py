import requests

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt'
    r = requests.get(url)

    lineas = r.text.strip().split('\n')
    encabezados = lineas[0].split('|')

    datos = [linea.split('|') for linea in lineas[1:]]
    datos_filtrados = [fila for fila in datos if fila[0][0] in ['3', '4', '5', '7']]

    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %M, %H, %S")
    
    
    fila_encabezados = ''
    for encabezado in encabezados:
        fila_encabezados += '<th>' + str(encabezado) + '</th>'
    
    
    filas_datos = ''
    for fila in datos_filtrados:
        filas_datos += '<tr>'
        for celda in fila:
            filas_datos += '<td>' + str(celda) + '</td>'
        filas_datos += '</tr>'
    
    
    return (
        '¡Hola, Loja! <b>' + str(fecha_formateada) + '</b>\n'
        '<table border="1">\n'
        '    <tr>' + fila_encabezados + '</tr>\n'
        '    ' + filas_datos + '\n'
        '</table>'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)