from datetime import datetime
from model.partidas import Partida
from model.times import Time
from model.estadios import Estadio
from .controller_times import Controller_Times
from conexion.mysql_queries import MySQLQueries

class Controller_Partidas:
    def __init__(self):
        self.ctrl_times = Controller_Times()

    def inserir_partida(self) -> Partida:
        # Conexão com o banco
        mysql_queries = MySQLQueries(can_write=True)
        mysql_queries.connect()

        # Listar times para escolha do time da casa e visitante
        self.listar_times(mysql_queries, need_connect=False)
        id_time_casa = str(input("Digite o número (ID) do Time da casa: "))
        id_time_visitante = str(input("Digite o número (ID) do Time visitante: "))
        self.listar_estadios(mysql_queries, need_connect=True)
        estadio = input("Digite o estádio onde a partida será realizada: ")

        # Obtem os dados dos times a partir do banco
        df_time_casa = mysql_queries.sqlToDataFrame(f"SELECT * FROM times WHERE id = {id_time_casa}")
        df_time_visitante = mysql_queries.sqlToDataFrame(f"SELECT * FROM times WHERE id = {id_time_visitante}")
        df_estadio = mysql_queries.sqlToDataFrame(f"SELECT * FROM estadios WHERE id = {estadio}")
        
        if df_time_casa.empty or df_time_visitante.empty:
            print("Erro: Um ou ambos os times não foram encontrados.")
            return None

        time_casa_obj = Time(df_time_casa.id.values[0], df_time_casa.nome.values[0], df_time_casa.cidade.values[0], df_time_casa.estado.values[0])
        time_visitante_obj = Time(df_time_visitante.id.values[0], df_time_visitante.nome.values[0], df_time_visitante.cidade.values[0], df_time_visitante.estado.values[0])
        estadio_obj = Estadio(df_estadio.id.values[0], df_estadio.nome.values[0], df_estadio.cidade[0],df_estadio.estado[0])
        
        # Entrar com as informações da partida
        data = input("Digite a data da partida (YYYY-MM-DD): ")
        horario = input("Digite o horário da partida (HH:MM:SS): ")
        gols_time_casa = int(input(f"Digite os gols do time da casa ({time_casa_obj.nome}): "))
        gols_time_visitante = int(input(f"Digite os gols do time visitante ({time_visitante_obj.nome}): "))

        # Inserção da nova partida
        mysql_queries.write(f"""
            INSERT INTO partidas (data, horario, time_casa_id, time_visitante_id, estadio_id, gols_time_casa, gols_time_visitante) 
            VALUES ('{data}', '{horario}', {id_time_casa}, {id_time_visitante}, '{estadio}', {gols_time_casa}, {gols_time_visitante})
        """)

        # Recupera a partida recém inserida
        df_partida = mysql_queries.sqlToDataFrame(f"""
            SELECT * FROM partidas 
            WHERE data = '{data}' AND horario = '{horario}' AND time_casa_id = {id_time_casa} AND time_visitante_id = {id_time_visitante}
        """)
        
        nova_partida = Partida(
            df_partida.id.values[0], 
            df_partida.data.values[0], 
            df_partida.horario.values[0], 
            time_casa_obj, 
            time_visitante_obj, 
            estadio_obj, 
            df_partida.gols_time_casa.values[0], 
            df_partida.gols_time_visitante.values[0]
        )

        print(nova_partida.to_string())
        return nova_partida

    def atualizar_partida(self) -> Partida:
        # Conexão com o banco
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        # Solicita o ID da partida a ser alterada
        id_partida = int(input("Digite o ID da partida que deseja alterar: "))

        df_partida_atual = mysql.sqlToDataFrame(f"SELECT * FROM partidas WHERE id = {id_partida}")
        if df_partida_atual.empty:
            print(f"Partida com ID {id_partida} não encontrada.")
            return None

        # Entrar com as informações que deseja alterar
        print("Digite somente nos campos que deseja alterar, caso não queira alterar o campo pressione Enter")
        nova_data = input(f"Digite a nova data (atual: {df_partida_atual.data.values[0]}): ") or df_partida_atual.data.values[0]
        novo_horario = input(f"Digite o novo horário (atual: {df_partida_atual.horario.values[0]}): ") or df_partida_atual.horario.values[0]
        novo_estadio = input(f"Digite o novo estádio (atual: {df_partida_atual.estadio_id.values[0]}): ") or df_partida_atual.estadio_id.values[0]
        novos_gols_time_casa = input(f"Digite os novos gols do time da casa (atual: {df_partida_atual.gols_time_casa.values[0]}): ") or df_partida_atual.gols_time_casa.values[0]
        novos_gols_time_visitante = input(f"Digite os novos gols do time visitante (atual: {df_partida_atual.gols_time_visitante.values[0]}): ") or df_partida_atual.gols_time_visitante.values[0]

        # Verifica se o estádio existe no banco
        df_estadio = mysql.sqlToDataFrame(f"SELECT * FROM estadios WHERE id = {novo_estadio}")
        if df_estadio.empty:
            print(f"Estádio com o ID {novo_estadio} não encontrado.")
            return None
        else:
            estadio_obj = Estadio(df_estadio.id.values[0], df_estadio.nome.values[0], df_estadio.cidade[0],df_estadio.estado[0])

        # Atualizar a partida no banco
        mysql.write(f"""
            UPDATE partidas 
            SET data = '{nova_data}', 
                horario = '{novo_horario}', 
                estadio_id = '{novo_estadio}', 
                gols_time_casa = {novos_gols_time_casa}, 
                gols_time_visitante = {novos_gols_time_visitante}
            WHERE id = {id_partida}
        """)

        # Recupera e exibe a partida atualizada
        df_partida_atualizada = mysql.sqlToDataFrame(f"SELECT * FROM partidas WHERE id = {id_partida}")
        print(df_partida_atualizada)
        return df_partida_atualizada

    def excluir_partida(self):
        # Conexão com o banco
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        # Solicita o ID da partida que deseja excluir
        id_partida = int(input("Digite o ID da partida que deseja excluir: "))

        df_partida = mysql.sqlToDataFrame(f"SELECT * FROM partidas WHERE id = {id_partida}")
        if df_partida.empty:
            print(f"Partida com ID {id_partida} não encontrada.")
        else:
            mysql.write(f"DELETE FROM partidas WHERE id = {id_partida}")
            print(f"Partida ID {id_partida} excluída com sucesso.")

    def listar_partidas(self, mysql: MySQLQueries, need_connect: bool=False):
        query = "SELECT * FROM partidas ORDER BY data, horario"
        if need_connect:
            mysql.connect()
        print(mysql.sqlToDataFrame(query))

    def listar_estadios(self, mysql: MySQLQueries, need_connect: bool = False):
        query = "SELECT * FROM estadios ORDER BY id"
        if need_connect:
            mysql.connect()
        print(mysql.sqlToDataFrame(query))
    
    def listar_times(self, mysql: MySQLQueries, need_connect: bool = False):
        query = "SELECT * FROM times ORDER BY id"
        if need_connect:
            mysql.connect()
        print(mysql.sqlToDataFrame(query))
