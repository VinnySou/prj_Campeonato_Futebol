from model.times import Time
class Jogador:
    def __init__(self,
                 id:int=None,
                 nome:str=None,
                 posicao:str=None,
                 numero:int=None,
                 time:Time=None):
        self.set_id(id)
        self.set_nome(nome)
        self.set_posicao(posicao)
        self.set_numero(numero)
        self.set_time(time)
        

    def set_id(self, id:int):
        self.id = id

    def set_nome(self, nome:str):
        self.nome = nome  
    
    def set_posicao(self, posicao:str):
        self.posicao = posicao

    def set_numero(self, numero:int):
        self.numero = numero 
    
    def set_time(self, time:Time):
        self.time = time

    def get_id(self) -> int:
        return self.id
    
    def get_nome(self) -> str:
        return self.nome 
    
    def get_posicao(self) -> str:
        return self.posicao
    
    def get_numero(self) -> int:
        return self.numero
    
    def get_time(self) -> Time:  
        return self.time
    
    def to_string(self):
        time_info = f"Time ID: {self.time.get_id()}" if self.time else "Sem Time"
        return (f"Jogador: Matricula (ID): {self.id} | Nome: {self.nome} | "
                f"Numero: {self.numero} | Posicao: {self.posicao} | {time_info}")