#Módulo para calcular dosagem de produtos químicos
class Solução_Cal:
    def __init__(self,Pureza,):
        self.Estequiometria = 3.581
        self.Pureza = Pureza
        self.Diluição = Diluição

    def calcular_Dosagem(self, ConcentraçãoP):
        return self.Estequiometria*ConcentraçãoP/self.Diluição

    def calcular_Consumo(self, Dosagem, Entrada):
        return Dosagem*Entrada/self.Pureza