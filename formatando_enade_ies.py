import pandas as pd
from pandas_profiling import ProfileReport as pr

# pd.set_option("max_columns", None)
# pd.set_option("max_rows", None)

# df_enade = pd.read_csv("enade_presencas_validas_sem_missing_com_escopo_menor_n.csv", sep=",", encoding="ISO-8859-1", dtype='unicode')
df_enade = pd.read_csv("enade_presencas_validas_sem_missing_com_escopo_maior.csv", sep=",", encoding="ISO-8859-1", dtype='unicode')
df_ies = pd.read_csv("censo_superior_ies.csv", sep=",", encoding="ISO-8859-1", dtype='unicode')

df_ies.drop('CATEGORIA_ADMINISTRATIVA_IES', axis=1, inplace=True)
df_ies.drop('ORGANIZACAO_ACADEMICA_IES', axis=1, inplace=True)
df_ies.drop('CODIGO_REGIAO_IES', axis=1, inplace=True)
df_ies.drop('CODIGO_UNIDADE_FEDERATIVA_IES', axis=1, inplace=True)
df_ies.drop('CODIGO_MUNICIPIO_IES', axis=1, inplace=True)

print("Começando join")
df_final = df_enade.join(df_ies.set_index('CODIGO_IES'), on='CODIGO_IES')
print("Finalizando join")

df_final.to_csv('enade_sem_missing_com_escopo_maior_ies.csv', index=False, encoding="ISO-8859-1")

profile = pr(df_final, title='ENADE + IES', minimal=True, html={'style':{'full_width':True}})
profile.to_file("profiling_enade_sem_missing_com_escopo_maior_ies.html")