from utils import config
from reports.relatorios import Relatorio
from utils.splash_screen import SplashScreen
from controller.controller_estadios import Controller_Estadios
from controller.controller_times import Controller_Times
from controller.controller_jogadores import Controller_Jogadores
from controller.controller_partidas import Controller_Partidas
# from create_db_and_tables import create_database, create_tables

# create_database()
# create_tables()



tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_estadios = Controller_Estadios()
ctrl_times = Controller_Times()
ctrl_jogadores = Controller_Jogadores()
ctrl_partidas = Controller_Partidas()

def reports(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio_estadios()     
    elif opcao_relatorio == 2:
         relatorio.get_relatorio_times()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_jogadores()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_partidas()
    elif opcao_relatorio == 5:
        relatorio.get_relatorio_classificacao() 
    elif opcao_relatorio == 6:
        relatorio.get_relatorio_jogadores_por_time()
        
        #precisa alterar para colocar o agrupamento   


def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:                               
        novo_estadio = ctrl_estadios.inserir_estadios()
    elif opcao_inserir == 2:
        novo_time = ctrl_times.inserir_times()
    elif opcao_inserir == 3:
        novo_jogador = ctrl_jogadores.inserir_jogador()
    elif opcao_inserir == 4:
        nova_partida = ctrl_partidas.inserir_partida()

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_relatorio_estadios()
        estadios_atualizado = ctrl_estadios.atualizar_estadio()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_times()
        time_atualizado = ctrl_times.atualizar_time()
    elif opcao_atualizar == 3:
        relatorio.get_relatorio_jogadores()
        jogador_atualizado = ctrl_jogadores.atualizar_jogador()
    elif opcao_atualizar == 4:
        relatorio.get_relatorio_partidas()
        partida_atualizado = ctrl_partidas.atualizar_partida()

def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        relatorio.get_relatorio_estadios()
        ctrl_estadios.excluir_estadios()
    elif opcao_excluir == 2:                
        relatorio.get_relatorio_times()
        ctrl_times.excluir_times()
    elif opcao_excluir == 3:                
        relatorio.get_relatorio_jogadores()
        ctrl_jogadores.excluir_jogadores()
    elif opcao_excluir == 4:                
        relatorio.get_relatorio_partidas()
        ctrl_partidas.excluir_partida()
def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)
        
        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-6]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4: # Exlcuir Registros

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()