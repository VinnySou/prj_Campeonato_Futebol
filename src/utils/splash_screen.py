from conexion.mysql_queries import MySQLQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_estadios = config.QUERY_COUNT.format(tabela="estadios")
        self.qry_total_times = config.QUERY_COUNT.format(tabela="times")
        self.qry_total_jogadores = config.QUERY_COUNT.format(tabela="jogadores")
        self.qry_total_partidas = config.QUERY_COUNT.format(tabela="partidas")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "Arthur Coutinho, Enzo Sampaio, Felipe Koscky, Pedro Henrique, Vinícius De S. Silva"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2024/2"

    def get_total_estadios(self):
        # Cria uma nova conexão com o banco que permite alteração
        mysql = MySQLQueries()
        mysql.connect()
        # Retorna o total de registros computado pela query
        return mysql.sqlToDataFrame(self.qry_total_estadios)["total_estadios"].values[0]
    
    def get_total_times(self):
        mysql = MySQLQueries()
        mysql.connect()
        return mysql.sqlToDataFrame(self.qry_total_times)["total_times"].values[0]
    
    def get_total_jogadores(self):
        mysql = MySQLQueries()
        mysql.connect()
        return mysql.sqlToDataFrame(self.qry_total_jogadores)["total_jogadores"].values[0]
    
    def get_total_partidas(self):
        mysql = MySQLQueries()
        mysql.connect()
        return mysql.sqlToDataFrame(self.qry_total_partidas)["total_partidas"].values[0]
    
    
    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE CAMPEONATO DE FUTEBOL                    
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - ESTADIOS:      {str(self.get_total_estadios()).rjust(5)}
        #      2 - TIMES:      {str(self.get_total_times()).rjust(5)}
        #      3 - JOGADORES {str(self.get_total_jogadores()).rjust(5)}
        #      4 - PARTIDAS {str(self.get_total_partidas()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """