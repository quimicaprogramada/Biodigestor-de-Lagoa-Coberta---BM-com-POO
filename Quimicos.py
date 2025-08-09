#Módulo para calcular dosagem de produtos químicos
class Solução_Cal:
    def __init__(self,Pureza,Concentração):
        self.Estequiometria = 3.581
        self.Pureza = Pureza
        self.Concentração = Concentração

    def calcular_Dosagem(self, ConcentraçãoP):
        return self.Estequiometria*ConcentraçãoP/self.Concentração

    def calcular_Consumo(self, Dosagem, Entrada):
        return Dosagem*Entrada/self.Pureza