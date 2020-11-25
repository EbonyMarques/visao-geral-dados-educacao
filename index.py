import pandas as pd
from pandas_profiling import ProfileReport as pr

# df_enade = pd.read_csv("enade_presencas_validas_com.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")
# # df_ies = pd.read_csv("censo_superior_ies.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")

# df_enade = df_enade.drop_duplicates(subset=['CODIGO_IES'], ignore_index=True)
# ies_enade = df_enade['CODIGO_IES']

# # ies_enade.to_csv('ies_associadas_enade.csv', index=False)

# print(len(ies_enade))

# count = 0
# df_ies_final = None

# for i in ies_enade:
#     df = df_ies[df_ies['CODIGO_IES']==str(i)]
#     # print(df)
#     if count == 0:
#         df_ies_final = df
#         # print('é')
#     else:
#         # print('é não')
#         df_ies_final = df_ies_final.append(df, ignore_index=True)
#     count+=1

# df_ies_final.to_csv('ies_final.csv', index=False, encoding= "ISO-8859-1")

# print(len(list(df_ies_final.index)))

# profile = pr(df_ies_final, title='IES final', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("ies_final.html")



# df_enade = pd.read_csv("enade_presencas_validas_com.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")
# variaveis = list(df_enade)

# arquivo = open('variaveis_enade_2.txt','w')

# for i in variaveis:
#     arquivo.writelines(str(i)+'\n')

# arquivo.close()


# df_ies = pd.read_csv("censo_superior_ies.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")
# variaveis = list(df_ies)

# arquivo = open('variaveis_ies.txt','w')

# for i in variaveis:
#     arquivo.writelines(str(i)+'\n')

# arquivo.close()



# df_ies_enade = pd.read_csv("ies_associadas_enade.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")
# df_ies_possiveis = pd.read_csv("ies_final.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")
# df_enade = pd.read_csv("enade_presencas_validas_com.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")

# df_ies_enade = list(df_ies_enade['CODIGO_IES'])
# df_ies_possiveis = list(df_ies_possiveis['CODIGO_IES'])

# count_708 = 0
# count_18210 = 0
# count_4899 = 0

# for i, j in df_enade.iterrows():
#     if j['CODIGO_IES'] == '708':
#         count_708+=1
#     elif j['CODIGO_IES'] == '18210':
#         count_18210+=1
#     elif j['CODIGO_IES'] == '4899':
#         count_4899+=1

# print(count_708)
# print(count_18210)
# print(count_4899)


# df_ies_igc = pd.read_csv("ies_igc.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")
# df = df_ies_igc[df_ies_igc['CODIGO_IES']=='1356']
# print(df)



# df_enade = pd.read_csv("enade_presencas_validas_sem.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")
# # df_ies = pd.read_csv("censo_superior_ies.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")

# df_enade = df_enade.drop_duplicates(subset=['CODIGO_IES', 'CODIGO_CURSO'], ignore_index=True)
# df_enade = df_enade[['CODIGO_IES','CODIGO_CURSO']]

# # ies_enade.to_csv('ies_associadas_enade.csv', index=False)

# # print(len(ies_enade))

# df_enade.to_csv('enade_ies_cursos.csv', index=False, encoding= "ISO-8859-1")

# profile = pr(df_enade, title='Enade + IES + sursos', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("enade_ies_cursos.html")



# df_enade_ies_cursos = pd.read_csv("enade_ies_cursos.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")
# df_cpc = pd.read_csv("cpc.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")

# print("Começando join")
# df_final = df_enade_ies_cursos.join(df_cpc.set_index(['CODIGO_IES', 'CODIGO_CURSO']), on=['CODIGO_IES', 'CODIGO_CURSO'])
# print("Finalizando join")

# df_final.to_csv('enade_ies_cursos_cpc.csv', index=False)

# profile = pr(df_final, title='Enade + IES + sursos', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("enade_ies_cursos.html")










# df_enade = pd.read_csv("enade_presencas_validas_sem.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")

# df_enade = df_enade.drop_duplicates(subset=['CODIGO_IES'], ignore_index=True)
# df_enade = df_enade['CODIGO_IES']

# df_enade.to_csv('enade_ies_menor.csv', index=False)


# df_enade = pd.read_csv("enade_presencas_validas_sem.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")

# df_enade = df_enade.drop_duplicates(subset=['CODIGO_IES', 'CODIGO_CURSO'], ignore_index=True)
# df_enade = df_enade[['CODIGO_IES', 'CODIGO_CURSO']]

# df_enade.to_csv('enade_ies_cursos_menor.csv', index=False)



# df_enade_1 = pd.read_csv("enade_presencas_validas_final.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")
# df_enade_2 = pd.read_csv("enade_presencas_validas_sem_missing.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")

# df_enade_1 = df_enade_1['CODIGO_IES']
# df_enade_1 = df_enade_1.drop_duplicates()

# df_enade_2 = df_enade_2['CODIGO_IES']
# df_enade_2 = df_enade_2.drop_duplicates()

# l1 = list(df_enade_1)
# l2 = list(df_enade_2)

# for i in l2:
#     if i not in l1:
#         print(i)



df_enade = pd.read_csv("enade_final.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")
# # df_ies = pd.read_csv("censo_superior_ies.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")

df_enade = df_enade.drop_duplicates(subset=['CODIGO_IES'], ignore_index=True)
ies_enade = df_enade['CODIGO_IES']

ies_enade.to_csv('ies_associadas_enade.csv', index=False)
