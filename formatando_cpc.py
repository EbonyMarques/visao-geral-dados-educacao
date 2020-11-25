import pandas as pd
from pandas_profiling import ProfileReport as pr

df_cpc_2018 = pd.read_excel("indices/2018/cpc_2018.xlsx", dtype='unicode')
df_cpc_2017 = pd.read_excel("indices/2017/cpc_2017.xlsx", dtype='unicode')
df_cpc_2016 = pd.read_excel("indices/2016/cpc_2016.xls", dtype='unicode')
df_cpc_2015 = pd.read_excel("indices/2015/cpc_2015.xls", dtype='unicode')

df_cpc_2018 = df_cpc_2018[['Ano','Código da IES','Código do Curso','CPC (Faixa)']]

df_cpc_2018.rename(columns={'Ano': 'ANO_CPC',
                            'Código da IES': 'CODIGO_IES',
                            'Código do Curso': 'CODIGO_CURSO',
                            'CPC (Faixa)': 'CPC_FAIXA'}, inplace=True)

df_cpc_2017 = df_cpc_2017[['Edição','Código da IES','Código do Curso','CPC Faixa']]

df_cpc_2017.rename(columns={'Edição': 'ANO_CPC',
                            'Código da IES': 'CODIGO_IES',
                            'Código do Curso': 'CODIGO_CURSO',
                            'CPC Faixa': 'CPC_FAIXA'}, inplace=True)

df_cpc_2016 = df_cpc_2016[['Ano','Código da IES','Código do Curso','CPC Faixa']]

df_cpc_2016.rename(columns={'Ano': 'ANO_CPC',
                            'Código da IES': 'CODIGO_IES',
                            'Código do Curso': 'CODIGO_CURSO',
                            'CPC Faixa': 'CPC_FAIXA'}, inplace=True)
                            
df_cpc_2015 = df_cpc_2015[['Ano','Código da IES','Código do Curso','CPC Faixa']]

df_cpc_2015.rename(columns={'Ano': 'ANO_CPC',
                            'Código da IES': 'CODIGO_IES',
                            'Código do Curso': 'CODIGO_CURSO',
                            'CPC Faixa': 'CPC_FAIXA'}, inplace=True)
                            
df_cpc = df_cpc_2018
df_cpc = df_cpc.append(df_cpc_2017, ignore_index=True)
df_cpc = df_cpc.append(df_cpc_2016, ignore_index=True)
df_cpc = df_cpc.append(df_cpc_2015, ignore_index=True)

df_cpc.drop_duplicates(subset=['CODIGO_IES', 'CODIGO_CURSO'],ignore_index=True, inplace=True)

df_cpc.to_csv('cpc.csv', index=False)

profile = pr(df_cpc, title='cpc', minimal=True, html={'style':{'full_width':True}})
profile.to_file("cpc.html")

# profile = pr(df_cpc_2017, title='cpc de 2017', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("cpc_2017.html")

# profile = pr(df_cpc_2016, title='cpc de 2016', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("cpc_2016.html")

