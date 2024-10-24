from model.jogadores import Jogador
from model.times import Time
from .controller_times import Controller_Times
from conexion.mysql_queries import MySQLQueries

class Controller_Jogadores:
    def __init__(self):
        self.ctrl_times = Controller_Times()

    def inserir_jogador(self):
        while True:
            # Conexão com o banco
            mysql_queries = MySQLQueries(can_write=True)
            mysql_queries.connect()

            # Listar times e selecionar o time do jogador
            self.listar_times(mysql_queries, need_connect=True)
            codigo_time = str(input("Digite o número (ID) do Time que o jogador joga: "))
            if codigo_time is None:
                print("Nenhum time com esse ID foi encontrado, verifique!")
                return None
            else:
                numero = int(input("Digite o número da Camisa para o Jogador: "))
                if self.verifica_existencia_camisa_jogador(mysql_queries, numero, codigo_time):
                    nome = input("Digite o Nome do jogador: ")
                    posicao = input("Digite a posição do jogador: ")

                    # Obtem os dados do time a partir do banco
                    df_time = mysql_queries.sqlToDataFrame(f"SELECT * FROM times WHERE id = {codigo_time}")
                    time_obj = Time(df_time.id.values[0], df_time.nome.values[0], df_time.cidade.values[0], df_time.estado.values[0])

                    # Criação do jogador com o objeto Time
                    mysql_queries.write(f"INSERT INTO jogadores (nome, posicao, numero, time_id) VALUES ('{nome}', '{posicao}', '{numero}', {codigo_time})")
                    df_jogadores = mysql_queries.sqlToDataFrame(f"SELECT * FROM jogadores WHERE numero = '{numero}' AND time_id = '{codigo_time}'")
                    novo_jogador = Jogador(df_jogadores.id.values[0], df_jogadores.nome.values[0], df_jogadores.posicao[0], df_jogadores.numero[0], time_obj)

                    print(novo_jogador.to_string())

                    # Pergunta se o usuário deseja inserir outro registro
                    resposta = input("Deseja inserir mais algum jogador? (Sim/Não): ")
                    if resposta.lower() == 'não':
                        break  # Voltar ao menu principal
                else:
                    print(f"O Número ({numero}) da camisa do jogador já está cadastrado! Defina outro.")
                    return None

    def excluir_jogadores(self):
        while True:
            # Conexão com o banco
            mysql = MySQLQueries(can_write=True)
            mysql.connect()

            # Solicita o ID do jogador
            id = int(input("Número (ID) do jogador que deseja excluir: "))  

            if not self.verifica_existencia_jogador(mysql, id):
                df_jogador = mysql.sqlToDataFrame(f"SELECT * FROM jogadores WHERE id = {id}")

                # Excluir o jogador
                mysql.write(f"DELETE FROM jogadores WHERE id = {id}")  
                jogador_excluido = Jogador(df_jogador.id.values[0], df_jogador.nome.values[0], df_jogador.posicao.values[0], df_jogador.numero.values[0])
                print("Jogador removido com sucesso!")
                print(jogador_excluido.to_string())

                # Pergunta se o usuário deseja excluir outro registro
                resposta = input("Deseja excluir mais algum jogador? (Sim/Não): ")
                if resposta.lower() == 'não':
                    break  # Voltar ao menu principal
            else:
                print(f"Não existe jogador com esse número: {id}.")

    def atualizar_jogador(self):
        while True:
            # Conexão com o banco
            mysql = MySQLQueries(can_write=True)
            mysql.connect()

            # Solicita ao usuário o código do jogador a ser alterado
            id = int(input("Digite a matrícula (id) do Jogador que deseja alterar: "))

            if not self.verifica_existencia_jogador(mysql, id):
                df_jogador_atual = mysql.sqlToDataFrame(f"SELECT * FROM jogadores WHERE id = {id}")

                if df_jogador_atual.empty:
                    print(f"Jogador com ID {id} não encontrado.")
                    return None

                print("Digite somente nos campos que deseja alterar, caso não queira alterar o campo pressione Enter")
                novo_nome = input(f"Digite o novo Nome (atual: {df_jogador_atual.nome.values[0]}): ") or df_jogador_atual.nome.values[0]
                nova_posicao = input(f"Digite a nova Posição (atual: {df_jogador_atual.posicao.values[0]}): ") or df_jogador_atual.posicao.values[0]
                novo_numero = input(f"Digite o novo Número (atual: {df_jogador_atual.numero.values[0]}): ") or df_jogador_atual.numero.values[0]
                novo_time = input(f"Digite o novo Time (atual: {df_jogador_atual.time_id.values[0]}): ") or df_jogador_atual.time_id.values[0]

                # Verifica se o time existe
                df_time = mysql.sqlToDataFrame(f"SELECT * FROM times WHERE id = {novo_time}")
                if df_time.empty:
                    print(f"Time com ID {novo_time} não encontrado.")
                    return None
                else:
                    time_obj = Time(df_time.id.values[0], df_time.nome.values[0], df_time.cidade.values[0], df_time.estado.values[0])

                # Atualiza o jogador
                mysql.write(f"""
                    UPDATE jogadores 
                    SET nome = '{novo_nome}', 
                        posicao = '{nova_posicao}', 
                        numero = '{novo_numero}', 
                        time_id = '{novo_time}' 
                    WHERE id = {id}
                """)

                # Cria um objeto Jogador atualizado
                df_jogadores = mysql.sqlToDataFrame(f"SELECT * FROM jogadores WHERE id = {id}")
                jogador_atualizado = Jogador(
                    df_jogadores.id.values[0], 
                    df_jogadores.nome.values[0], 
                    df_jogadores.posicao.values[0], 
                    df_jogadores.numero.values[0], 
                    time_obj
                )

                print(jogador_atualizado.to_string())

                # Pergunta se deseja atualizar outro registro
                resposta = input("Deseja atualizar mais algum jogador? (Sim/Não): ")
                if resposta.lower() == 'não':
                    break  # Voltar ao menu principal

    def verifica_existencia_camisa_jogador(self, mysql_queries:MySQLQueries, numero:str=None, codigo_time:int=None) -> bool:
        # Verifica se já existe um jogador com o mesmo número naquele time
        df_jogadores = mysql_queries.sqlToDataFrame(f"SELECT * FROM jogadores WHERE numero = '{numero}' AND time_id = '{codigo_time}' ")
        return df_jogadores.empty

    def verifica_existencia_jogador(self, mysql_queries:MySQLQueries, id:str=None) -> bool:
        # Verifica se o jogador com aquele ID já existe
        df_jogadores = mysql_queries.sqlToDataFrame(f"SELECT * FROM jogadores WHERE id = '{id}'")
        return df_jogadores.empty

    def listar_times(self, mysql: MySQLQueries, need_connect: bool=False):
        query = "SELECT * FROM times ORDER BY id"
        if need_connect:
            mysql.connect()
        print(mysql.sqlToDataFrame(query))

