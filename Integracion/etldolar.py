#Instalamos
# pip install sqlalchemy
# pip install psycopg2
# pip install python-dotenv
# pip install pandas

from sqlalchemy import create_engine,text
import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv

#Cargar archivo .env
load_dotenv()

#Rescatamos los valores de conexión en variables
DB_DIALECT = os.getenv("DB_DIALECT")
DB_DRIVER = os.getenv("DB_DRIVER")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_NAME")
DB_PWD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_DATABASE")

#Generamos string de conexión
SQLALCHEMY_DATABASE_URL = f"{DB_DIALECT}+{DB_DRIVER}://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

#Definimos un objeto de tipo engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
print("Limpiando Tabla : tb_dolar")
with engine.connect() as conn:
    conn.execute(text("DELETE FROM esquema.tb_dolar"))
    conn.commit()
print("Tabla limpiada: tb_dolar")

#Primeramente cargar el dataset origen
origen_dataset = pd.read_csv("./Dolar2025.csv", delimiter=";", encoding='windows-1252')
origen_dataset = origen_dataset.astype(str)
df_datos = pd.DataFrame()
for indmes in range(1,13):
    for inddia in range(0,31):
        valor = origen_dataset.iloc[inddia,indmes] #[indmes]
        valor = valor.replace(".", "")
        valor = valor.replace(",", ".")
        if valor != 'nan':
            reg_dato = pd.DataFrame ( [{ "year"  : "2025"
                , "mount" : indmes
                , "day"   : inddia+1
                , "value" : valor
                }])
            df_datos = pd.concat( [df_datos, reg_dato], ignore_index=True)
df_datos.to_sql( 'tb_dolar', con=engine,if_exists='append', index=False,schema='esquema')

print( " Tabla Cargada.. tb_dolar")
engine.dispose()
