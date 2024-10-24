from datetime import date, time
import numpy as np
from model.times import Time
from model.estadios import Estadio

class Partida:
    def __init__(self, 
                 id: int = None, 
                 data: date = None, 
                 horario: time = None,
                 time_casa: Time = None, 
                 time_visitante: Time = None, 
                 estadio: Estadio = None,
                 gols_casa:int = None,
                 gols_visitante:int = None):
        self.set_id(id)
        self.set_data(data)
        self.set_horario(horario)
        self.set_time_casa(time_casa)
        self.set_time_visitante(time_visitante)
        self.set_estadio(estadio)
        self.set_gols_casa(gols_casa)
        self.set_gols_visitante(gols_visitante)
    def set_id(self, id: int):
        self.id = id
    
    def set_data(self, data: date):
        self.data = data

    def set_horario(self, horario: time):
        self.horario = horario
    
    def set_time_casa(self, time_casa: Time):
        self.time_casa = time_casa
        
    def set_time_visitante(self, time_visitante: Time):
        self.time_visitante = time_visitante
        
    def set_estadio(self, estadio: Estadio):
        self.estadio = estadio
    
    def set_gols_casa(self, gols_casa: int):
        self.gols_casa = gols_casa
        
    def set_gols_visitante(self, gols_visitante: int):
        self.gols_visitante = gols_visitante
        
    def get_id(self) -> int:
        return self.id
    
    def get_data(self) -> date:
        return self.data
    
    def get_horario(self) -> time:
        return self.horario
       
    def get_time_casa(self) -> Time:
        return self.time_casa
    
    def get_time_visitante(self) -> Time:
        return self.time_visitante
    
    def get_estadio(self) -> Estadio:
        return self.estadio
    
    def get_gols_casa(self) -> int:
        return self.gols_casa
    
    def get_gols_visitante(self) -> int:
        return self.gols_visitante
        
    def to_string(self):
        # Conversão de horário
        if isinstance(self.horario, time):
            horario_formatado = self.horario.strftime('%H:%M:%S')
        else:
            horario_formatado = 'Formato de horário inválido'
        
        return (f"Partida ID: {self.get_id()} | Data: {self.get_data()} | "
                f"Horário: {horario_formatado} | "
                f"Estádio: {self.get_estadio().get_nome()} | "
                f"Time Casa: {self.get_time_casa().get_nome()} | "
                f"Total de Gols Time da Casa: {self.get_gols_casa()} | "
                f"Total de Gols Visitante: {self.get_gols_visitante()}")