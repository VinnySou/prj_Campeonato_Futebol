from model.estadios import Estadio
from conexion.mysql_queries import MySQLQueries

class Controller_Estadios:
    def __init__(self):
        pass

    def inserir_estadios(self) -> Estadio:

        # Conexão com o banco.
        mysql_queries = MySQLQueries(can_write=True)
        mysql_queries.connect()

        while True:
            nome = input("Digite um nome para o estádio: ")
            if self.verifica_existencia_nome_estadio(mysql_queries, nome):
                cidade = input("Digite a cidade do Estádio: ")
                estado = input("Digite o estado do Estádio: ")
                mysql_queries.write(f"INSERT INTO estadios (nome, cidade, estado) VALUES ('{nome}', '{cidade}', '{estado}')")
                df_estadio = mysql_queries.sqlToDataFrame(f"SELECT * FROM estadios WHERE nome = '{nome}'")
                novo_estadio = Estadio(df_estadio.id.values[0], df_estadio.nome.values[0], df_estadio.cidade[0], df_estadio.estado[0])
                print(novo_estadio.to_string())
                
                # Pergunta se deseja inserir mais algum registro
                continuar = input("Deseja inserir mais algum registro? (Sim/Não): ").strip().lower()
                if continuar != 'sim':
                    print("Voltando ao menu principal...")
                    break
            else:
                print(f"O nome {nome} já está cadastrado! Defina outro.")

        return novo_estadio
        
    # Verifica se o nome já existe
    def verifica_existencia_nome_estadio(self, mysql_queries: MySQLQueries, nome: str = None) -> bool:
        df_estadio = mysql_queries.sqlToDataFrame(f"SELECT * FROM estadios WHERE nome = '{nome}'")
        return df_estadio.empty
    
    def verifica_existencia_estadio(self, mysql_queries: MySQLQueries, id: str = None) -> bool:
        df_estadio = mysql_queries.sqlToDataFrame(f"SELECT * FROM estadios WHERE id = '{id}'")
        return df_estadio.empty

    def atualizar_estadio(self) -> Estadio:
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        while True:
            id = int(input("Número (ID) do Estádio que deseja alterar: "))

            # Verifica se o estádio existe
            if not self.verifica_existencia_estadio(mysql, id):

                # Obtém os dados atuais do estádio
                df_estadio_atual = mysql.sqlToDataFrame(f"SELECT * FROM estadios WHERE id = {id}")
                estadio_atual = Estadio(df_estadio_atual.id.values[0], df_estadio_atual.nome.values[0], df_estadio_atual.cidade.values[0], df_estadio_atual.estado.values[0])

                print("Detalhes atuais do estádio:")
                print(estadio_atual.to_string())

                # Pergunta pelo novo nome, cidade e estado (mantém o valor atual se não for informado)
                novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ") or df_estadio_atual.nome.values[0]
                nova_cidade = input("Digite a nova cidade (ou pressione Enter para manter a atual): ") or df_estadio_atual.cidade.values[0]
                novo_estado = input("Digite o novo estado (ou pressione Enter para manter o atual): ") or df_estadio_atual.estado.values[0]

                # Atualiza o banco de dados com os novos valores (ou mantidos se o usuário não alterar)
                mysql.write(f"UPDATE estadios SET nome = '{novo_nome}', cidade = '{nova_cidade}', estado = '{novo_estado}' WHERE id = {id}")

                # Obtém os dados atualizados do estádio
                df_estadio_atualizado = mysql.sqlToDataFrame(f"SELECT * FROM estadios WHERE id = {id}")
                estadio_atualizado = Estadio(df_estadio_atualizado.id.values[0], df_estadio_atualizado.nome.values[0], df_estadio_atualizado.cidade.values[0], df_estadio_atualizado.estado.values[0])

                print("Estádio atualizado com sucesso:")
                print(estadio_atualizado.to_string())

            else:
                print(f"Não existe estádio com o número: {id}.")

            # Pergunta se deseja atualizar mais algum registro
            continuar = input("Deseja atualizar mais algum registro? (Sim/Não): ").strip().lower()
            if continuar != 'sim':
                print("Voltando ao menu principal...")
                break

        return estadio_atualizado


    def excluir_estadios(self):
        mysql = MySQLQueries(can_write=True)
        mysql.connect()

        while True:
            id = int(input("Número (ID) do Estadio que deseja excluir: "))

            if not self.verifica_existencia_estadio(mysql, id):
                df_estadio = mysql.sqlToDataFrame(f"SELECT * FROM estadios WHERE id = {id}")

                # Verificar se o estádio é uma FK em outra tabela
                df_partidas = mysql.sqlToDataFrame(f"SELECT * FROM partidas WHERE estadio_id = {id}")
                if not df_partidas.empty:
                    print(f"O estádio com ID {id} está vinculado a uma partida. Não pode ser excluído diretamente.")
                    excluir_partidas = input("Deseja excluir as partidas associadas? (Sim/Não): ").strip().lower()
                    if excluir_partidas == 'sim':
                        mysql.write(f"DELETE FROM partidas WHERE estadio_id = {id}")
                        print(f"Partidas associadas ao estádio {id} excluídas com sucesso.")
                    else:
                        print("Exclusão cancelada. Voltando ao menu principal.")
                        break

                mysql.write(f"DELETE FROM estadios WHERE id = {id}")
                estadio_excluido = Estadio(df_estadio.id.values[0], df_estadio.nome.values[0], df_estadio.cidade.values[0], df_estadio.estado.values[0])
                print("Estádio removido com sucesso!")
                print(estadio_excluido.to_string())
                
                # Pergunta se deseja excluir mais algum registro
                continuar = input("Deseja excluir mais algum registro? (Sim/Não): ").strip().lower()
                if continuar != 'sim':
                    print("Voltando ao menu principal...")
                    break
            else:
                print(f"Não existe estádio com esse número: {id}.")
