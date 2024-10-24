MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Estádios
2 - Relatório de Times
3 - Relatório de Jogadores
4 - Relatório de Partidas
5 - CLASSIFICAÇÃO GERAL
6 - Relatório de Jogadores Agrupados por Times
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - ESTADIOS
2 - TIMES
3 - JOGADORES
4 - PARTIDAS
"""

# Consulta de contagem de registros por tabela
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=7):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")