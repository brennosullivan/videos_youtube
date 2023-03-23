import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


lista_medalion = range(1988, 2019)



lista_dfs = []

df = pd.DataFrame()

def calculadora_de_montante_juros_compostos(valor_inicial, taxa, tempo_total_do_investimento, aporte = 0, escala = "M"):

    if escala in ["M", "A", "D"]:
        
        tempo_investido = 0

        lista_dfs.append(pd.DataFrame(data={'Acumulado': 100}, index= [lista_medalion[tempo_investido]]))

        vetor_montante_ao_longo_do_tempo = []

        while tempo_investido < tempo_total_do_investimento:

            if tempo_investido == 0:

                valor_final = valor_inicial + ((valor_inicial + aporte) * (taxa/100)) 
                
                valor_ganho = ((valor_inicial + aporte) * (taxa/100))

                tempo_investido = tempo_investido + 1

                vetor_montante_ao_longo_do_tempo.append(valor_final)

                lista_dfs.append(pd.DataFrame(data={'Acumulado': valor_final}, index= [lista_medalion[tempo_investido]]))

            else:

                valor_final = valor_final + (valor_final * (taxa/100)) + aporte

                valor_ganho = (valor_final * (taxa/100)) + aporte

                tempo_investido = tempo_investido + 1

                vetor_montante_ao_longo_do_tempo.append(valor_final)

                lista_dfs.append(pd.DataFrame(data={'Acumulado': valor_final}, index=[lista_medalion[tempo_investido]]))

        
        return pd.concat(lista_dfs)

    else:

        return('Escolha uma escala válida')


vetor_medallion = calculadora_de_montante_juros_compostos(valor_inicial = 100, taxa=66, tempo_total_do_investimento=30, escala="A")

vetor_medallion = vetor_medallion.round(0)

print(vetor_medallion)



# #arroz

# arroz_ao_longo_do_tempo = calculadora_de_montante_juros_compostos(valor_inicial = 0.01, 
#                                                                                 taxa = 100, tempo_total_do_investimento = 30 
#                                                                                 ,aporte = 0, escala = "D")

# print(arroz_ao_longo_do_tempo)

# fig, ax = plt.subplots()

# ax.plot(np.arange(0, 30, 1), arroz_ao_longo_do_tempo)
# ax.set_xlabel("Dias",fontsize=14)
# ax.set_ylabel("Reais",color="blue",fontsize=14)
# ax.set_title('Valor acumulado ao longo dos dias')

# ax.yaxis.set_major_formatter('R${x:,}')

# plt.show()



# aporte_variavel = range(0, 5000)

# montante_final_primeiro_periodo_variavel = []


# for aporte in aporte_variavel:


#     montantes_estagiario_primeiro_periodo = calculadora_de_montante_juros_compostos(valor_inicial = 0, 
#                                                                                 taxa = 0.8, tempo_total_do_investimento = 96 #8 anos
#                                                                                 ,aporte = aporte, escala = "M")

#     montantes_estagiario_segundo_periodo = calculadora_de_montante_juros_compostos(valor_inicial = montantes_estagiario_primeiro_periodo[-1], 
#                                                                                 taxa = 0.8, tempo_total_do_investimento = 264 #22 anos
#                                                                                 ,aporte = 5000, escala = "M")


#     montante_final_estag = montantes_estagiario_segundo_periodo[-1]

#     montante_final_primeiro_periodo_variavel.append(montante_final_estag)


# aporte_variavel = range(5000, 10000)

# montante_final_segundo_periodo_variavel = []


# for aporte in aporte_variavel:


#     montantes_estagiario_primeiro_periodo = calculadora_de_montante_juros_compostos(valor_inicial = 0, 
#                                                                                 taxa = 0.8, tempo_total_do_investimento = 96 #8 anos
#                                                                                 ,aporte = 300, escala = "M")

#     montantes_estagiario_segundo_periodo = calculadora_de_montante_juros_compostos(valor_inicial = montantes_estagiario_primeiro_periodo[-1], 
#                                                                                 taxa = 0.8, tempo_total_do_investimento = 264 #22 anos
#                                                                                 ,aporte = aporte, escala = "M")


#     montante_final_estag = montantes_estagiario_segundo_periodo[-1]

#     montante_final_segundo_periodo_variavel.append(montante_final_estag)

# aporte_variavel = range(10000, 15000)

# lista_montante_final_gerente = []


# for aporte in aporte_variavel:


#     montantes_gerente = calculadora_de_montante_juros_compostos(valor_inicial = 0, 
#                                                             taxa = 0.8, tempo_total_do_investimento = 264 #22 anos, começou com 28
#                                                             ,aporte = aporte, escala = "M")


#     montante_final_gerente= montantes_gerente[-1]

#     lista_montante_final_gerente.append(montante_final_gerente)



# fig, ax = plt.subplots()

# ax.plot(range(0, 5000), lista_montante_final_gerente, color = "purple", label = "Gerente")
# ax.plot(montante_final_segundo_periodo_variavel, color = "blue", label = "Gerente tardio")
# ax.plot(montante_final_primeiro_periodo_variavel, color = "green", label = "Estagiário rico")
# ax.yaxis.set_major_formatter('R${x:,}')
# ax.legend()

# plt.show()

















# montantes_estagiario_primeiro_periodo = calculadora_de_montante_juros_compostos(valor_inicial = 0, 
#                                                                                 taxa = 0.8, tempo_total_do_investimento = 96 #8 anos
#                                                                                 ,aporte = 2500, escala = "M")

# montantes_estagiario_segundo_periodo = calculadora_de_montante_juros_compostos(valor_inicial = montantes_estagiario_primeiro_periodo[-1], 
#                                                                                 taxa = 0.8, tempo_total_do_investimento = 384 #32 anos
#                                                                                 ,aporte = 7500, escala = "M")

# montante_ao_longo_do_tempo_estag = montantes_estagiario_primeiro_periodo + montantes_estagiario_segundo_periodo

# montantes_gerente = calculadora_de_montante_juros_compostos(valor_inicial = 0, 
#                                                             taxa = 0.8, tempo_total_do_investimento = 384 #32 anos, começou com 28
#                                                             ,aporte = 12500, escala = "M")


# montante_sem_aporte = list(np.zeros(96))

# montante_final_gerente = montante_sem_aporte + montantes_gerente

# fig, ax = plt.subplots()

# ax.plot(np.arange(0, 40, 0.0834), montante_ao_longo_do_tempo_estag, label = "Estagiário")
# ax.plot(np.arange(0, 40, 0.0834), montante_final_gerente, color = "purple", label = "Gerente")
# ax.set_xlabel("Anos",fontsize=14)
# ax.set_ylabel("Montante",color="blue",fontsize=14)
# ax.legend()
# ax.yaxis.set_major_formatter('R${x:,}')

# plt.show()


#nunca é linear o crescimento dos seus aportes ao longo da vida
#a sua história de vida ta longe de ser linear
#investir em você mesmo no início da vida quase sempre vale a pena
#Quer que eu faça outro video simulando a diferença entre aumentar 0.2% a rentabilidade todos os meses? deixa nos comentários
