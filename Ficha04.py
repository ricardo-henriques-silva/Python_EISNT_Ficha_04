import pandas as pd

# Carregar dados do Excel
dados = pd.read_excel('P_Data_Extract_From_World_Development_Indicators.xlsx', sheet_name='Data')

# Selecionar as colunas de interesse (País, Ano e Consumo de Energia)
dados = dados[['Country Name', '1990 [YR1990]', '2000 [YR2000]']]

# Filtrar os dados para Portugal
dados_portugal = dados[dados['Country Name'] == 'Portugal']

# Calcular a variação percentual
def calcular_variacao_percentual(consumo_inicial, consumo_final):
    return (consumo_final - consumo_inicial) / consumo_inicial * 100

# Extrair os valores para o Brasil
consumo_1990 = dados_portugal['1990 [YR1990]'].values[0]
consumo_2000 = dados_portugal['2000 [YR2000]'].values[0]

# Calcular e imprimir a variação percentual
variacao_percentual = calcular_variacao_percentual(consumo_1990, consumo_2000)
print(f'Variação percentual no consumo de energia elétrica em Portugal entre 1990 e 2000: {variacao_percentual:.2f}%')


# # === Explorar funções do Numpy

import numpy as np
anos = np.array(['2001','2011','2021'])
PIB_milhoes = np.array([ 139222.3, 180748.3,187432.5])
Investimento_percent = np.array([0.267,0.274,0.184]) 

Investimento_milhoes = PIB_milhoes*Investimento_percent

print('\nInvestimento em milhões de euros entre 2001 e 2021')
print(anos)
print(Investimento_milhoes)

print('\nMédia do Investimento em milhões de euros')
print(np.mean(Investimento_milhoes))


# # === Explorar funções do Matplotlib

import matplotlib.pyplot as plt

plt.barh(anos,Investimento_milhoes,color='#AA0000',label='Investimento')
plt.title('Investimento em milhões de euros entre 2001 e 2021')
plt.ylabel('Anos', fontdict='Bahnschrift')
plt.xlabel('Milhões €', fontdict='Bahnschrift')
plt.legend()
plt.show()