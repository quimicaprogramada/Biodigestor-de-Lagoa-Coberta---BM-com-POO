#Módulo para descrição da classe dos reatores
from Correntes import Corrente
class Reator:
    def __init__(self, Ef):
        self.Ef = Ef

    def calcular_Q(self, QEntrada,QSaida):
        return (QEntrada.Q - QSaida.Q)

    def calcular_P(self, QEntrada):
        return (1-self.Ef)*QEntrada.P


