import pandas as pd
from pandas_profiling import ProfileReport as pr

df_ies_2018 = pd.read_csv("educacao_superior/2018/dados/dm_ies.csv", sep="|", encoding = "ISO-8859-1", dtype="unicode")
df_ies_2017 = pd.read_csv("educacao_superior/2017/dados/dm_ies.csv", sep="|", encoding = "ISO-8859-1", dtype="unicode")
df_ies_2016 = pd.read_csv("educacao_superior/2016/dados/dm_ies.csv", sep="|", encoding = "ISO-8859-1", dtype="unicode")
df_ies_2015 = pd.read_csv("educacao_superior/2015/dados/dm_ies.csv", sep="|", encoding = "ISO-8859-1", dtype="unicode")
df_ies_2014 = pd.read_csv("educacao_superior/2014/dados/dm_ies.csv", sep="|", encoding = "ISO-8859-1", dtype="unicode")
df_ies_2013 = pd.read_csv("educacao_superior/2013/dados/dm_ies.csv", sep="|", encoding = "ISO-8859-1", dtype="unicode")

# profile = pr(df_ies_2018, title='Censo Escolar da Educação Superior: IES', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("profiling_censo_educacao_superior_ies_2018.html")

# profile = pr(df_ies_2017, title='Censo Escolar da Educação Superior: IES', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("profiling_censo_educacao_superior_ies_2017.html")

# profile = pr(df_ies_2016, title='Censo Escolar da Educação Superior: IES', minimal=True, html={'style':{'full_width':True}})
# profile.to_file("profiling_censo_educacao_superior_ies_2016.html")

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

df_ies.to_csv('censo_superior_ies.csv', index=False)

profile = pr(df_ies, title='Censo Escolar da Educação Superior: IES', minimal=True, html={'style':{'full_width':True}})
profile.to_file("profiling_censo_educacao_superior_ies.html")
