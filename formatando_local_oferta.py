import pandas as pd
from pandas_profiling import ProfileReport as pr

# df_local_2018 = pd.read_csv("educacao_superior/2018/dados/dm_local_oferta.csv", sep="|", encoding = "ISO-8859-1")
# df_local_2017 = pd.read_csv("educacao_superior/2017/dados/dm_local_oferta.csv", sep="|", encoding = "ISO-8859-1")
# df_local_2016 = pd.read_csv("educacao_superior/2016/dados/dm_local_oferta.csv", sep="|", encoding = "ISO-8859-1")

# df_local_2018.rename(columns={'NU_ANO_CENSO': 'ANO_CENSO_LOCAL_OFERTA',
#                             'CO_LOCAL_OFERTA': 'CODIGO_LOCAL_OFERTA',
#                             'NO_LOCAL_OFERTA': 'NOME_LOCAL_OFERTA',
#                             'CO_IES': 'CODIGO_IES',
#                             'IN_SEDE': 'INDICADOR_SEDE_LOCAL_OFERTA',
#                             'CO_CURSO_POLO': 'CODIGO_CURSO_POLO_LOCAL_OFERTA',
#                             'CO_CURSO': 'CODIGO_CURSO',
#                             'IN_LOCAL_OFERTA_NEAD': 'INDICADOR_LOCAL_OFERTA_NEAD',
#                             'IN_LOCAL_OFERTA_UAB': 'INDICADOR_LOCAL_OFERTA_UAB',
#                             'IN_LOCAL_OFERTA_REITORIA': 'INDICADOR_LOCAL_OFERTA_REITORIA',
#                             'IN_LOCAL_OFERTA_POLO': 'INDICADOR_LOCAL_OFERTA_POLO',
#                             'IN_LOCAL_OFERTA_UNID_ACADEMICA': 'INDICADOR_LOCAL_OFERTA_UNIDADE_ACADEMICA',
                            
#                             'CO_UF': 'CODIGO_UNIDADE_FEDERATIVA_LOCAL_OFERTA',
#                             'CO_MUNICIPIO': 'CODIGO_MUNICIPIO_LOCAL_OFERTA',
#                             'IN_CAPITAL': 'INDICADOR_CAPITAL_LOCAL_OFERTA',
#                             'QT_COMPUTADOR_DISCENTE': 'QTDE_COMPUTADORES_DISCENTE_LOCAL_OFERTA',
#                             'IN_ACESSIBILIDADE': 'INDICADOR_ACESSIBILIDADE_LOCAL_OFERTA',
#                             'IN_SINALIZACAO_TATIL': 'INDICADOR_SINALIZACAO_TATIL_LOCAL_OFERTA',
#                             'IN_RAMPA_ACESSO_CORRIMAO': 'INDICADOR_RAMPA_ACESSO_CORRIMAO_LOCAL_OFERTA',
#                             'IN_ENTRADA_SAIDA_DIMENSAO': 'INDICADOR_ENTRADA_SAIDA_DIMENSAO_LOCAL_OFERTA',
#                             'IN_AMBIENTE_DESOBSTRUIDO': 'INDICADOR_AMBIENTE_DESOBSTRUIDO_LOCAL_OFERTA',
#                             'IN_SINALIZACAO_SONORA': 'INDICADOR_SINALIZACAO_SONORA_LOCAL_OFERTA',
#                             'IN_SINALIZACAO_VISUAL': 'INDICADOR_SINALIZACAO_VISUAL_LOCAL_OFERTA',
#                             'IN_EQUIPAMENTO_ELETROMECANICO': 'INDICADOR_EQUIPAMENTO_ELETROMECANICO_LOCAL_OFERTA',
#                             'IN_BANHEIRO_ADAPTADO': 'INDICADOR_BANHEIRO_ADAPTADO_LOCAL_OFERTA',
#                             'IN_ESPACO_ATENDIMENTO_ADAPTADO': 'INDICADOR_ESPACO_ATENDIMENTO_ADAPTADO_LOCAL_OFERTA',
#                             'IN_MOBILIARIO_ADAPTADO': 'INDICADOR_MOBILIARIO_ADAPTADO_LOCAL_OFERTA',
#                             'IN_BEBEDOURO_LAVABO_ADAPTADO': 'INDICADOR_BEBEDOURO_LAVABO_ADAPTADO_LOCAL_OFERTA',
#                             'IN_RESTAURANTE_UNIVERSITARIO': 'INDICADOR_RESTAURANTE_UNIVERSITARIO_LOCAL_OFERTA',
#                             'IN_QUADRA_POLIESPORTIVA': 'INDICADOR_QUADRA_POLIESPORTIVA_LOCAL_OFERTA',
#                             'IN_PISCINA': 'INDICADOR_PISCINA_LOCAL_OFERTA',
#                             'IN_QUADRA_COBERTA_GINASIO': 'INDICADOR_QUADRA_COBERTA_GINASIO_LOCAL_OFERTA',
#                             'IN_CINEMA': 'INDICADOR_CINEMA_LOCAL_OFERTA',
#                             'IN_VESTIARIO': 'INDICADOR_VESTIARIO_LOCAL_OFERTA',
#                             'IN_SERVICOS': 'INDICADOR_SERVICOS_LOCAL_OFERTA',
#                             'IN_ESTACIONAMENTO_DOCENTE': 'INDICADOR_ESTACIONAMENTO_DOCENTE_LOCAL_OFERTA',
#                             'IN_CANTINA_LANCHONETE': 'INDICADOR_CANTINA_LANCHONETE_LOCAL_OFERTA',
#                             'IN_PISTA_ATLETISMO': 'INDICADOR_PISTA_ATLETISMO_LOCAL_OFERTA',
#                             'IN_CAMPO_PRATICA_ESPORTIVA': 'INDICADOR_CAMPO_PRATICA_ESPORTIVA_LOCAL_OFERTA',
#                             'IN_AUDITORIO_TEATRO': 'INDICADOR_AUDITORIO_TEATRO_LOCAL_OFERTA',
#                             'IN_REDE_SEM_FIO_COMU_ACADEMICA': 'INDICADOR_REDE_SEM_FIO_COMUNIDADE_ACADEMICA_LOCAL_OFERTA',
#                             'IN_POSTO_ATENDIMENTO_1_SOCORRO': 'INDICADOR_POSTO_ATENDIMENTO_1_SOCORRO_LOCAL_OFERTA',
#                             'IN_BICICLETARIO': 'INDICADOR_BICICLETARIO_LOCAL_OFERTA',
#                             'IN_ESTACIONAMENTO_ALUNO': 'INDICADOR_ESTACIONAMENTO_ALUNO_LOCAL_OFERTA',
#                             'IN_MORADIA_ESTUDANTIL': 'INDICADOR_MORADIA_ESTUDANTIL_LOCAL_OFERTA',
#                             'IN_EQUIPA_VIDEOCONFERENCIA': 'INDICADOR_EQUIPAMENTO_VIDEOCONFERENCIA_LOCAL_OFERTA',
#                             'IN_SALA_COORDENACAO_POLO': 'INDICADOR_SALA_COORDENACAO_POLO_LOCAL_OFERTA',
#                             'IN_MICROCOMPUTADOR': 'INDICADOR_MICROCOMPUTADOR_LOCAL_OFERTA',
#                             'IN_POSSUI_INTERNET_BANDA_LARGA': 'INDICADOR_POSSUI_INTERNET_BANDA_LARGA_LOCAL_OFERTA',
#                             'IN_SALA_ATENDIMENTO_TUTOR': 'INDICADOR_SALA_ATENDIMENTO_TUTOR_LOCAL_OFERTA',

#                             }, inplace=True)

# df_local = df_local_2018

# df_local_2017.rename(columns={'NU_ANO_CENSO': 'ANO_CENSO_LOCAL_OFERTA',
#                             'CO_LOCAL_OFERTA': 'CODIGO_LOCAL_OFERTA',
#                             'NO_LOCAL_OFERTA': 'NOME_LOCAL_OFERTA',
#                             'CO_IES': 'CODIGO_IES',
#                             'IN_SEDE': 'INDICADOR_SEDE_LOCAL_OFERTA',
#                             'CO_CURSO_POLO': 'CODIGO_CURSO_POLO_LOCAL_OFERTA',
#                             'CO_CURSO': 'CODIGO_CURSO',
#                             'IN_LOCAL_OFERTA_NEAD': 'INDICADOR_LOCAL_OFERTA_NEAD',
#                             'IN_LOCAL_OFERTA_UAB': 'INDICADOR_LOCAL_OFERTA_UAB',
#                             'IN_LOCAL_OFERTA_REITORIA': 'INDICADOR_LOCAL_OFERTA_REITORIA',
#                             'IN_LOCAL_OFERTA_POLO': 'INDICADOR_LOCAL_OFERTA_POLO',
#                             'IN_LOCAL_OFERTA_UNID_ACADEMICA': 'INDICADOR_LOCAL_OFERTA_UNIDADE_ACADEMICA',
                            
#                             'CO_UF': 'CODIGO_UNIDADE_FEDERATIVA_LOCAL_OFERTA',
#                             'CO_MUNICIPIO': 'CODIGO_MUNICIPIO_LOCAL_OFERTA',
#                             'IN_CAPITAL': 'INDICADOR_CAPITAL_LOCAL_OFERTA',
#                             'QT_COMPUTADOR_DISCENTE': 'QTDE_COMPUTADORES_DISCENTE_LOCAL_OFERTA',
#                             'IN_ACESSIBILIDADE': 'INDICADOR_ACESSIBILIDADE_LOCAL_OFERTA',
#                             'IN_SINALIZACAO_TATIL': 'INDICADOR_SINALIZACAO_TATIL_LOCAL_OFERTA',
#                             'IN_RAMPA_ACESSO_CORRIMAO': 'INDICADOR_RAMPA_ACESSO_CORRIMAO_LOCAL_OFERTA',
#                             'IN_ENTRADA_SAIDA_DIMENSAO': 'INDICADOR_ENTRADA_SAIDA_DIMENSAO_LOCAL_OFERTA',
#                             'IN_AMBIENTE_DESOBSTRUIDO': 'INDICADOR_AMBIENTE_DESOBSTRUIDO_LOCAL_OFERTA',
#                             'IN_SINALIZACAO_SONORA': 'INDICADOR_SINALIZACAO_SONORA_LOCAL_OFERTA',
#                             'IN_SINALIZACAO_VISUAL': 'INDICADOR_SINALIZACAO_VISUAL_LOCAL_OFERTA',
#                             'IN_EQUIPAMENTO_ELETROMECANICO': 'INDICADOR_EQUIPAMENTO_ELETROMECANICO_LOCAL_OFERTA',
#                             'IN_BANHEIRO_ADAPTADO': 'INDICADOR_BANHEIRO_ADAPTADO_LOCAL_OFERTA',
#                             'IN_ESPACO_ATENDIMENTO_ADAPTADO': 'INDICADOR_ESPACO_ATENDIMENTO_ADAPTADO_LOCAL_OFERTA',
#                             'IN_MOBILIARIO_ADAPTADO': 'INDICADOR_MOBILIARIO_ADAPTADO_LOCAL_OFERTA',
#                             'IN_BEBEDOURO_LAVABO_ADAPTADO': 'INDICADOR_BEBEDOURO_LAVABO_ADAPTADO_LOCAL_OFERTA',
#                             'IN_RESTAURANTE_UNIVERSITARIO': 'INDICADOR_RESTAURANTE_UNIVERSITARIO_LOCAL_OFERTA',
#                             'IN_QUADRA_POLIESPORTIVA': 'INDICADOR_QUADRA_POLIESPORTIVA_LOCAL_OFERTA',
#                             'IN_PISCINA': 'INDICADOR_PISCINA_LOCAL_OFERTA',
#                             'IN_QUADRA_COBERTA_GINASIO': 'INDICADOR_QUADRA_COBERTA_GINASIO_LOCAL_OFERTA',
#                             'IN_CINEMA': 'INDICADOR_CINEMA_LOCAL_OFERTA',
#                             'IN_VESTIARIO': 'INDICADOR_VESTIARIO_LOCAL_OFERTA',
#                             'IN_SERVICOS': 'INDICADOR_SERVICOS_LOCAL_OFERTA',
#                             'IN_ESTACIONAMENTO_DOCENTE': 'INDICADOR_ESTACIONAMENTO_DOCENTE_LOCAL_OFERTA',
#                             'IN_CANTINA_LANCHONETE': 'INDICADOR_CANTINA_LANCHONETE_LOCAL_OFERTA',
#                             'IN_PISTA_ATLETISMO': 'INDICADOR_PISTA_ATLETISMO_LOCAL_OFERTA',
#                             'IN_CAMPO_PRATICA_ESPORTIVA': 'INDICADOR_CAMPO_PRATICA_ESPORTIVA_LOCAL_OFERTA',
#                             'IN_AUDITORIO_TEATRO': 'INDICADOR_AUDITORIO_TEATRO_LOCAL_OFERTA',
#                             'IN_REDE_SEM_FIO_COMU_ACADEMICA': 'INDICADOR_REDE_SEM_FIO_COMUNIDADE_ACADEMICA_LOCAL_OFERTA',
#                             'IN_POSTO_ATENDIMENTO_1_SOCORRO': 'INDICADOR_POSTO_ATENDIMENTO_1_SOCORRO_LOCAL_OFERTA',
#                             'IN_BICICLETARIO': 'INDICADOR_BICICLETARIO_LOCAL_OFERTA',
#                             'IN_ESTACIONAMENTO_ALUNO': 'INDICADOR_ESTACIONAMENTO_ALUNO_LOCAL_OFERTA',
#                             'IN_MORADIA_ESTUDANTIL': 'INDICADOR_MORADIA_ESTUDANTIL_LOCAL_OFERTA',
#                             'IN_EQUIPA_VIDEOCONFERENCIA': 'INDICADOR_EQUIPAMENTO_VIDEOCONFERENCIA_LOCAL_OFERTA',
#                             'IN_SALA_COORDENACAO_POLO': 'INDICADOR_SALA_COORDENACAO_POLO_LOCAL_OFERTA',
#                             'IN_MICROCOMPUTADOR': 'INDICADOR_MICROCOMPUTADOR_LOCAL_OFERTA',
#                             'IN_POSSUI_INTERNET_BANDA_LARGA': 'INDICADOR_POSSUI_INTERNET_BANDA_LARGA_LOCAL_OFERTA',
#                             'IN_SALA_ATENDIMENTO_TUTOR': 'INDICADOR_SALA_ATENDIMENTO_TUTOR_LOCAL_OFERTA',

#                             }, inplace=True)

# df_local = df_local.append(df_local_2017)

# df_local_2016.insert(1, "NU_ANO_CENSO", [2016]*len(df_local_2016.index), True)

# df_local_2016.drop('SGL_UF_LOCAL_OFERTA', axis=1, inplace=True)
# df_local_2016.drop('NO_MUNICIPIO_LOCAL_OFERTA', axis=1, inplace=True)
# df_local_2016.drop('DT_INICIO_FUNCIONAMENTO', axis=1, inplace=True)

# df_local_2016.rename(columns={'NU_ANO_CENSO': 'ANO_CENSO_LOCAL_OFERTA',
#                             'CO_LOCAL_OFERTA': 'CODIGO_LOCAL_OFERTA',
#                             'NO_LOCAL_OFERTA': 'NOME_LOCAL_OFERTA',
#                             'CO_IES': 'CODIGO_IES',
#                             'IN_SEDE': 'INDICADOR_SEDE_LOCAL_OFERTA',
#                             'CO_CURSO_POLO': 'CODIGO_CURSO_POLO_LOCAL_OFERTA',
#                             'CO_CURSO': 'CODIGO_CURSO',
#                             'IN_LOCAL_OFERTA_NEAD': 'INDICADOR_LOCAL_OFERTA_NEAD',
#                             'IN_LOCAL_OFERTA_UAB': 'INDICADOR_LOCAL_OFERTA_UAB',
#                             'IN_LOCAL_OFERTA_REITORIA': 'INDICADOR_LOCAL_OFERTA_REITORIA',
#                             'IN_LOCAL_OFERTA_POLO': 'INDICADOR_LOCAL_OFERTA_POLO',
#                             'IN_LOCAL_OFERTA_UNID_ACADEMICA': 'INDICADOR_LOCAL_OFERTA_UNIDADE_ACADEMICA',
                            
#                             'CO_UF_LOCAL_OFERTA': 'CODIGO_UNIDADE_FEDERATIVA_LOCAL_OFERTA',
#                             'CO_MUNICIPIO_LOCAL_OFERTA': 'CODIGO_MUNICIPIO_LOCAL_OFERTA',

#                             }, inplace=True)

# df_local = df_local.append(df_local_2016)

# df_local = df_local.drop_duplicates(subset=['CODIGO_LOCAL_OFERTA', 'CODIGO_IES', 'CODIGO_CURSO'],ignore_index=True)
# df_local.reset_index(drop=True, inplace=True)

# df_local.to_csv('censo_superior_local_oferta_com_missing.csv', index=False)

# profile = pr(df_local, title='Censo Escolar da Educação Superior: Local de Oferta', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("profiling_censo_educacao_superior_local_oferta_com_missing.html")

df_local = pd.read_csv("censo_superior_local_oferta_com_missing.csv", sep=",", encoding = "ISO-8859-1")

df_local = df_local.dropna()
df_local.reset_index(drop=True, inplace=True)

df_local.to_csv('censo_superior_local_oferta_sem_missing.csv', index=False)

profile = pr(df_local, title='Censo Escolar da Educação Superior: Local de Oferta', minimal=True, html={'style':{'full_width':True}})
profile.to_file("profiling_censo_educacao_superior_local_oferta_sem_missing.html")
