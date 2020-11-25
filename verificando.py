import pandas as pd
from pandas_profiling import ProfileReport as pr

pd.set_option("max_columns", None)
pd.set_option("max_rows", None)

df_enade_1 = pd.read_csv("enade_2.csv", sep=",", encoding="ISO-8859-1", dtype='unicode') #MENOR
df_enade_2 = pd.read_csv("enade_final_1.csv", sep=",", encoding="ISO-8859-1", dtype='unicode') #MAIOR

df_enade_1 = df_enade_1['CODIGO_IES']
# df_enade_2 = df_enade_2['CODIGO_IES']

df = df_enade_2[~df_enade_2['CODIGO_IES'].isin(list(df_enade_1))]

print(len(df.index))

for i,j in df.iterrows():
    print(j)
    input()

# for i, j in df_enade.iterrows():
#     msg = ''
#     if j['CATEGORIA_ADM_IES'] != j['CATEGORIA_ADMINISTRATIVA_IES']:
#         msg+='diferente,'
#     if j['ORGANIZACAO_ACAD_IES'] != j['ORGANIZACAO_ACADEMICA_IES']:
#         msg+='diferente'
#     if msg!='':
#         print(msg)


# df_enade = df_enade[['CODIGO_IES','CATEGORIA_ADM_IES','CATEGORIA_ADMINISTRATIVA_IES','ORGANIZACAO_ACAD_IES','ORGANIZACAO_ACADEMICA_IES']]

# df_enade.to_csv('verificando_enade.csv',index=False)

# profile = pr(df_enade, title='IES + IGC', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("verificando_enade.html")