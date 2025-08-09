#Inicializar as correntes
from Correntes import Corrente
from Processos import Reator
from Equipamentos import Unidades_com_TRH
from Quimicos import Solução_Cal

#Início do dimensionamento
#Definição das correntes com dados disponíveis
Alimentação = Corrente(220, 1.33)
Lodo1 = Corrente(8)
Lodo2 = Corrente(6)
#Definição das características dos reatores
BiodigestorLC = Reator(0.86)
Nitri_Desnitri = Reator(0.75)
Mistura_Decantador = Reator(0.90)
#Calculando o balanço de massa
#Os argumentos do metodo 'calcular_Q' deve ser um objeto (e não um float)
#Para poder utilizar o valor Qb para o cálculo de Qn_d com
#o metodo 'calcular_Q' foi necessário transformá-lo num objeto Corrente
Qb = Corrente(BiodigestorLC.calcular_Q(Alimentação, Lodo1))
Qn_d = Nitri_Desnitri.calcular_Q(Qb, Lodo2)
print("--------------Cálculo das vazões-------------------")
print("Vazão do efluente do Biodigestor de Lagoa Coberta (Qb):", Qb.Q, "m3/d")
print("Vazão do efluente do Nitri/Desnitri (Qn_d):", Qn_d, "m3/d")
#Calculando o balando de fósforo nas correntes principais
#Fósforo na saída do digestato
Pb=BiodigestorLC.calcular_P(Alimentação)
#Usar o dado de Qb e Pb para definir a corrente do Digestato
print("--------Cálculo das concentrações de fósforo---------")
print(f"Fósforo na corrente de saída do digestado (Pd):{Pb:.4f} g/L")
Digestato = Corrente(Q=Qb, P=Pb)
Pn_d=Nitri_Desnitri.calcular_P(Digestato)
print(f"Fósforo na corrente de saída da nitrificação/desnitrificação (Pn_d):{Pn_d:.4f} g/L")
EfluenteN_D = Corrente(Q=Qn_d, P=Pn_d)
Pf = Mistura_Decantador.calcular_P(EfluenteN_D)
print(f"Fósforo na corrente de final (Pf):{Pf:.4f} g/L")
#Criação dos objetos Unidade de Mistura rápida e decantador com
#atributo tempo de retenção hidráulica TRH
Unidade_MR = Unidades_com_TRH(1/1440)
Decantador = Unidades_com_TRH(6/24)
Volume_MR = 1000*Unidade_MR.calcular_V(Qn_d)
Volume_Decant = Decantador.calcular_V(Qn_d)
print("---------Cálculo do volume dos equipamentos-------")
print(f"Volume da Unidade de Mistura Rápida:{Volume_MR:.1f} L")
print(f"Volume do Decantador:{Volume_Decant:.1f} m3")
print("-----Cálculo da dosagem de produtos químicos------")
Cal=Solução_Cal(0.9,100)
Dosagem = Cal.calcular_Dosagem(Pn_d)
Carga_diária = Cal.calcular_Consumo(Dosagem, Qn_d)
print(f"Dosagem de solução preparada de Cal 10% :{1000*Dosagem:.2f} L/m3")
print(f"Carga diária de cal:{100*Carga_diária:.2f} kg/d")

