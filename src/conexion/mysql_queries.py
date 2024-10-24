import mysql.connector
from pandas import DataFrame
import json
import os

class MySQLQueries:

    def __init__(self, can_write: bool = False, database=None):
        self.can_write = can_write
        self.host = "localhost"
        self.port = 3306
        self.database = database or "campeonato_de_futebol"  # Permitir que o banco de dados seja opcional
        self.user = 'labdatabase'
        self.passwd = 'lab@Database2022'
        
        #base_dir = os.path.dirname(os.path.abspath(__file__))
        #file_path = os.path.join(base_dir, "passphrase/authentication.mysql")
        #with open(file_path, "r") as f:
         #   self.user, self.passwd = f.read().split(',')
            

    def __del__(self):
        if hasattr(self, 'cur') and self.cur:
            self.close()


    def connect(self):
        # '''
        # Método para realizar a conexão com o banco de dados MySQL.
        # Se o banco de dados não for especificado, conecta apenas ao servidor MySQL.
        # '''
        if self.database:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.passwd,
                database=self.database
            )
        else:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.passwd
            )
        
        self.cur = self.conn.cursor()
        return self.cur


    def sqlToDataFrame(self, query: str) -> DataFrame:
        '''
        Executa uma query e retorna o resultado como um DataFrame.
        Parameters:
        - query: SQL query
        Return: DataFrame com os resultados da consulta
        '''
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return DataFrame(rows, columns=[col[0].lower() for col in self.cur.description])

    def sqlToMatrix(self, query: str) -> tuple:
        '''
        Executa uma query e retorna os dados como uma matriz.
        Parameters:
        - query: SQL query
        Return: Matriz (lista de listas) e lista com os nomes das colunas
        '''
        self.cur.execute(query)
        rows = self.cur.fetchall()
        matrix = [list(row) for row in rows]
        columns = [col[0].lower() for col in self.cur.description]
        return matrix, columns

    def sqlToJson(self, query: str):
        '''
        Executa uma query e retorna os dados no formato JSON.
        Parameters:
        - query: SQL query
        Return: JSON com os resultados da consulta
        '''
        self.cur.execute(query)
        columns = [col[0].lower() for col in self.cur.description]
        rows = self.cur.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        return json.dumps(result, default=str)

    def write(self, query: str):
        '''
        Executa uma query de escrita no banco de dados.
        Parameters:
        - query: SQL query de inserção/atualização/exclusão
        '''
        if not self.can_write:
            raise Exception('Can\'t write using this connection')

        self.cur.execute(query)
        self.conn.commit()

    def close(self):
        '''
        Fecha a conexão com o banco de dados.
        '''
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def executeDDL(self, query: str):
        '''
        Executa uma query DDL (Data Definition Language).
        Parameters:
        - query: SQL query DDL
        '''
        self.cur.execute(query)
