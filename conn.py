import os
from dotenv import load_dotenv
import pymysql

load_dotenv()

db = None 

try:
    db = pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    print("🚀 Conexão com MySQL estabelecida com sucesso!")
except Exception as err:
    print("❌ Falha na conexão:", err)