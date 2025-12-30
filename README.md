# Data Analyst - Datalized
Postulación cargo Data Analyst

## Pregunta Analítica
Se desea conocer la tendencia, a través del análisis de la información entregada por el Servicio de Impuestos Internos (SII) sobre valores financieros de la moneda Dólar. Se desea un reporte que muestra la tendencia del año 2025 de esta moneda.

# Panel de Analítica
Para el desarrollo de esta pregunta he utilizado Power BI.
Como fuente de datos publica he utilizado el valor Dólar entregado por el SII (https://www.sii.cl/valores_y_fechas/dolar/dolar2025.htm#) para todo el año 2025. Se adjunta archivo Dolar2025.csv para el despliegue del Dashboard desarrollado.

En el Dashboard, desarrolle diversas funciones DAX autorreferenciales en su nombre como ejemplo de análisis de datos, de las cuales solo utilice algunas para dar a conocer el despliegue de información.

La información desplegada, muestra el valor Dólar del día actual (29-12-2025, fecha del desarrollo); Promedio Anual, Mínimo Anual y Máximo Anual del Dólar.

La matriz refleja la información de los meses del año, el mínimo, máximo y promedio anual de cada mes.

El primer grafico de columna muestra el Dólar promedio por mes, el segundo grafico de líneas muestra la tendencia del Dólar en el año 2025.


El archivo Power BI se llama Dashboard.pbix.
El archivo Dolar2025.csv, contiene la información del SII para el año 2025.
El archivo Dashboard.pdf, es un ejemplo del Dashboard desarrollado.

# Código Integración
## Prerrequisitos
Para la ejecución del proceso de integración es necesario cumplir con algunos prerrequisitos de instalación de algunos componentes:
- Instalar Visual Studio Buil Tools. (https://aka.ms/vs/stable/vs_BuildTools.exe)
- Instalar Python 3.13.9 (https://www.python.org/ftp/python/3.13.9/python-3.13.9-amd64.exe)
- Una vez instalado Python, utilizaremos pip para instalar unas librerías con el siguiente comando:
	- pip install -r requirements

- Instalar PostgreSQL 18 (https://get.enterprisedb.com/postgresql/postgresql-18.1-2-windows-x64.exe), que se utilizó para el desarrollo de la integración.


## Descripción del Desarrollo
Para el desarrollo de la integración se utilizó Python con una BD PostgreSQL. En Python se utilizó las siguientes librerías: 
- Pandas:  Librería esencial y de código abierto para el análisis y la manipulación de datos.
- SqlAlchemy: Librería de herramientas SQL de código abierto y un mapeador relacional de objetos (ORM).
- Psycopg2: Driver de base de datos PostgreSQL más utilizado.
- python-dotenv: Librería que simplifica la gestión de variables de configuración mediante la lectura de pares clave-valor de un archivo .env y su carga en el entorno de la aplicación.

A nivel de Bases de Datos PostgreSQL, se debe ejecutar el Script basedatos.sql, el cual creara la base de datos "DB_Dolar", un Schema llamado "esquema" y finalmente una tabla llamada "tb_dolar".

El archivo .env, contiene las variables para acceder  la Base de Datos, el cual debe ser actualizado según la configuración local que se posea.

El archivo etldolar.py, contiene el código necesario para la carga y limpieza del archivo Dolar2025.csv a la tabla “tb_dolar”. Este código procede a conectarse a la Base de Datos, eliminar los datos preexistentes para evitar duplicidad de información. Luego se procede a la lectura del archivo de datos a través de las librerías Pandas creando un DataFrame para la manipulación de los datos. Luego se crea un DataFrame que almacenara la estructura de la tabla “tb_dolar”. Posteriormente, se recorre todo el DataFrame de origen de datos para limpiar la data y transformar los valores del Dólar a un formato permitido por la Base de Datos. Finalmente utilizando librerías Pandas se procedió a la inserción de los datos en la tabla “tb_dolar”.
