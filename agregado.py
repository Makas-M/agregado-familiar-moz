import pandas as pd

# distrito desejado
distrito = 'Chibuto'

# array dos distritos por provincia
distritoCD = ["Ancuabe","Balama","Chiúre","Ibo","Macomia","Mecúfi","Meluco","Metuge","Mocímboa da Praia","Montepuez","Mueda","Muidumbe","Namuno","Nangade","Palma","Pemba","Quissanga"]
distritoG = ["Bilene","Chibuto","Chicualacuala","Chigubo","Chókwè","Chongoene","Guijá","Limpopo","Mabalane","Manjacaze","Mapai","Massangena","Massingir","Xai-Xai"]
distritoI = ["Funhalouro","Govuro","Homoíne","Inhambane","Inharrime","Inhassoro","Jangamo","Mabote","Massinga","Maxixe","Morrumbene", "Panda","Vilanculos","Zavala"]
distritoMan = ["Bárue","Chimoio","Gondola","Guro","Macate","Machaze","Macossa","Manica","Mossurize","Sussundenga","Tambara","Vanduzi"]

# condicao para seleccao da provincia de acordo com o distrito
if (distrito in distritoCD):
    provincia = 'Cabo Delgado'
elif (distrito in distritoG):
    provincia = 'Gaza'
elif (distrito in distritoI):
    provincia = 'Inhambane'
elif (distrito in distritoMan):
    provincia = 'Manica'

# caminhos
caminho_arquivo = 'agregado.xlsx'
nome_da_planilha = 'Plan1'

coluna_agregado = 'Agregado' 
coluna_provincia = 'Provincia'

# arquivo
df = pd.read_excel(caminho_arquivo, sheet_name=nome_da_planilha)

# filtrar
dados_coluna = df[df[coluna_provincia] == provincia].values

# Imprimir 
print(dados_coluna)
print(distrito)
