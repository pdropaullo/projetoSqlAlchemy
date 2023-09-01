from sqlalchemy import text
import conexao as con

engine = con.get_connection()
#print(engine)

# Criando tabelas pelos SQlALchemy
# 1
with engine.connect() as connection:
    connection.execute(text("CREATE TABLE IF NOT EXISTS users (id INTEGER primary key auto_increment, name VARCHAR(20))"))

# adicionando dados a tabela::
# 2
with engine.connect() as connection:
    pass
    connection.execute(text("INSERT INTO users (name) VALUES (:name)"), {"name": "Usuario Novo A"})
    connection.execute(text("INSERT INTO users (name) VALUES (:name)"), [{"name": "Usuario Novo B"}, {"name": "Usuario Novo C"}])
    connection.commit()

with engine.connect() as connection:
# consultando dados
# 3
    result = connection.execute(text("SELECT * FROM users WHERE name = :name"), dict(name="Usuario Novo A"))
    for row in result.mappings():
        print("Autor:" ,row["id"], row["name"])

# Listar as colunas de uma tabelas
with engine.connect() as connection:
    query = "SELECT * FROM student LIMIT 0,10"
    my_data = connection.execute(text(query))
    print(my_data.keys())

# Utilizando fetchmany()
with engine.connect() as connection:
    query = "SELECT * FROM student LIMIT 0,5"
    my_data = connection.execute(text(query))  # SQLAlchemy my_conn result
    # my_data=my_data.fetchmany(size=2) # collect 2 rows of data
    for row in my_data:
        print(row)



# Utilizando FetchONE
with engine.connect() as connection:
    query = "SELECT * FROM student LIMIT 0,5"
    my_data = connection.execute(text(query))
    my_row = my_data.fetchone()
    # my_data=my_data.fetchmany(size=2)
    print(my_row[0], my_row[1])  # 1 John Deo
    # my_data.next()
    my_row = my_data.fetchone()
    print(my_row[0], my_row[1])  # 2 Max Ruin


# Utilizando FETCHALL
with engine.connect() as connection:
    from sqlalchemy.exc import SQLAlchemyError
    q="SELECT * FROM student LIMIT 0,10"
    try:
        my_cursor=connection.execute(text(q))
        my_data=my_cursor.fetchall()
        for row in my_data:
            print(row)
    except SQLAlchemyError as e:
        error=str(e.__dict__['orig'])
        print(error)
    except Exception as e:
        print(e)
    else:
        print("Total Number of rows : ",my_cursor.rowcount)


# Utilizando First:
with engine.connect() as connection:
    from sqlalchemy.exc import SQLAlchemyError
    q = "SELECT * FROM student LIMIT 0,10"
    try:
        my_cursor = connection.execute(text(q))
        my_data = my_cursor.first()
        print(type(my_data))
        print(my_data['name'])
        for row in my_data:
            print(row)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    except Exception as e:
        print(e)
    else:
        print("Total Number of rows : ", my_cursor.rowcount)


# Utilizando o Where:

with engine.connect() as connection:
    rs = connection.execute(text("SELECT * FROM  student WHERE class='Three'"))
    my_data = rs.fetchall()  # a list
    print(my_data)

# Utilizando parametros nas querys:
with engine.connection() as connection:
    sql="SELECT * FROM student WHERE class=%s and id > %s"
    rs=connection.execute(text(sql), 'Four',20)
    print("Rows collected  = ",rs.rowcount)
    print(rs.fetchall())

