from conexion.mysql_queries import MySQLQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("src/sql/relatorio_estadios.sql") as f:
            self.query_relatorio_estadios = f.read()

        with open("src/sql/relatorio_times.sql") as f:
            self.query_relatorio_times = f.read()

        with open("src/sql/relatorio_jogadores.sql") as f:
            self.query_relatorio_jogadores = f.read()
            
        with open("src/sql/relatorio_partidas.sql") as f:
            self.query_relatorio_partidas = f.read()
            
        with open("src/sql/relatorio_classificacao.sql") as f:
            self.query_relatorio_classificacao = f.read()
           
        with open("src/sql/relatorio_jogadores_agrupados_time.sql") as f:
            self.query_relatorio_jogadores_por_time = f.read()

    def get_relatorio_estadios(self):
        # Cria uma nova conexão com o banco que permite alteração
        mysql = MySQLQueries()
        mysql.connect()
        # Recupera os dados transformando em um DataFrame
        print(mysql.sqlToDataFrame(self.query_relatorio_estadios))
        input("Pressione Enter para Sair do Relatório de Estádios")

    def get_relatorio_times(self):
        # Cria uma nova conexão com o banco que permite alteração
        mysql = MySQLQueries()
        mysql.connect()
        # Recupera os dados transformando em um DataFrame
        print(mysql.sqlToDataFrame(self.query_relatorio_times))
        input("Pressione Enter para Sair do Relatório de Times")
        
    def get_relatorio_jogadores(self):
        # Cria uma nova conexão com o banco que permite alteração
        mysql = MySQLQueries()
        mysql.connect()
        # Recupera os dados transformando em um DataFrame
        print(mysql.sqlToDataFrame(self.query_relatorio_jogadores))
        input("Pressione Enter para Sair do Relatório de Jogadores")
        
    def get_relatorio_partidas(self):
        # Cria uma nova conexão com o banco que permite alteração
        mysql = MySQLQueries()
        mysql.connect()
        # Recupera os dados transformando em um DataFrame
        print(mysql.sqlToDataFrame(self.query_relatorio_partidas))
        input("Pressione Enter para Sair do Relatório de Partidas")
        

    def  get_relatorio_classificacao(self):
        # Cria uma nova conexão com o banco que permite alteração
        mysql = MySQLQueries()
        mysql.connect()
        # Recupera os dados transformando em um DataFrame
        print(mysql.sqlToDataFrame(self.query_relatorio_classificacao))
        input("Pressione Enter para Sair do Relatório de Classificação")

    def get_relatorio_jogadores_por_time(self):
        # Cria uma nova conexão com o banco que permite alteração
        mysql = MySQLQueries()
        mysql.connect()
        # Recupera os dados transformando em um DataFrame
        print(mysql.sqlToDataFrame(self.query_relatorio_jogadores_por_time))
        input("Pressione Enter para Sair do Relatório de Jogadores por Time")