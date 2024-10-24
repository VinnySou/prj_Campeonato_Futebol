from model.times import Time
from conexion.mysql_queries import MySQLQueries

class Controller_Times:
    def __init__(self):
        pass

    def inserir_times(self) -> Time:
        # Conexão com o banco
        mysql_queries = MySQLQueries(can_write=True)
        mysql_queries.connect()

        while True:
            nome = input("Digite um nome para o Time: ")
            if self.verifica_existencia_nome_time(mysql_queries, nome):
                cidade = input("Digite a Cidade do time: ")
                estado = input("Digite o Estado do time: ")
                mysql_queries.write(f"INSERT INTO times (nome, cidade, estado) VALUES ('{nome}', '{cidade}', '{estado}')")
                df_time = mysql_queries.sqlToDataFrame(f"SELECT * FROM times WHERE nome = '{nome}'")
                novo_time = Time(df_time.id.values[0], df_time.nome.values[0], df_time.cidade[0], df_time.estado[0])
                print(novo_time.to_string())

                resposta = input("Deseja inserir mais algum registro? (Sim/Não): ").strip().lower()
                if resposta == "não":
                    break
            else:
                print(f"O nome {nome} já está cadastrado! Defina outro.")

        return novo_time

        
        #verifica se o nome já existe
    def verifica_existencia_nome_time(self, mysql_queries:MySQLQueries, nome:str=None) -> bool:
         # Recupera os dados do novo time criado transformando em um DataFrame
        df_time = mysql_queries.sqlToDataFrame(f"SELECT * FROM times WHERE nome = '{nome}'")
        return df_time.empty
    
    def verifica_existencia_time(self, mysql_queries:MySQLQueries, id:str=None) -> bool:
        df_time = mysql_queries.sqlToDataFrame(f"SELECT * FROM times WHERE id = '{id}'")
        return df_time.empty
    

    def atualizar_time(self) -> Time:
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        while True:
            id = int(input("Número (ID) do time que deseja alterar: "))

            # Verifica se o time existe
            if not self.verifica_existencia_time(mysql, id):
                print(f"Time encontrado com ID: {id}.")
                
                # Mostra os detalhes atuais do time
                df_time = mysql.sqlToDataFrame(f"SELECT * FROM times WHERE id = {id}")
                time_atual = Time(df_time.id.values[0], df_time.nome.values[0], df_time.cidade.values[0], df_time.estado.values[0])
                print("Detalhes atuais do time:")
                print(time_atual.to_string())

                # Atualização do nome
                novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
                if novo_nome.strip() == "":
                    novo_nome = df_time.nome.values[0]

                # Atualização da cidade
                nova_cidade = input("Digite a nova cidade (ou pressione Enter para manter a atual): ")
                if nova_cidade.strip() == "":
                    nova_cidade = df_time.cidade.values[0]

                # Atualização do estado
                novo_estado = input("Digite o novo estado (ou pressione Enter para manter o atual): ")
                if novo_estado.strip() == "":
                    novo_estado = df_time.estado.values[0]

                # Realiza a atualização no banco de dados
                mysql.write(f"UPDATE times SET nome = '{novo_nome}', cidade = '{nova_cidade}', estado = '{novo_estado}' WHERE id = {id}")
                
                # Obtém os dados atualizados e cria o objeto atualizado
                df_time_atualizado = mysql.sqlToDataFrame(f"SELECT * FROM times WHERE id = {id}")
                time_atualizado = Time(df_time_atualizado.id.values[0], df_time_atualizado.nome.values[0], df_time_atualizado.cidade.values[0], df_time_atualizado.estado.values[0])
                
                print("Time atualizado com sucesso:")
                print(time_atualizado.to_string())

            else:
                print(f"Não existe time com esse número: {id}.")

            # Pergunta se deseja atualizar mais algum registro
            resposta = input("Deseja atualizar mais algum registro? (Sim/Não): ").strip().lower()
            if resposta == "não":
                break

        return time_atualizado

        

    def excluir_times(self):
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        while True:
            id = int(input("Número (ID) do time que deseja excluir: "))

            if not self.verifica_existencia_time(mysql, id):
                # Verifica se o time é uma chave estrangeira em outra tabela
                df_fk_check = mysql.sqlToDataFrame(f"SELECT * FROM partidas WHERE time_casa_id = {id} OR time_visitante_id = {id}")
                if not df_fk_check.empty:
                    resposta_fk = input(f"O time {id} está vinculado a partidas. Deseja excluir também os registros relacionados? (Sim/Não): ").strip().lower()
                    if resposta_fk == "não":
                        print("Ação cancelada.")
                        break
                    else:
                        mysql.write(f"DELETE FROM partidas WHERE time_casa_id = {id} OR time_visitante_id = {id}")

                df_time = mysql.sqlToDataFrame(f"SELECT * FROM times WHERE id = {id}")
                mysql.write(f"DELETE FROM times WHERE id = {id}")
                time_excluido = Time(df_time.id.values[0], df_time.nome.values[0], df_time.cidade.values[0], df_time.estado.values[0])
                print("Time Removido com Sucesso!")
                print(time_excluido.to_string())

            else:
                print(f"Não existe time com esse número: {id}.")

            resposta = input("Deseja excluir mais algum registro? (Sim/Não): ").strip().lower()
            if resposta == "não":
                break
