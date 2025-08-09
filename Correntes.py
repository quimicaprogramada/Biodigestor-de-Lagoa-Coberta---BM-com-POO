#Módulo para definição da classes das correntes
#Declaração da classe corrente que será usada para instanciar os objetos
# correntes principais e correntes de lodo descartado
class Corrente:
    def __init__(self, Q=None, P=None):
        self.Q = Q
        self.P = P
