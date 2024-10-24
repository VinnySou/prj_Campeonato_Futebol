from conexion.mysql_queries import MySQLQueries

def create_tables(query:str):
    list_of_commands = query.split(";")

    mysql = MySQLQueries(can_write=True)
    mysql.connect()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            try:
                mysql.executeDDL(command)
                print("Successfully executed")
            except Exception as e:
                print(e)            

def generate_records(query:str, sep:str=';'):
    list_of_commands = query.split(sep)

    mysql = MySQLQueries(can_write=True)
    mysql.connect()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            mysql.write(command)
            print("Successfully executed")

def run():
    mysql = MySQLQueries(can_write=True)
    mysql.connect()
    
    
    mysql.executeDDL("CREATE DATABASE IF NOT EXISTS campeonato_de_futebol")
    mysql.executeDDL("USE campeonato_de_futebol")

    with open("sql\create_tables_campeonato.sql") as f:
        query_create = f.read()
        
    print("Creating tables...")
    create_tables(query=query_create)
    print("Tables successfully created!")

if __name__ == '__main__':
    run()