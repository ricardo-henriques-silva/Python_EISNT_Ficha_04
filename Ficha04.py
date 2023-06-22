import pandas as pd

# Carregar dados do Excel
dados = pd.read_excel('P_Data_Extract_From_World_Development_Indicators.xlsx', sheet_name='Data')

# Selecionar as colunas de interesse (País, Ano e Consumo de Energia)
dados = dados[['Country Name', '1990 [YR1990]', '2000 [YR2000]']]

# Filtrar os dados para o Brasil
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