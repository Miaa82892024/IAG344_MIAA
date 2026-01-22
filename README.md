# Clase IA
## ❤️Comandos Consola
### ![imagen de python](PYTHON.png)
```
python --version (muestra la versión del python instalada en el equipo)

```
### ![imagen de git](git.png)
```
git --version (muestra la versión del git instalado en el equipo)
git init (solo una vez en una carpeta) 
git add . (agregar archivos)
git commit -m "primer commit" 
```

### ![imagen de git](gatito.jpg)

```
git branch -M main (rama principal)
git remote add origin https://github.com/Miaa82892024/IAG344_MIAA.git
  git push -u origin main
.gitignore. :para hacer excepciones, por ejemplo para no subir archivos a los entornos virtuales.  
```

### ![imagen de git](importante.jpg)

```
En cmd ->code . (para abrir el Visual Studio Code)

Para clonar carpeta, desde consola se ingresa: 
cd PROFES 
y se da la ruta: 
git clone https://github.com/fernandogh7508/IAG344.git

```
## 😘 Comandos git para subir archivos 
```
cd PERSONAL
git status
git remote -v
git push
git add .
git status
git commit -m "IAG344 v2"
git add .
git push
```

## 👌 html
```

alt + shift + a: para sacar el comentario
alt + shift + flecha: para duplicar
li*2 multiplica la etiqueta
<ol>: Lista ordenada
<ul>: Lista no ordenada
ctrl + shift + k: para eliminar una línea 
div.container y espacio o tab: autocompleta la etiqueta
alt+shift+f: organizar la tabla y organiza la identación
alt+ctrl+shift+flecha haacia abajo: selecciona varias líneas 

bootstrap: https://getbootstrap.com/

``` 
## 😍 Python

```
pip list: se encarga de realizar las instalaciones de las librerías 

python -m venv env3.13.5: crea entorno virtual para proyecto (verificar la versión de python)

env3.13.5\Scripts\activate: activar entorno virtual (sale error por primera vez)


Para corregir el error: en el buscador, ejecuta como administrador Powershell de Windows y digita set-ExecutionPolicy Unrestricted y dale S y enter

deactivate: Desactivar entorno virtual

#documenta en python
import re: expresiones regulares, librería estandar 
print: imprime en pantalla
python entrenamiento.py: ejecuta la instalación de la librería 

Markdown All in One: para organizar formato de tablas 

texto="Mi número es 1234"
resultado=re.search(r"\d+",texto)
print(resultado.group())

texto = "" (Aquí se crea una variable llamada texto que contiene una cadena vacía (no tiene nada)).
resultado = re.search(r"\d+", texto)

Esta línea usa expresiones regulares (re):

re.search() → busca un patrón dentro de un texto.

r"\d+" es el patrón:

\d → significa un dígito (0–9)

+ → uno o más dígitos seguidos

📌 En resumen:
👉 Está intentando buscar números dentro de texto.

Pero como texto está vacío (""), no hay ningún número, entonces: resultado = None

Con esta línea de código lo que hace es organizarme los números en una lista
resultado=re.findall(r"\d+",texto)
print(f"{texto} Resultado {resultado}")

Para declarar función se usa la palabra reservada 
def nombre():

Ejecutar una función

print(nombre de la función)

En ejemplo me separa número de los otros caracteres:

documento="CC 24.314.567"

def clean_id(docu):
    
    return re.sub(r"\D","",documento)

print(clean_id(documento))

Archivos test: Pruebas unitarias en el código

1. Documento para prueba de negocios
2. Documento de pruebas (test)

Para hacer las pruebas del test

Pip install pytest

Para actualizar 
python.exe -m pip install --upgrade

Para instalar la librería para pruebas
pip install pytest

Para mostrar las librerías instaladas
pip list

En la lógica de negocio (proccessor.py) y esta lo que la automatización debe hacer, luego la interfaz gráfica y por último el archivo ejecutable, aunque como es pequeña la alicación estas 2 últimas se pueden unir.

crear un .exe
1. Instalar librerias
   pip install pyinstaller

2. Crear el .exe
   pyinstaller --onefile --windowed app.py

```

## 😁 Comandos de consola (cmd)

```
|comando|Descripcion|
|-|-|: lo que esta encima es el título
|`cd`|cambio de directorio|
|`cd..`|cambio de directorio|
|`dir`|listar|
alt+shif+f: para organizar la tabla
cd: navega entre archivos
cd .. : se devuelve 
dir: visualiza archivos
```

## 😁 Comandos Panda
```
#LIBRERIAS
--
import pandas as pd #pip install pandas
--
df =pd.read_csv("./dataset.csv")
df.head(5)
--
df.describe()
--
df["favorites"]
--
df.loc[0:2]
--
df.loc[[0,1,7]]
--
df.loc[[1,7],["favorites"]]
--
df[df["favorites"]>400]
--
df[(df["favorites"]>400)&(df["mentions"]>20)]

```
