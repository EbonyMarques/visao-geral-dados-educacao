import pandas as pd
from pandas_profiling import ProfileReport as pr

df_ies_2018 = pd.read_csv("educacao_superior/2018/dados/dm_ies.csv", sep="|", encoding = "ISO-8859-1", dtype="unicode")
df_ies_2017 = pd.read_csv("educacao_superior/2017/dados/dm_ies.csv", sep="|", encoding = "ISO-8859-1", dtype="unicode")
df_ies_2016 = pd.read_csv("educacao_superior/2016/dados/dm_ies.csv", sep="|", encoding = "ISO-8859-1", dtype="unicode")
df_igc = pd.read_csv("igc.csv", sep=",", encoding="ISO-8859-1", dtype='unicode')

df_ies_2018.drop('IN_ACESSO_OUTRAS_BASES', axis=1, inplace=True)
df_ies_2018.drop('IN_ASSINA_OUTRA_BASE', axis=1, inplace=True)

df_ies_2018.rename(columns={'NU_ANO_CENSO': 'ANO_CENSO_IES',
                            'CO_IES': 'CODIGO_IES',
                            'NO_IES': 'NOME_IES',
                            'SG_IES': 'SIGLA_IES',
                            'CO_MANTENEDORA': 'CODIGO_MANTENEDORA_IES',
                            'NO_MANTENEDORA': 'NOME_MANTENEDORA_IES',
                            'TP_CATEGORIA_ADMINISTRATIVA': 'CATEGORIA_ADMINISTRATIVA_IES',
                            'TP_ORGANIZACAO_ACADEMICA': 'ORGANIZACAO_ACADEMICA_IES',
                            'CO_REGIAO': 'CODIGO_REGIAO_IES',
                            'CO_UF': 'CODIGO_UNIDADE_FEDERATIVA_IES',
                            'CO_MUNICIPIO': 'CODIGO_MUNICIPIO_IES',
                            'IN_CAPITAL': 'INDICADOR_CAPITAL_IES',

                            'QT_TEC_TOTAL': 'QTDE_TOTAL_TECNICOS_IES',
                            'QT_TEC_FUNDAMENTAL_COMP_FEM': 'QTDE_TECNICOS_FUNDAMENTAL_COMP_FEM_IES',
                            'QT_TEC_FUNDAMENTAL_COMP_MASC': 'QTDE_TECNICOS_FUNDAMENTAL_COMP_MASC_IES',
                            'QT_PERIODICO_ELETRONICO': 'QTDE_PERIODICOS_ELETRONICOS_IES',
                            'QT_LIVRO_ELETRONICO': 'QTDE_LIVROS_ELETRONICOS_IES',
                            'VL_DESPESA_PESQUISA': 'VALOR_DESPESA_PESQUISA_IES',
                            'QT_TEC_FUNDAMENTAL_INCOMP_FEM': 'QTDE_TECNICOS_FUNDAMENTAL_INCOMP_FEM_IES',
                            'QT_TEC_FUNDAMENTAL_INCOMP_MASC': 'QTDE_TECNICOS_FUNDAMENTAL_INCOMP_MASC_IES',
                            'QT_TEC_FUNDAMENTAL_COMP_FEM': 'QTDE_TECNICOS_FUNDAMENTAL_COMP_FEM_IES',
                            'QT_TEC_FUNDAMENTAL_COMP_MASC': 'QTDE_TECNICOS_FUNDAMENTAL_COMP_MASC_IES',
                            'QT_TEC_MEDIO_FEM': 'QTDE_TECNICOS_MEDIO_FEM_IES',
                            'QT_TEC_MEDIO_MASC': 'QTDE_TECNICOS_MEDIO_MASC_IES',
                            'QT_TEC_SUPERIOR_FEM': 'QTDE_TECNICOS_SUPERIOR_FEM_IES',
                            'QT_TEC_SUPERIOR_MASC': 'QTDE_TECNICOS_SUPERIOR_MASC_IES',
                            'QT_TEC_ESPECIALIZACAO_FEM': 'QTDE_TECNICOS_ESPECIALIZACAO_FEM_IES',
                            'QT_TEC_ESPECIALIZACAO_MASC': 'QTDE_TECNICOS_ESPECIALIZACAO_MASC_IES',
                            'QT_TEC_MESTRADO_FEM': 'QTDE_TECNICOS_MESTRADO_FEM_IES',
                            'QT_TEC_MESTRADO_MASC': 'QTDE_TECNICOS_MESTRADO_MASC_IES',
                            'QT_TEC_DOUTORADO_FEM': 'QTDE_TECNICOS_DOUTORADO_FEM_IES',
                            'QT_TEC_DOUTORADO_MASC': 'QTDE_TECNICOS_DOUTORADO_MASC_IES',
                            'QT_PERIODICO_ELETRONICO': 'QTDE_PERIODICOS_ELETRONICOS_IES',
                            'QT_LIVRO_ELETRONICO': 'QTDE_LIVROS_ELETRONICOS_IES',
                            'VL_RECEITA_PROPRIA': 'VALOR_RECEITA_PROPRIA_IES',
                            'VL_RECEITA_TRANSFERENCIA': 'VALOR_RECEITA_TRANSFERENCIA_IES',
                            'VL_RECEITA_OUTRA': 'VALOR_OUTRA_RECEITA_IES',
                            'VL_DESPESA_PESSOAL_DOCENTE': 'VALOR_DESPESA_PESSOAL_DOCENTE_IES',
                            'VL_DESPESA_PESSOAL_TECNICO': 'VALOR_DESPESA_PESSOAL_TECNICO_IES',
                            'VL_DESPESA_PESSOAL_ENCARGO': 'VALOR_DESPESA_PESSOAL_ENCARGO_IES',
                            'VL_DESPESA_CUSTEIO': 'VALOR_DESPESA_CUSTEIO_IES',
                            'VL_DESPESA_INVESTIMENTO': 'VALOR_DESPESA_INVESTIMENTO_IES',
                            'VL_DESPESA_PESQUISA': 'VALOR_DESPESA_PESQUISA_IES',
                            'VL_DESPESA_OUTRA': 'VALOR_OUTRA_DESPESA_IES',

                            'IN_ACESSO_PORTAL_CAPES': 'INDICADOR_ACESSO_PORTAL_CAPES_IES',
                            # 'IN_ASSINA_OUTRA_BASE': 'INDICADOR_ASSINA_OUTRA_BASE',
                            'IN_REPOSITORIO_INSTITUCIONAL': 'INDICADOR_REPOSITORIO_INSTITUCIONAL_IES',
                            'IN_BUSCA_INTEGRADA': 'INDICADOR_BUSCA_INTEGRADA_IES',
                            'IN_SERVICO_INTERNET': 'INDICADOR_SERVICO_INTERNET_IES',
                            'IN_PARTICIPA_REDE_SOCIAL': 'INDICADOR_PARTICIPACAO_REDE_SOCIAL_IES',
                            'IN_CATALOGO_ONLINE': 'INDICADOR_CATALOGO_ONLINE_IES',
                            'TP_REFERENTE': 'ENTIDADE_REFERENTE_DADO_FINANCEIRO_IES'
                            
                            }, inplace=True)

df_ies = df_ies_2018

df_ies_2017.drop('IN_ACESSO_OUTRAS_BASES', axis=1, inplace=True)

df_ies_2017.rename(columns={'NU_ANO_CENSO': 'ANO_CENSO_IES',
                            'CO_IES': 'CODIGO_IES',
                            'NO_IES': 'NOME_IES',
                            'SG_IES': 'SIGLA_IES',
                            'CO_MANTENEDORA': 'CODIGO_MANTENEDORA_IES',
                            'NO_MANTENEDORA': 'NOME_MANTENEDORA_IES',
                            'TP_CATEGORIA_ADMINISTRATIVA': 'CATEGORIA_ADMINISTRATIVA_IES',
                            'TP_ORGANIZACAO_ACADEMICA': 'ORGANIZACAO_ACADEMICA_IES',
                            'CO_REGIAO': 'CODIGO_REGIAO_IES',
                            'CO_UF': 'CODIGO_UNIDADE_FEDERATIVA_IES',
                            'CO_MUNICIPIO': 'CODIGO_MUNICIPIO_IES',
                            'IN_CAPITAL': 'INDICADOR_CAPITAL_IES',
                            
                            'QT_TEC_TOTAL': 'QTDE_TOTAL_TECNICOS_IES',
                            'QT_TEC_FUNDAMENTAL_COMP_FEM': 'QTDE_TECNICOS_FUNDAMENTAL_COMP_FEM_IES',
                            'QT_TEC_FUNDAMENTAL_COMP_MASC': 'QTDE_TECNICOS_FUNDAMENTAL_COMP_MASC_IES',
                            'QT_PERIODICO_ELETRONICO': 'QTDE_PERIODICOS_ELETRONICOS_IES',
                            'QT_LIVRO_ELETRONICO': 'QTDE_LIVROS_ELETRONICOS_IES',
                            'VL_DESPESA_PESQUISA': 'VALOR_DESPESA_PESQUISA_IES',
                            'QT_TEC_FUNDAMENTAL_INCOMP_FEM': 'QTDE_TECNICOS_FUNDAMENTAL_INCOMP_FEM_IES',
                            'QT_TEC_FUNDAMENTAL_INCOMP_MASC': 'QTDE_TECNICOS_FUNDAMENTAL_INCOMP_MASC_IES',
                            'QT_TEC_FUNDAMENTAL_COMP_FEM': 'QTDE_TECNICOS_FUNDAMENTAL_COMP_FEM_IES',
                            'QT_TEC_FUNDAMENTAL_COMP_MASC': 'QTDE_TECNICOS_FUNDAMENTAL_COMP_MASC_IES',
                            'QT_TEC_MEDIO_FEM': 'QTDE_TECNICOS_MEDIO_FEM_IES',
                            'QT_TEC_MEDIO_MASC': 'QTDE_TECNICOS_MEDIO_MASC_IES',
                            'QT_TEC_SUPERIOR_FEM': 'QTDE_TECNICOS_SUPERIOR_FEM_IES',
                            'QT_TEC_SUPERIOR_MASC': 'QTDE_TECNICOS_SUPERIOR_MASC_IES',
                            'QT_TEC_ESPECIALIZACAO_FEM': 'QTDE_TECNICOS_ESPECIALIZACAO_FEM_IES',
                            'QT_TEC_ESPECIALIZACAO_MASC': 'QTDE_TECNICOS_ESPECIALIZACAO_MASC_IES',
                            'QT_TEC_MESTRADO_FEM': 'QTDE_TECNICOS_MESTRADO_FEM_IES',
                            'QT_TEC_MESTRADO_MASC': 'QTDE_TECNICOS_MESTRADO_MASC_IES',
                            'QT_TEC_DOUTORADO_FEM': 'QTDE_TECNICOS_DOUTORADO_FEM_IES',
                            'QT_TEC_DOUTORADO_MASC': 'QTDE_TECNICOS_DOUTORADO_MASC_IES',
                            'QT_PERIODICO_ELETRONICO': 'QTDE_PERIODICOS_ELETRONICOS_IES',
                            'QT_LIVRO_ELETRONICO': 'QTDE_LIVROS_ELETRONICOS_IES',
                            'VL_RECEITA_PROPRIA': 'VALOR_RECEITA_PROPRIA_IES',
                            'VL_RECEITA_TRANSFERENCIA': 'VALOR_RECEITA_TRANSFERENCIA_IES',
                            'VL_RECEITA_OUTRA': 'VALOR_OUTRA_RECEITA_IES',
                            'VL_DESPESA_PESSOAL_DOCENTE': 'VALOR_DESPESA_PESSOAL_DOCENTE_IES',
                            'VL_DESPESA_PESSOAL_TECNICO': 'VALOR_DESPESA_PESSOAL_TECNICO_IES',
                            'VL_DESPESA_PESSOAL_ENCARGO': 'VALOR_DESPESA_PESSOAL_ENCARGO_IES',
                            'VL_DESPESA_CUSTEIO': 'VALOR_DESPESA_CUSTEIO_IES',
                            'VL_DESPESA_INVESTIMENTO': 'VALOR_DESPESA_INVESTIMENTO_IES',
                            'VL_DESPESA_PESQUISA': 'VALOR_DESPESA_PESQUISA_IES',
                            'VL_DESPESA_OUTRA': 'VALOR_OUTRA_DESPESA_IES',

                            'IN_ACESSO_PORTAL_CAPES': 'INDICADOR_ACESSO_PORTAL_CAPES_IES',
                            'IN_ASSINA_OUTRA_BASE': 'INDICADOR_ASSINA_OUTRA_BASE_IES',
                            'IN_REPOSITORIO_INSTITUCIONAL': 'INDICADOR_REPOSITORIO_INSTITUCIONAL_IES',
                            'IN_BUSCA_INTEGRADA': 'INDICADOR_BUSCA_INTEGRADA_IES',
                            'IN_SERVICO_INTERNET': 'INDICADOR_SERVICO_INTERNET_IES',
                            'IN_PARTICIPA_REDE_SOCIAL': 'INDICADOR_PARTICIPACAO_REDE_SOCIAL_IES',
                            'IN_CATALOGO_ONLINE': 'INDICADOR_CATALOGO_ONLINE_IES',
                            'TP_REFERENTE': 'ENTIDADE_REFERENTE_DADO_FINANCEIRO_IES'
                            
                            }, inplace=True)

df_ies = df_ies.append(df_ies_2017, ignore_index=True)

df_ies_2016.drop('IN_ACESSO_OUTRAS_BASES', axis=1, inplace=True)
df_ies_2016.drop('DS_CATEGORIA_ADMINISTRATIVA', axis=1, inplace=True)
df_ies_2016.drop('DS_ORGANIZACAO_ACADEMICA', axis=1, inplace=True)
df_ies_2016.drop('NO_MUNICIPIO_IES', axis=1, inplace=True)
df_ies_2016.drop('SGL_UF_IES', axis=1, inplace=True)

df_ies_2016['NO_REGIAO_IES'] = df_ies_2016['NO_REGIAO_IES'].replace(['Norte'],'1')
df_ies_2016['NO_REGIAO_IES'] = df_ies_2016['NO_REGIAO_IES'].replace(['Nordeste'],'2')
df_ies_2016['NO_REGIAO_IES'] = df_ies_2016['NO_REGIAO_IES'].replace(['Sudeste'],'3')
df_ies_2016['NO_REGIAO_IES'] = df_ies_2016['NO_REGIAO_IES'].replace(['Sul'],'4')
df_ies_2016['NO_REGIAO_IES'] = df_ies_2016['NO_REGIAO_IES'].replace(['Centro-Oeste'],'5')

df_ies_2016.insert(1, "ANO_CENSO_IES", ['2016']*len(df_ies_2016.index), True)

df_ies_2016.rename(columns={'CO_IES': 'CODIGO_IES',
                            'NO_IES': 'NOME_IES',
                            'SGL_IES': 'SIGLA_IES',
                            'CO_MANTENEDORA': 'CODIGO_MANTENEDORA_IES',
                            'NO_MANTENEDORA': 'NOME_MANTENEDORA_IES',
                            'CO_CATEGORIA_ADMINISTRATIVA': 'CATEGORIA_ADMINISTRATIVA_IES',
                            'CO_ORGANIZACAO_ACADEMICA': 'ORGANIZACAO_ACADEMICA_IES',
                            'NO_REGIAO_IES': 'CODIGO_REGIAO_IES',
                            'CO_UF_IES': 'CODIGO_UNIDADE_FEDERATIVA_IES',
                            'CO_MUNICIPIO_IES': 'CODIGO_MUNICIPIO_IES',
                            'IN_CAPITAL_IES': 'INDICADOR_CAPITAL_IES',
                            
                            'QT_TEC_TOTAL': 'QTDE_TOTAL_TECNICOS_IES',
                            'QT_TEC_FUNDAMENTAL_COMP_FEM': 'QTDE_TECNICOS_FUNDAMENTAL_COMP_FEM_IES',
                            'QT_TEC_FUNDAMENTAL_COMP_MASC': 'QTDE_TECNICOS_FUNDAMENTAL_COMP_MASC_IES',
                            'QT_PERIODICO_ELETRONICO': 'QTDE_PERIODICOS_ELETRONICOS_IES',
                            'QT_LIVRO_ELETRONICO': 'QTDE_LIVROS_ELETRONICOS_IES',
                            'VL_DESPESA_PESQUISA': 'VALOR_DESPESA_PESQUISA_IES',
                            'QT_TEC_FUND_INCOMP_FEM': 'QTDE_TECNICOS_FUNDAMENTAL_INCOMP_FEM_IES',
                            'QT_TEC_FUND_INCOMP_MASC': 'QTDE_TECNICOS_FUNDAMENTAL_INCOMP_MASC_IES',
                            'QT_TEC_FUND_COMP_FEM': 'QTDE_TECNICOS_FUNDAMENTAL_COMP_FEM_IES',
                            'QT_TEC_FUND_COMP_MASC': 'QTDE_TECNICOS_FUNDAMENTAL_COMP_MASC_IES',
                            'QT_TEC_MEDIO_FEM': 'QTDE_TECNICOS_MEDIO_FEM_IES',
                            'QT_TEC_MEDIO_MASC': 'QTDE_TECNICOS_MEDIO_MASC_IES',
                            'QT_TEC_SUPERIOR_FEM': 'QTDE_TECNICOS_SUPERIOR_FEM_IES',
                            'QT_TEC_SUPERIOR_MASC': 'QTDE_TECNICOS_SUPERIOR_MASC_IES',
                            'QT_TEC_ESPECIALIZACAO_FEM': 'QTDE_TECNICOS_ESPECIALIZACAO_FEM_IES',
                            'QT_TEC_ESPECIALIZACAO_MASC': 'QTDE_TECNICOS_ESPECIALIZACAO_MASC_IES',
                            'QT_TEC_MESTRADO_FEM': 'QTDE_TECNICOS_MESTRADO_FEM_IES',
                            'QT_TEC_MESTRADO_MASC': 'QTDE_TECNICOS_MESTRADO_MASC_IES',
                            'QT_TEC_DOUTORADO_FEM': 'QTDE_TECNICOS_DOUTORADO_FEM_IES',
                            'QT_TEC_DOUTORADO_MASC': 'QTDE_TECNICOS_DOUTORADO_MASC_IES',
                            'QT_PERIODICO_ELETRONICO': 'QTDE_PERIODICOS_ELETRONICOS_IES',
                            'QT_LIVRO_ELETRONICO': 'QTDE_LIVROS_ELETRONICOS_IES',
                            'VL_RECEITA_PROPRIA': 'VALOR_RECEITA_PROPRIA_IES',
                            'VL_TRANSFERENCIA': 'VALOR_RECEITA_TRANSFERENCIA_IES',
                            'VL_OUTRA_RECEITA': 'VALOR_OUTRA_RECEITA_IES',
                            'VL_DES_PESSOAL_REM_DOCENTE': 'VALOR_DESPESA_PESSOAL_DOCENTE_IES',
                            'VL_DES_PESSOAL_REM_TECNICO': 'VALOR_DESPESA_PESSOAL_TECNICO_IES',
                            'VL_DES_PESSOAL_ENCARGO': 'VALOR_DESPESA_PESSOAL_ENCARGO_IES',
                            'VL_DES_CUSTEIO': 'VALOR_DESPESA_CUSTEIO_IES',
                            'VL_DES_INVESTIMENTO': 'VALOR_DESPESA_INVESTIMENTO_IES',
                            'VL_DES_PESQUISA': 'VALOR_DESPESA_PESQUISA_IES',
                            'VL_DES_OUTRAS': 'VALOR_OUTRA_DESPESA_IES',

                            'IN_ACESSO_PORTAL_CAPES': 'INDICADOR_ACESSO_PORTAL_CAPES_IES',
                            'IN_ASSINA_OUTRA_BASE': 'INDICADOR_ASSINA_OUTRA_BASE_IES',
                            'IN_REPOSITORIO_INSTITUCIONAL': 'INDICADOR_REPOSITORIO_INSTITUCIONAL_IES',
                            'IN_BUSCA_INTEGRADA': 'INDICADOR_BUSCA_INTEGRADA_IES',
                            'IN_SERVICO_INTERNET': 'INDICADOR_SERVICO_INTERNET_IES',
                            'IN_PARTICIPA_REDE_SOCIAL': 'INDICADOR_PARTICIPACAO_REDE_SOCIAL_IES',
                            'IN_CATALOGO_ONLINE': 'INDICADOR_CATALOGO_ONLINE_IES',
                            'IN_REFERENTE': 'ENTIDADE_REFERENTE_DADO_FINANCEIRO_IES'
                            
                            }, inplace=True)

df_ies = df_ies.append(df_ies_2016, ignore_index=True)

df_ies = df_ies.drop_duplicates(subset=['CODIGO_IES'], ignore_index=True)
df_ies.reset_index(drop=True, inplace=True)

df_ies['SIGLA_IES'].fillna('SEM SIGLA', inplace=True)

df_ies.rename(columns={'INDICADOR_CAPITAL_IES':'LOCALIZACAO_CAPITAL_IES'}, inplace=True)
df_ies.rename(columns={'INDICADOR_ACESSO_PORTAL_CAPES_IES':'ACESSO_PORTAL_CAPES_IES'}, inplace=True)
df_ies.rename(columns={'INDICADOR_REPOSITORIO_INSTITUCIONAL_IES':'REPOSITORIO_INSTITUCIONAL_IES'}, inplace=True)
df_ies.rename(columns={'INDICADOR_BUSCA_INTEGRADA_IES':'BUSCA_INTEGRADA_IES'}, inplace=True)
df_ies.rename(columns={'INDICADOR_SERVICO_INTERNET_IES':'SERVICO_INTERNET_IES'}, inplace=True)
df_ies.rename(columns={'INDICADOR_PARTICIPACAO_REDE_SOCIAL_IES':'PARTICIPACAO_REDE_SOCIAL_IES'}, inplace=True)
df_ies.rename(columns={'INDICADOR_CATALOGO_ONLINE_IES':'CATALOGO_ONLINE_IES'}, inplace=True)
df_ies.rename(columns={'ENTIDADE_REFERENTE_DADO_FINANCEIRO_IES':'REFERENCIA_DADO_FINANCEIRO_IES'}, inplace=True)

df_ies.rename(columns={'VALOR_RECEITA_PROPRIA_IES':'RECEITA_PROPRIA_IES'}, inplace=True)
df_ies.rename(columns={'VALOR_RECEITA_TRANSFERENCIA_IES':'RECEITA_TRANSFERENCIA_IES'}, inplace=True)
df_ies.rename(columns={'VALOR_OUTRA_RECEITA_IES':'OUTRA_RECEITA_IES'}, inplace=True)
df_ies.rename(columns={'VALOR_DESPESA_PESSOAL_DOCENTE_IES':'DESPESA_PESSOAL_DOCENTE_IES'}, inplace=True)
df_ies.rename(columns={'VALOR_DESPESA_PESSOAL_TECNICO_IES':'DESPESA_PESSOAL_TECNICO_IES'}, inplace=True)
df_ies.rename(columns={'VALOR_DESPESA_PESSOAL_ENCARGO_IES':'DESPESA_PESSOAL_ENCARGO_IES'}, inplace=True)
df_ies.rename(columns={'VALOR_DESPESA_CUSTEIO_IES':'DESPESA_CUSTEIO_IES'}, inplace=True)
df_ies.rename(columns={'VALOR_DESPESA_INVESTIMENTO_IES':'DESPESA_INVESTIMENTO_IES'}, inplace=True)
df_ies.rename(columns={'VALOR_DESPESA_PESQUISA_IES':'DESPESA_PESQUISA_IES'}, inplace=True)
df_ies.rename(columns={'VALOR_OUTRA_DESPESA_IES':'OUTRA_DESPESA_IES'}, inplace=True)

df_ies = df_ies.astype({'QTDE_TECNICOS_FUNDAMENTAL_INCOMP_FEM_IES': 'int32'})
df_ies = df_ies.astype({'QTDE_TECNICOS_FUNDAMENTAL_INCOMP_MASC_IES': 'int32'})
df_ies = df_ies.astype({'QTDE_TECNICOS_FUNDAMENTAL_COMP_FEM_IES': 'int32'})
df_ies = df_ies.astype({'QTDE_TECNICOS_FUNDAMENTAL_COMP_MASC_IES': 'int32'})
df_ies = df_ies.astype({'QTDE_TECNICOS_MEDIO_FEM_IES': 'int32'})
df_ies = df_ies.astype({'QTDE_TECNICOS_MEDIO_MASC_IES': 'int32'})
df_ies = df_ies.astype({'QTDE_TECNICOS_SUPERIOR_FEM_IES': 'int32'})
df_ies = df_ies.astype({'QTDE_TECNICOS_SUPERIOR_MASC_IES': 'int32'})
df_ies = df_ies.astype({'QTDE_TECNICOS_ESPECIALIZACAO_FEM_IES': 'int32'})
df_ies = df_ies.astype({'QTDE_TECNICOS_ESPECIALIZACAO_MASC_IES': 'int32'})
df_ies = df_ies.astype({'QTDE_TECNICOS_MESTRADO_FEM_IES': 'int32'})
df_ies = df_ies.astype({'QTDE_TECNICOS_MESTRADO_MASC_IES': 'int32'})
df_ies = df_ies.astype({'QTDE_TECNICOS_DOUTORADO_FEM_IES': 'int32'})
df_ies = df_ies.astype({'QTDE_TECNICOS_DOUTORADO_MASC_IES': 'int32'})

df_ies['RECEITA_PROPRIA_IES'] = df_ies['RECEITA_PROPRIA_IES'].replace(['0'],'0.00')
df_ies['RECEITA_TRANSFERENCIA_IES'] = df_ies['RECEITA_TRANSFERENCIA_IES'].replace(['0'],'0.00')
df_ies['OUTRA_RECEITA_IES'] = df_ies['OUTRA_RECEITA_IES'].replace(['0'],'0.00')
df_ies['DESPESA_PESSOAL_DOCENTE_IES'] = df_ies['DESPESA_PESSOAL_DOCENTE_IES'].replace(['0'],'0.00')
df_ies['DESPESA_PESSOAL_TECNICO_IES'] = df_ies['DESPESA_PESSOAL_TECNICO_IES'].replace(['0'],'0.00')
df_ies['DESPESA_PESSOAL_ENCARGO_IES'] = df_ies['DESPESA_PESSOAL_ENCARGO_IES'].replace(['0'],'0.00')
df_ies['DESPESA_CUSTEIO_IES'] = df_ies['DESPESA_CUSTEIO_IES'].replace(['0'],'0.00')
df_ies['DESPESA_INVESTIMENTO_IES'] = df_ies['DESPESA_INVESTIMENTO_IES'].replace(['0'],'0.00')
df_ies['DESPESA_PESQUISA_IES'] = df_ies['DESPESA_PESQUISA_IES'].replace(['0'],'0.00')
df_ies['OUTRA_DESPESA_IES'] = df_ies['OUTRA_DESPESA_IES'].replace(['0'],'0.00')

qtde_tecnicos_fundamental = df_ies['QTDE_TECNICOS_FUNDAMENTAL_INCOMP_FEM_IES'] + df_ies['QTDE_TECNICOS_FUNDAMENTAL_INCOMP_MASC_IES'] + df_ies['QTDE_TECNICOS_FUNDAMENTAL_COMP_FEM_IES'] + df_ies['QTDE_TECNICOS_FUNDAMENTAL_COMP_MASC_IES']
qtde_tecnicos_medio = df_ies['QTDE_TECNICOS_MEDIO_FEM_IES'] + df_ies['QTDE_TECNICOS_MEDIO_MASC_IES']
qtde_tecnicos_superior = df_ies['QTDE_TECNICOS_SUPERIOR_FEM_IES'] + df_ies['QTDE_TECNICOS_SUPERIOR_MASC_IES']
qtde_tecnicos_pos = df_ies['QTDE_TECNICOS_ESPECIALIZACAO_FEM_IES'] + df_ies['QTDE_TECNICOS_ESPECIALIZACAO_MASC_IES'] + df_ies['QTDE_TECNICOS_MESTRADO_FEM_IES'] + df_ies['QTDE_TECNICOS_MESTRADO_MASC_IES'] + df_ies['QTDE_TECNICOS_DOUTORADO_FEM_IES'] + df_ies['QTDE_TECNICOS_DOUTORADO_MASC_IES']

# qtde_tecnicos_fundamental_fem = df_ies['QTDE_TECNICOS_FUNDAMENTAL_INCOMP_FEM_IES'] + df_ies['QTDE_TECNICOS_FUNDAMENTAL_COMP_FEM_IES']
# qtde_tecnicos_fundamental_masc = df_ies['QTDE_TECNICOS_FUNDAMENTAL_INCOMP_MASC_IES'] + df_ies['QTDE_TECNICOS_FUNDAMENTAL_COMP_MASC_IES']
# qtde_tecnicos_pos_fem = df_ies['QTDE_TECNICOS_ESPECIALIZACAO_FEM_IES'] + df_ies['QTDE_TECNICOS_MESTRADO_FEM_IES'] + df_ies['QTDE_TECNICOS_DOUTORADO_FEM_IES']
# qtde_tecnicos_pos_masc = df_ies['QTDE_TECNICOS_ESPECIALIZACAO_MASC_IES'] + df_ies['QTDE_TECNICOS_MESTRADO_MASC_IES'] + df_ies['QTDE_TECNICOS_DOUTORADO_MASC_IES']

df_igc.rename(columns={'ANO':'ANO_IGC'}, inplace=True)

df_ies.insert(12,'QTDE_TECNICOS_FUNDAMENTAL_IES',list(qtde_tecnicos_fundamental),True)
df_ies.insert(13,'QTDE_TECNICOS_MEDIO_IES',list(qtde_tecnicos_medio),True)
df_ies.insert(14,'QTDE_TECNICOS_SUPERIOR_IES',list(qtde_tecnicos_superior),True)
df_ies.insert(15,'QTDE_TECNICOS_POS_IES',list(qtde_tecnicos_pos),True)

# df_ies.insert(12,'QTDE_TECNICOS_FUNDAMENTAL_FEM_IES',list(qtde_tecnicos_fundamental_fem),True)
# df_ies.insert(12,'QTDE_TECNICOS_FUNDAMENTAL_MASC_IES',list(qtde_tecnicos_fundamental_masc),True)
# df_ies.insert(15,'QTDE_TECNICOS_POS_FEM_IES',list(qtde_tecnicos_pos_fem),True)
# df_ies.insert(15,'QTDE_TECNICOS_POS_MASC_IES',list(qtde_tecnicos_pos_masc),True)

df_ies.drop('QTDE_TECNICOS_FUNDAMENTAL_INCOMP_FEM_IES', axis=1, inplace=True)
df_ies.drop('QTDE_TECNICOS_FUNDAMENTAL_INCOMP_MASC_IES', axis=1, inplace=True)
df_ies.drop('QTDE_TECNICOS_FUNDAMENTAL_COMP_FEM_IES', axis=1, inplace=True)
df_ies.drop('QTDE_TECNICOS_FUNDAMENTAL_COMP_MASC_IES', axis=1, inplace=True)
df_ies.drop('QTDE_TECNICOS_MEDIO_FEM_IES', axis=1, inplace=True)
df_ies.drop('QTDE_TECNICOS_MEDIO_MASC_IES', axis=1, inplace=True)
df_ies.drop('QTDE_TECNICOS_SUPERIOR_FEM_IES', axis=1, inplace=True)
df_ies.drop('QTDE_TECNICOS_SUPERIOR_MASC_IES', axis=1, inplace=True)
df_ies.drop('QTDE_TECNICOS_ESPECIALIZACAO_FEM_IES', axis=1, inplace=True)
df_ies.drop('QTDE_TECNICOS_ESPECIALIZACAO_MASC_IES', axis=1, inplace=True)
df_ies.drop('QTDE_TECNICOS_MESTRADO_FEM_IES', axis=1, inplace=True)
df_ies.drop('QTDE_TECNICOS_MESTRADO_MASC_IES', axis=1, inplace=True)
df_ies.drop('QTDE_TECNICOS_DOUTORADO_FEM_IES', axis=1, inplace=True)
df_ies.drop('QTDE_TECNICOS_DOUTORADO_MASC_IES', axis=1, inplace=True)

# print(list(qtde_tecnicos_fundamental))
# print(len(list(qtde_tecnicos_fundamental)))

print(len(list(df_ies.index)))

ies_enade = pd.read_csv("ies_associadas_enade.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")
ies_enade = list(ies_enade['CODIGO_IES'])
count = 0
df_ies_final = None

print(len(ies_enade))

for i in ies_enade:
    df = df_ies[df_ies['CODIGO_IES']==str(i)]
    # print(df)
    if count == 0:
        df_ies_final = df
        # print('é')
    else:
        # print('é não')
        df_ies_final = df_ies_final.append(df, ignore_index=True)
    count+=1
    # print('adicionado')

# df_ies_final.to_csv('ies_final.csv', index=False, encoding= "ISO-8859-1")

print(len(list(df_ies_final.index)))

a = list(df_ies_final['CODIGO_IES'])

for i in ies_enade:
    if i not in a:
        print(i)

# profile = pr(df_ies_final, title='IES final', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("ies_final.html")

print("Começando join")
df_final = df_ies_final.join(df_igc.set_index('CODIGO_IES'), on='CODIGO_IES')
print("Finalizando join")

df_final = df_final[['ANO_CENSO_IES','CODIGO_IES','ANO_IGC','IGC_FAIXA','NOME_IES','SIGLA_IES','CODIGO_MANTENEDORA_IES','NOME_MANTENEDORA_IES','CATEGORIA_ADMINISTRATIVA_IES','ORGANIZACAO_ACADEMICA_IES','CODIGO_REGIAO_IES','CODIGO_UNIDADE_FEDERATIVA_IES','CODIGO_MUNICIPIO_IES','LOCALIZACAO_CAPITAL_IES','QTDE_TOTAL_TECNICOS_IES','QTDE_TECNICOS_FUNDAMENTAL_IES','QTDE_TECNICOS_MEDIO_IES','QTDE_TECNICOS_SUPERIOR_IES','QTDE_TECNICOS_POS_IES','ACESSO_PORTAL_CAPES_IES','REPOSITORIO_INSTITUCIONAL_IES','BUSCA_INTEGRADA_IES','SERVICO_INTERNET_IES','PARTICIPACAO_REDE_SOCIAL_IES','CATALOGO_ONLINE_IES','QTDE_PERIODICOS_ELETRONICOS_IES','QTDE_LIVROS_ELETRONICOS_IES','REFERENCIA_DADO_FINANCEIRO_IES','RECEITA_PROPRIA_IES','RECEITA_TRANSFERENCIA_IES','OUTRA_RECEITA_IES','DESPESA_PESSOAL_DOCENTE_IES','DESPESA_PESSOAL_TECNICO_IES','DESPESA_PESSOAL_ENCARGO_IES','DESPESA_CUSTEIO_IES','DESPESA_INVESTIMENTO_IES','DESPESA_PESQUISA_IES','OUTRA_DESPESA_IES']]
# df_final = df_final[['ANO_CENSO_IES','CODIGO_IES','ANO_IGC','IGC_FAIXA','NOME_IES','SIGLA_IES','CODIGO_MANTENEDORA_IES','NOME_MANTENEDORA_IES','CATEGORIA_ADMINISTRATIVA_IES','ORGANIZACAO_ACADEMICA_IES','CODIGO_REGIAO_IES','CODIGO_UNIDADE_FEDERATIVA_IES','CODIGO_MUNICIPIO_IES','LOCALIZACAO_CAPITAL_IES','QTDE_TOTAL_TECNICOS_IES','QTDE_TECNICOS_FUNDAMENTAL_FEM_IES','QTDE_TECNICOS_FUNDAMENTAL_MASC_IES','QTDE_TECNICOS_MEDIO_FEM_IES','QTDE_TECNICOS_MEDIO_MASC_IES','QTDE_TECNICOS_SUPERIOR_FEM_IES','QTDE_TECNICOS_SUPERIOR_MASC_IES','QTDE_TECNICOS_POS_FEM_IES','QTDE_TECNICOS_POS_MASC_IES','ACESSO_PORTAL_CAPES_IES','REPOSITORIO_INSTITUCIONAL_IES','BUSCA_INTEGRADA_IES','SERVICO_INTERNET_IES','PARTICIPACAO_REDE_SOCIAL_IES','CATALOGO_ONLINE_IES','QTDE_PERIODICOS_ELETRONICOS_IES','QTDE_LIVROS_ELETRONICOS_IES','REFERENCIA_DADO_FINANCEIRO_IES','RECEITA_PROPRIA_IES','RECEITA_TRANSFERENCIA_IES','OUTRA_RECEITA_IES','DESPESA_PESSOAL_DOCENTE_IES','DESPESA_PESSOAL_TECNICO_IES','DESPESA_PESSOAL_ENCARGO_IES','DESPESA_CUSTEIO_IES','DESPESA_INVESTIMENTO_IES','DESPESA_PESQUISA_IES','OUTRA_DESPESA_IES']]

df_final.to_csv('ies_final.csv',index=False,encoding="utf-8")
# df_final.to_csv('ies_final.csv',index=False,encoding="utf-8")

# #!!!!!! É PRECISO ADICIONAR A IES 4899 AO ARQUIVO ANTES DE GERAR PROFILE !!!!!!
# 2015,4899,2018,SC,FACULDADE DE CIÊNCIAS MÉDICAS DA BAHIA,CIENCIAS MEDICAS,3125,CENTRO EDUCACIONAL DO SUL DA BAHIA LTDA - ME,4,3,2,29,2927705,0,6,1,2,2,1,0,0,0,1,1,1,0,0,2,485042.00,0.00,15264.20,265420.00,112580.00,56325.11,18632.32,14125.00,17560.00,52005.44
# 2015,4899,2018,SC,FACULDADE DE CIÊNCIAS MÉDICAS DA BAHIA,CIENCIAS MEDICAS,3125,CENTRO EDUCACIONAL DO SUL DA BAHIA LTDA - ME,4,3,2,29,2927705,0,6,1,0,2,0,1,1,1,0,0,0,0,1,1,1,0,0,2,485042.00,0.00,15264.20,265420.00,112580.00,56325.11,18632.32,14125.00,17560.00,52005.44

# df_final = pd.read_csv("ies_final.csv", sep=",", encoding = "ISO-8859-1", dtype="unicode")

# profile = pr(df_final, title='IES + IGC', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("ies_final.html")