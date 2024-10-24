from conexion.mysql_queries import MySQLQueries

def create_database():
    try:
        # Conectar sem especificar o banco de dados para poder criar o banco
        mysql = MySQLQueries(can_write=True, database=None)  
        mysql.connect()  # Estabelecer a conexão

        # Criação do banco de dados usando o cursor
        mysql.cur.execute("CREATE DATABASE IF NOT EXISTS campeonato_de_futebol")
        print("Banco de dados criado com sucesso!")

        # Agora seleciona explicitamente o banco de dados criado
        mysql.cur.execute("USE campeonato_de_futebol")

    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")
    
    finally:
        # Fechar a conexão ao final
        if 'mysql' in locals():
            mysql.close()

def create_tables():
    try:
        # Conectar ao banco de dados já criado
        mysql = MySQLQueries(can_write=True, database="campeonato_de_futebol")  
        mysql.connect()  # Estabelecer a conexão

        # Ler o arquivo SQL que contém a criação das tabelas
        with open("sql/create_tables_campeonato.sql", "r") as f:
            query = f.read()

        # Executar as queries
        list_of_commands = query.split(";")
        for command in list_of_commands:
            if command.strip():  # Verifica se o comando não é uma string vazia
                mysql.cur.execute(command)
                print(f"Executed: {command[:30]}...")  # Mostra os primeiros 30 caracteres do comando
        print("Tabelas criadas com sucesso!")
        
    except Exception as e:
        print(f"Erro ao criar as tabelas: {e}")
    
    finally:
        # Fechar a conexão ao final
        if 'mysql' in locals():
            mysql.close()
