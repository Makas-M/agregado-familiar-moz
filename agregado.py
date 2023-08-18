import pandas as pd

# caminhos
caminho_arquivo = 'agregado.xlsx'
nome_da_planilha = 'Plan1'

coluna_agregado = 'Agregado' 
coluna_provincia = 'Provincia'

# Carregar o arquivo
df = pd.read_excel(caminho_arquivo, sheet_name=nome_da_planilha)

# Extrair dados da coluna
dados_coluna = df[coluna_agregado]

# Imprimir os dados da coluna
print(dados_coluna)
