import pandas as pd

# coluna desejada
provincia = 'Maputo Cidade'
# caminhos
caminho_arquivo = 'agregado.xlsx'
nome_da_planilha = 'Plan1'

coluna_agregado = 'Agregado' 
coluna_provincia = 'Provincia'

# Carregar o arquivo
df = pd.read_excel(caminho_arquivo, sheet_name=nome_da_planilha)

# filtrar
dados_coluna = df[df[coluna_provincia] == provincia]


# Imprimir os dados
print(dados_coluna)
