class Time:
    def __init__(self, 
                id:int=None,
                nome:str=None,
                cidade:str=None,
                estado:str=None):
        self.set_id(id)
        self.set_nome(nome)
        self.set_cidade(cidade)
        self.set_estado(estado)

    def set_id(self, id:int):
        self.id = id
    
    def set_nome(self, nome:str):
        self.nome = nome

    def set_cidade(self, cidade:str):
        self.cidade = cidade
    
    def set_estado(self, estado:str):
        self.estado= estado


    def get_id(self) -> int:
        return self.id
    
    def get_nome(self) -> str:
        return self.nome
    
    def get_cidade(self) -> str:
        return self.cidade
    
    def get_estado(self) -> str:
        return self.estado
    
    def to_string(self) -> str:
        return f"Time: Número (ID): {self.get_id()}, Nome: {self.get_nome()}, Cidade: {self.get_cidade()} Estado: {self.get_estado()} "