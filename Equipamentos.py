#Módulo para declaração da classe dos equipamentos
class Unidades_com_TRH:
    def __init__(self, TRH):
        self.TRH = TRH

    def calcular_V(self, Entrada):
        return self.TRH*Entrada
