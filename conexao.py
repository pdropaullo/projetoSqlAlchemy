# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine

# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = 'Senac2021'
host = '127.0.0.1'
port = 3306
database = 'flask_exemplo'

# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
if __name__ == '__main__':
    try:
        engine = get_connection()
        print(
            f"Conexão no host {host} para o usuario {user} criada com sucesso.")
    except Exception as ex:
        print("Erro de Conexão: \n", ex)
