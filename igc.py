import pandas as pd
from pandas_profiling import ProfileReport as pr

df_igc_2018 = pd.read_excel("indices/2018/igc_2018.xlsx", dtype='unicode')
df_igc_2017 = pd.read_excel("indices/2017/igc_2017.xlsx", dtype='unicode')
conjunto_2016 = pd.read_excel("indices/2016/igc_2016.xlsx", sheet_name=[0,1,2], dtype='unicode')
conjunto_2015 = pd.read_excel("indices/2015/igc_2015.xlsx", sheet_name=[0,1,2], dtype='unicode')

df_igc_2018 = df_igc_2018[['Ano','Código da IES','IGC (Faixa)']]

df_igc_2018.rename(columns={'Ano': 'ANO',
                            'Código da IES': 'CODIGO_IES',
                            'IGC (Faixa)': 'IGC_FAIXA'}, inplace=True)

df_igc_2017 = df_igc_2017[['Código da IES','IGC (Faixa)']]
df_igc_2017.insert(1,'ANO',['2017']*len(df_igc_2017.index),True)

df_igc_2017.rename(columns={'Código da IES': 'CODIGO_IES',
                            'IGC (Faixa)': 'IGC_FAIXA'}, inplace=True)

df_igc_2016 = conjunto_2016[0][['nu_ano','co_ies','fx_igc']]
df_igc_2016 = df_igc_2016.append(conjunto_2016[1][['nu_ano','co_ies','fx_igc']], ignore_index=True)
df_igc_2016 = df_igc_2016.append(conjunto_2016[2][['nu_ano','co_ies','fx_igc']], ignore_index=True)

df_igc_2016.rename(columns={'nu_ano':'ANO',
                            'co_ies': 'CODIGO_IES',
                            'fx_igc': 'IGC_FAIXA'}, inplace=True)
                            
df_igc_2015 = conjunto_2015[0][['Ano','Cód.IES','IGC (faixa)']]
df_igc_2015 = df_igc_2015.append(conjunto_2015[1][['Ano','Cód.IES','IGC (faixa)']], ignore_index=True)
df_igc_2015 = df_igc_2015.append(conjunto_2015[2][['Ano','Cód.IES','IGC (faixa)']], ignore_index=True)

df_igc_2015.rename(columns={'Ano':'ANO',
                            'Cód.IES': 'CODIGO_IES',
                            'IGC (faixa)': 'IGC_FAIXA'}, inplace=True)

df_igc = df_igc_2018
df_igc = df_igc.append(df_igc_2017, ignore_index=True)
df_igc = df_igc.append(df_igc_2016, ignore_index=True)
df_igc = df_igc.append(df_igc_2015, ignore_index=True)

df_igc.drop_duplicates(subset=['CODIGO_IES'],ignore_index=True, inplace=True)

df_igc.to_csv('igc_final.csv', index=False)

profile = pr(df_igc, title='IGC', minimal=True, html={'style':{'full_width':True}})
profile.to_file("igc_final.html")

# profile = pr(df_igc_2017, title='IGC de 2017', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("igc_2017.html")

# profile = pr(df_igc_2016, title='IGC de 2016', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("igc_2016.html")

