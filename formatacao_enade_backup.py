import pandas as pd
from pandas_profiling import ProfileReport as pr

df_enade_2018 = pd.read_csv("enade/2018/3.dados/microdados_enade_2018.csv", sep=";", encoding = "ISO-8859-1", dtype='unicode')
df_enade_2017 = pd.read_csv("enade/2017/3.dados/microdados_enade_2017.csv", sep=";", encoding = "ISO-8859-1", dtype='unicode')
df_enade_2016 = pd.read_csv("enade/2016/3.dados/microdados_enade_2016.csv", sep=";", encoding = "ISO-8859-1", dtype='unicode')
# df_enade_2016 = pd.read_csv("enade/2016/3.dados/microdados_enade_2016_formatados.csv", sep=",", encoding = "ISO-8859-1", dtype='unicode')

# dropando variáveis que não serão usadas

df_enade_2018.drop('CO_CATEGAD', axis=1, inplace=True)
df_enade_2018.drop('CO_ORGACAD', axis=1, inplace=True)

# df_enade_2018.drop('CO_GRUPO', axis=1, inplace=True)
df_enade_2018.drop('NU_ITEM_OFG', axis=1, inplace=True)
df_enade_2018.drop('NU_ITEM_OFG_Z', axis=1, inplace=True)
df_enade_2018.drop('NU_ITEM_OFG_X', axis=1, inplace=True)
df_enade_2018.drop('NU_ITEM_OFG_N', axis=1, inplace=True)
df_enade_2018.drop('NU_ITEM_OCE', axis=1, inplace=True)
df_enade_2018.drop('NU_ITEM_OCE_Z', axis=1, inplace=True)
df_enade_2018.drop('NU_ITEM_OCE_X', axis=1, inplace=True)
df_enade_2018.drop('NU_ITEM_OCE_N', axis=1, inplace=True)
df_enade_2018.drop('DS_VT_GAB_OFG_ORIG', axis=1, inplace=True)
df_enade_2018.drop('DS_VT_GAB_OFG_FIN', axis=1, inplace=True)
df_enade_2018.drop('DS_VT_GAB_OCE_ORIG', axis=1, inplace=True)
df_enade_2018.drop('DS_VT_GAB_OCE_FIN', axis=1, inplace=True)
df_enade_2018.drop('DS_VT_ESC_OFG', axis=1, inplace=True)
df_enade_2018.drop('DS_VT_ACE_OFG', axis=1, inplace=True)
df_enade_2018.drop('DS_VT_ESC_OCE', axis=1, inplace=True)
df_enade_2018.drop('DS_VT_ACE_OCE', axis=1, inplace=True)

# df_enade_2018.drop('TP_PRES', axis=1, inplace=True)
df_enade_2018.drop('TP_PR_GER', axis=1, inplace=True)
df_enade_2018.drop('TP_PR_OB_FG', axis=1, inplace=True)
df_enade_2018.drop('TP_PR_DI_FG', axis=1, inplace=True)
df_enade_2018.drop('TP_PR_OB_CE', axis=1, inplace=True)
df_enade_2018.drop('TP_PR_DI_CE', axis=1, inplace=True)
df_enade_2018.drop('TP_SFG_D1', axis=1, inplace=True)
df_enade_2018.drop('TP_SFG_D2', axis=1, inplace=True)
df_enade_2018.drop('TP_SCE_D1', axis=1, inplace=True)
df_enade_2018.drop('TP_SCE_D2', axis=1, inplace=True)
df_enade_2018.drop('TP_SCE_D3', axis=1, inplace=True)

# df_enade_2018.drop('NT_GER', axis=1, inplace=True)
df_enade_2018.drop('NT_FG', axis=1, inplace=True)
df_enade_2018.drop('NT_OBJ_FG', axis=1, inplace=True)
df_enade_2018.drop('NT_DIS_FG', axis=1, inplace=True)
df_enade_2018.drop('NT_FG_D1', axis=1, inplace=True)
df_enade_2018.drop('NT_FG_D1_PT', axis=1, inplace=True)
df_enade_2018.drop('NT_FG_D1_CT', axis=1, inplace=True)
df_enade_2018.drop('NT_FG_D2', axis=1, inplace=True)
df_enade_2018.drop('NT_FG_D2_PT', axis=1, inplace=True)
df_enade_2018.drop('NT_FG_D2_CT', axis=1, inplace=True)
df_enade_2018.drop('NT_CE', axis=1, inplace=True)
df_enade_2018.drop('NT_OBJ_CE', axis=1, inplace=True)
df_enade_2018.drop('NT_DIS_CE', axis=1, inplace=True)
df_enade_2018.drop('NT_CE_D1', axis=1, inplace=True)
df_enade_2018.drop('NT_CE_D2', axis=1, inplace=True)
df_enade_2018.drop('NT_CE_D3', axis=1, inplace=True)

df_enade_2018.drop('CO_RS_I1', axis=1, inplace=True)
df_enade_2018.drop('CO_RS_I2', axis=1, inplace=True)
df_enade_2018.drop('CO_RS_I3', axis=1, inplace=True)
df_enade_2018.drop('CO_RS_I4', axis=1, inplace=True)
df_enade_2018.drop('CO_RS_I5', axis=1, inplace=True)
df_enade_2018.drop('CO_RS_I6', axis=1, inplace=True)
df_enade_2018.drop('CO_RS_I7', axis=1, inplace=True)
df_enade_2018.drop('CO_RS_I8', axis=1, inplace=True)
df_enade_2018.drop('CO_RS_I9', axis=1, inplace=True)
df_enade_2018.drop('TP_INSCRICAO_ADM', axis=1, inplace=True)
df_enade_2018.drop('TP_INSCRICAO', axis=1, inplace=True)

df_enade_2018.drop('QE_I07', axis=1, inplace=True)
df_enade_2018.drop('QE_I14', axis=1, inplace=True)
df_enade_2018.drop('QE_I26', axis=1, inplace=True)
df_enade_2018.drop('QE_I30', axis=1, inplace=True)
df_enade_2018.drop('QE_I31', axis=1, inplace=True)
df_enade_2018.drop('QE_I32', axis=1, inplace=True)
df_enade_2018.drop('QE_I33', axis=1, inplace=True)
df_enade_2018.drop('QE_I42', axis=1, inplace=True)
df_enade_2018.drop('QE_I46', axis=1, inplace=True)
df_enade_2018.drop('QE_I47', axis=1, inplace=True)
df_enade_2018.drop('QE_I48', axis=1, inplace=True)
df_enade_2018.drop('QE_I52', axis=1, inplace=True)
df_enade_2018.drop('QE_I53', axis=1, inplace=True)
df_enade_2018.drop('QE_I55', axis=1, inplace=True)
df_enade_2018.drop('QE_I66', axis=1, inplace=True)

# df_enade_2018.drop('QE_I26', axis=1, inplace=True)
# df_enade_2018.drop('QE_I27', axis=1, inplace=True)
# df_enade_2018.drop('QE_I28', axis=1, inplace=True)
# df_enade_2018.drop('QE_I29', axis=1, inplace=True)
# df_enade_2018.drop('QE_I30', axis=1, inplace=True)
# df_enade_2018.drop('QE_I31', axis=1, inplace=True)
# df_enade_2018.drop('QE_I32', axis=1, inplace=True)
# df_enade_2018.drop('QE_I33', axis=1, inplace=True)
# df_enade_2018.drop('QE_I34', axis=1, inplace=True)
# df_enade_2018.drop('QE_I35', axis=1, inplace=True)
# df_enade_2018.drop('QE_I36', axis=1, inplace=True)
# df_enade_2018.drop('QE_I37', axis=1, inplace=True)
df_enade_2018.drop('QE_I38', axis=1, inplace=True)
df_enade_2018.drop('QE_I39', axis=1, inplace=True)
# df_enade_2018.drop('QE_I40', axis=1, inplace=True)
# df_enade_2018.drop('QE_I41', axis=1, inplace=True)
# df_enade_2018.drop('QE_I43', axis=1, inplace=True)
# df_enade_2018.drop('QE_I44', axis=1, inplace=True)
# df_enade_2018.drop('QE_I45', axis=1, inplace=True)
# df_enade_2018.drop('QE_I46', axis=1, inplace=True)
# df_enade_2018.drop('QE_I47', axis=1, inplace=True)
# df_enade_2018.drop('QE_I48', axis=1, inplace=True)
df_enade_2018.drop('QE_I49', axis=1, inplace=True)
# df_enade_2018.drop('QE_I50', axis=1, inplace=True)
# df_enade_2018.drop('QE_I51', axis=1, inplace=True)
# df_enade_2018.drop('QE_I52', axis=1, inplace=True)
# df_enade_2018.drop('QE_I53', axis=1, inplace=True)
# df_enade_2018.drop('QE_I54', axis=1, inplace=True)
# df_enade_2018.drop('QE_I55', axis=1, inplace=True)
# df_enade_2018.drop('QE_I56', axis=1, inplace=True)
# df_enade_2018.drop('QE_I57', axis=1, inplace=True)
# df_enade_2018.drop('QE_I58', axis=1, inplace=True)
# df_enade_2018.drop('QE_I59', axis=1, inplace=True)
# df_enade_2018.drop('QE_I60', axis=1, inplace=True)
# df_enade_2018.drop('QE_I62', axis=1, inplace=True)
# df_enade_2018.drop('QE_I63', axis=1, inplace=True)
# df_enade_2018.drop('QE_I64', axis=1, inplace=True)
# df_enade_2018.drop('QE_I65', axis=1, inplace=True)
# df_enade_2018.drop('QE_I66', axis=1, inplace=True)
# df_enade_2018.drop('QE_I67', axis=1, inplace=True)
# df_enade_2018.drop('CO_TURNO_GRADUACAO', axis=1, inplace=True)

# renomeando variáveis

df_enade_2018.rename(columns={'NU_ANO': 'ANO_ENADE',
                            'CO_IES': 'CODIGO_IES',
                            'CO_CATEGAD': 'CATEGORIA_ADM_IES',
                            'CO_ORGACAD': 'ORGANIZACAO_ACAD_IES',
                            'CO_GRUPO': 'AREA_CURSO',
                            'CO_CURSO': 'CODIGO_CURSO',
                            'CO_MODALIDADE': 'MODALIDADE_CURSO',
                            'CO_MUNIC_CURSO': 'MUNICIPIO_CURSO',
                            'CO_UF_CURSO': 'UF_CURSO',
                            'CO_REGIAO_CURSO': 'REGIAO_CURSO',
                            'NU_IDADE': 'IDADE',
                            'TP_SEXO': 'SEXO',
                            'ANO_FIM_EM': 'ANO_FIM_ENS_MEDIO',
                            'ANO_IN_GRAD': 'ANO_INICIO_GRADUACAO',
                            'CO_TURNO_GRADUACAO': 'TURNO_GRADUACAO',
                            'TP_PRES': 'PRESENCA_ENADE',
                            'NT_GER': 'NOTA_BRUTA_ENADE',
                            # 'NT_FG': 'NOTA_BRUTA_FORMACAO_GERAL_ENADE',
                            # 'NT_OBJ_FG': 'NOTA_BRUTA_FORMACAO_GERAL_OBJETIVA_ENADE',
                            # 'NT_DIS_FG': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_ENADE',
                            # 'NT_FG_D1': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_1_ENADE',
                            # 'NT_FG_D1_PT': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_1_PORTUGUES_ENADE',
                            # 'NT_FG_D1_CT': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_1_CONTEUDO_ENADE',
                            # 'NT_FG_D2': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_2_ENADE',
                            # 'NT_FG_D2_PT': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_2_PORTUGUES_ENADE',
                            # 'NT_FG_D2_CT': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_2_CONTEUDO_ENADE',
                            # 'NT_CE': 'NOTA_BRUTA_ESPECIFICA_ENADE',
                            # 'NT_OBJ_CE': 'NOTA_BRUTA_ESPECIFICA_OBJETIVA_ENADE',
                            # 'NT_DIS_CE': 'NOTA_BRUTA_ESPECIFICA_DISCURSIVA_ENADE',
                            # 'NT_CE_D1': 'NOTA_BRUTA_ESPECIFICA_DISCURSIVA_1_ENADE',
                            # 'NT_CE_D2': 'NOTA_BRUTA_ESPECIFICA_DISCURSIVA_2_ENADE',
                            # 'NT_CE_D3': 'NOTA_BRUTA_ESPECIFICA_DISCURSIVA_3_ENADE',
                            'QE_I01': 'ESTADO_CIVIL',
                            'QE_I02': 'COR_RACA',
                            'QE_I03': 'NACIONALIDADE',
                            'QE_I04': 'ESCOLARIDADE_PAI',
                            'QE_I05': 'ESCOLARIDADE_MAE',
                            'QE_I06': 'COMPANHIA_RESIDENCIA',
                            # 'QE_I07': 'QUANTIDADE_COMPANHIA_RESIDENCIA',
                            'QE_I08': 'RENDA_FAMILIAR',
                            'QE_I09': 'SITUACAO_FINANCEIRA',
                            'QE_I10': 'SITUACAO_TRABALHO',
                            'QE_I11': 'BOLSA_ESTUDOS',
                            'QE_I12': 'AUXILIO_PERMANENCIA',
                            'QE_I13': 'BOLSA_ACADEMICA',
                            # 'QE_I14': 'INDICADOR_PARTICIPACAO_ATIVIDADES_EXTERIOR',
                            'QE_I15': 'ACAO_AFIRMATIVA',
                            'QE_I16': 'UF_ESCOLA_ENS_MEDIO',
                            'QE_I17': 'CATEGORIA_ADM_ESCOLA_ENS_MEDIO',
                            'QE_I18': 'MODALIDADE_ENS_MEDIO',
                            'QE_I19': 'INCENTIVO_GRADUACAO',
                            'QE_I20': 'OFERTA_APOIO_GERAL',
                            'QE_I21': 'GRADUACAO_FAMILIA',
                            'QE_I22': 'LEITURA_ANUAL',
                            'QE_I23': 'DEDICACAO_SEMANAL',
                            'QE_I24': 'OFERTA_IDIOMA_IES',
                            'QE_I25': 'MOTIVO_GRADUACAO',
                            # 'QE_I26': 'MOTIVO_ESCOLHA_IES',
                            'QE_I27': 'FORMACAO_INTEGRAL',
                            'QE_I28': 'ATUACAO_PROFISSIONAL',
                            'QE_I29': 'CAPACIDADE_CRITICA',
                            # 'QE_I30': 'INDICADOR_APRENDIZAGEM_INOVADORA_CURSO',
                            # 'QE_I31': 'INDICADOR_DESENVOLVIMENTO_CONSCIENCIA_ETICA',
                            # 'QE_I32': 'INDICADOR_OPORTUNIDADE_EQUIPE_CURSO',
                            # 'QE_I33': 'CAPACIDADE_REFLEXAO',
                            'QE_I34': 'CAPACIDADE_ANALISE',
                            'QE_I35': 'CAPACIDADE_COMUNICACAO',
                            'QE_I36': 'CAPACIDADE_APRENDIZADO',
                            'QE_I37': 'RELACAO_PROFESSOR_ALUNO',
                            # 'QE_I38': 'PLANOS_ENSINO_PROFESSORES',
                            # 'QE_I39': 'REFERENCIAS_PROFESSORES',
                            'QE_I40': 'OFERTA_APOIO_IES',
                            'QE_I41': 'ACESSO_COORDENACAO_CURSO',
                            # 'QE_I42': 'DEDICACAO',
                            'QE_I43': 'ATIVIDADES_EXTENSAO_IES',
                            'QE_I44': 'ATIVIDADES_PESQUISA_IES',
                            'QE_I45': 'OFERTA_EVENTOS_IES',
                            # 'QE_I46': 'INDICADOR_OFERTA_OPORTUNIDADES_ATUACAO_COLEGIADOS_IES',
                            # 'QE_I47': 'INDICADOR_FAVORECIMENTO_TEORIA_ATIVIDADES_PRATICAS_CURSO',
                            # 'QE_I48': 'INDICADOR_SUFICIENCIA_ATIVIDADES_PRATICAS_CURSO',
                            # 'QE_I49': 'CONTEUDO_ATUALIZADO_CURSO',
                            'QE_I50': 'CONTRIBUICAO_ESTAGIO',
                            'QE_I51': 'CONTRIBUICAO_TCC',
                            # 'QE_I52': 'INDICADOR_OFERTA_INTERCAMBIOS_BRASIL_IES',
                            # 'QE_I53': 'INDICADOR_OFERTA_INTERCAMBIOS_EXTERIOR_IES',
                            'QE_I54': 'AVALIACOES_PERIODICAS_CURSO',
                            # 'QE_I55': 'INDICADOR_COMPATIBILIDADE_AVALIACOES_CONTEUDOS_PROFESSORES',
                            'QE_I56': 'SUPORTE_EXTERNO_PROFESSORES',
                            'QE_I57': 'DOMINIO_CONTEUDO_PROFESSORES',
                            'QE_I58': 'EMPREGO_TICS_PROFESSORES',
                            'QE_I59': 'PESSOAL_APOIO_IES',
                            'QE_I60': 'MONITORES_IES',
                            'QE_I61': 'INFRAESTRUTURA_SALAS_AULA_IES',
                            'QE_I62': 'RECURSOS_AULAS_PRATICAS_IES',
                            'QE_I63': 'AMBIENTES_AULAS_PRATICAS_IES',
                            'QE_I64': 'BIBLIOTECA_FISICA_IES',
                            'QE_I65': 'BIBLIOTECA_VIRTUAL_IES',
                            # 'QE_I66': 'INDICADOR_CONTRIBUICAO_ATIVIDADES_REFLEXAO',
                            'QE_I67': 'OFERTA_LAZER_IES',
                            'QE_I68': 'INFRAESTRUTURA_GERAL_IES',
                            }, inplace=True)

df_enade_2018['MODALIDADE_CURSO'] = df_enade_2018['MODALIDADE_CURSO'].replace([2],0)
df_enade = df_enade_2018

# dropando variáveis que não serão usadas

df_enade_2017.drop('CO_CATEGAD', axis=1, inplace=True)
df_enade_2017.drop('CO_ORGACAD', axis=1, inplace=True)

# df_enade_2017.drop('CO_GRUPO', axis=1, inplace=True)
df_enade_2017.drop('NU_ITEM_OFG', axis=1, inplace=True)
df_enade_2017.drop('NU_ITEM_OFG_Z', axis=1, inplace=True)
df_enade_2017.drop('NU_ITEM_OFG_X', axis=1, inplace=True)
df_enade_2017.drop('NU_ITEM_OFG_N', axis=1, inplace=True)
df_enade_2017.drop('NU_ITEM_OCE', axis=1, inplace=True)
df_enade_2017.drop('NU_ITEM_OCE_Z', axis=1, inplace=True)
df_enade_2017.drop('NU_ITEM_OCE_X', axis=1, inplace=True)
df_enade_2017.drop('NU_ITEM_OCE_N', axis=1, inplace=True)
df_enade_2017.drop('DS_VT_GAB_OFG_ORIG', axis=1, inplace=True)
df_enade_2017.drop('DS_VT_GAB_OFG_FIN', axis=1, inplace=True)
df_enade_2017.drop('DS_VT_GAB_OCE_ORIG', axis=1, inplace=True)
df_enade_2017.drop('DS_VT_GAB_OCE_FIN', axis=1, inplace=True)
df_enade_2017.drop('DS_VT_ESC_OFG', axis=1, inplace=True)
df_enade_2017.drop('DS_VT_ACE_OFG', axis=1, inplace=True)
df_enade_2017.drop('DS_VT_ESC_OCE', axis=1, inplace=True)
df_enade_2017.drop('DS_VT_ACE_OCE', axis=1, inplace=True)

# df_enade_2017.drop('TP_PRES', axis=1, inplace=True)
df_enade_2017.drop('TP_PR_GER', axis=1, inplace=True)
df_enade_2017.drop('TP_PR_OB_FG', axis=1, inplace=True)
df_enade_2017.drop('TP_PR_DI_FG', axis=1, inplace=True)
df_enade_2017.drop('TP_PR_OB_CE', axis=1, inplace=True)
df_enade_2017.drop('TP_PR_DI_CE', axis=1, inplace=True)
df_enade_2017.drop('TP_SFG_D1', axis=1, inplace=True)
df_enade_2017.drop('TP_SFG_D2', axis=1, inplace=True)
df_enade_2017.drop('TP_SCE_D1', axis=1, inplace=True)
df_enade_2017.drop('TP_SCE_D2', axis=1, inplace=True)
df_enade_2017.drop('TP_SCE_D3', axis=1, inplace=True)

# df_enade_2017.drop('NT_GER', axis=1, inplace=True)
df_enade_2017.drop('NT_FG', axis=1, inplace=True)
df_enade_2017.drop('NT_OBJ_FG', axis=1, inplace=True)
df_enade_2017.drop('NT_DIS_FG', axis=1, inplace=True)
df_enade_2017.drop('NT_FG_D1', axis=1, inplace=True)
df_enade_2017.drop('NT_FG_D1_PT', axis=1, inplace=True)
df_enade_2017.drop('NT_FG_D1_CT', axis=1, inplace=True)
df_enade_2017.drop('NT_FG_D2', axis=1, inplace=True)
df_enade_2017.drop('NT_FG_D2_PT', axis=1, inplace=True)
df_enade_2017.drop('NT_FG_D2_CT', axis=1, inplace=True)
df_enade_2017.drop('NT_CE', axis=1, inplace=True)
df_enade_2017.drop('NT_OBJ_CE', axis=1, inplace=True)
df_enade_2017.drop('NT_DIS_CE', axis=1, inplace=True)
df_enade_2017.drop('NT_CE_D1', axis=1, inplace=True)
df_enade_2017.drop('NT_CE_D2', axis=1, inplace=True)
df_enade_2017.drop('NT_CE_D3', axis=1, inplace=True)

df_enade_2017.drop('CO_RS_I1', axis=1, inplace=True)
df_enade_2017.drop('CO_RS_I2', axis=1, inplace=True)
df_enade_2017.drop('CO_RS_I3', axis=1, inplace=True)
df_enade_2017.drop('CO_RS_I4', axis=1, inplace=True)
df_enade_2017.drop('CO_RS_I5', axis=1, inplace=True)
df_enade_2017.drop('CO_RS_I6', axis=1, inplace=True)
df_enade_2017.drop('CO_RS_I7', axis=1, inplace=True)
df_enade_2017.drop('CO_RS_I8', axis=1, inplace=True)
df_enade_2017.drop('CO_RS_I9', axis=1, inplace=True)
df_enade_2017.drop('TP_INSCRICAO_ADM', axis=1, inplace=True)
df_enade_2017.drop('TP_INSCRICAO', axis=1, inplace=True)

df_enade_2017.drop('QE_I07', axis=1, inplace=True)
df_enade_2017.drop('QE_I14', axis=1, inplace=True)
df_enade_2017.drop('QE_I26', axis=1, inplace=True)
df_enade_2017.drop('QE_I30', axis=1, inplace=True)
df_enade_2017.drop('QE_I31', axis=1, inplace=True)
df_enade_2017.drop('QE_I32', axis=1, inplace=True)
df_enade_2017.drop('QE_I33', axis=1, inplace=True)
df_enade_2017.drop('QE_I42', axis=1, inplace=True)
df_enade_2017.drop('QE_I46', axis=1, inplace=True)
df_enade_2017.drop('QE_I47', axis=1, inplace=True)
df_enade_2017.drop('QE_I48', axis=1, inplace=True)
df_enade_2017.drop('QE_I52', axis=1, inplace=True)
df_enade_2017.drop('QE_I53', axis=1, inplace=True)
df_enade_2017.drop('QE_I55', axis=1, inplace=True)
df_enade_2017.drop('QE_I66', axis=1, inplace=True)

# df_enade_2017.drop('QE_I26', axis=1, inplace=True)
# df_enade_2017.drop('QE_I27', axis=1, inplace=True)
# df_enade_2017.drop('QE_I28', axis=1, inplace=True)
# df_enade_2017.drop('QE_I29', axis=1, inplace=True)
# df_enade_2017.drop('QE_I30', axis=1, inplace=True)
# df_enade_2017.drop('QE_I31', axis=1, inplace=True)
# df_enade_2017.drop('QE_I32', axis=1, inplace=True)
# df_enade_2017.drop('QE_I33', axis=1, inplace=True)
# df_enade_2017.drop('QE_I34', axis=1, inplace=True)
# df_enade_2017.drop('QE_I35', axis=1, inplace=True)
# df_enade_2017.drop('QE_I36', axis=1, inplace=True)
# df_enade_2017.drop('QE_I37', axis=1, inplace=True)
df_enade_2017.drop('QE_I38', axis=1, inplace=True)
df_enade_2017.drop('QE_I39', axis=1, inplace=True)
# df_enade_2017.drop('QE_I40', axis=1, inplace=True)
# df_enade_2017.drop('QE_I41', axis=1, inplace=True)
# df_enade_2017.drop('QE_I43', axis=1, inplace=True)
# df_enade_2017.drop('QE_I44', axis=1, inplace=True)
# df_enade_2017.drop('QE_I45', axis=1, inplace=True)
# df_enade_2017.drop('QE_I46', axis=1, inplace=True)
# df_enade_2017.drop('QE_I47', axis=1, inplace=True)
# df_enade_2017.drop('QE_I48', axis=1, inplace=True)
df_enade_2017.drop('QE_I49', axis=1, inplace=True)
# df_enade_2017.drop('QE_I50', axis=1, inplace=True)
# df_enade_2017.drop('QE_I51', axis=1, inplace=True)
# df_enade_2017.drop('QE_I52', axis=1, inplace=True)
# df_enade_2017.drop('QE_I53', axis=1, inplace=True)
# df_enade_2017.drop('QE_I54', axis=1, inplace=True)
# df_enade_2017.drop('QE_I55', axis=1, inplace=True)
# df_enade_2017.drop('QE_I56', axis=1, inplace=True)
# df_enade_2017.drop('QE_I57', axis=1, inplace=True)
# df_enade_2017.drop('QE_I58', axis=1, inplace=True)
# df_enade_2017.drop('QE_I59', axis=1, inplace=True)
# df_enade_2017.drop('QE_I60', axis=1, inplace=True)
# df_enade_2017.drop('QE_I62', axis=1, inplace=True)
# df_enade_2017.drop('QE_I63', axis=1, inplace=True)
# df_enade_2017.drop('QE_I64', axis=1, inplace=True)
# df_enade_2017.drop('QE_I65', axis=1, inplace=True)
# df_enade_2017.drop('QE_I66', axis=1, inplace=True)
# df_enade_2017.drop('QE_I67', axis=1, inplace=True)
# df_enade_2017.drop('ANO_FIM_EM', axis=1, inplace=True)
df_enade_2017.drop('QE_I69', axis=1, inplace=True)
df_enade_2017.drop('QE_I70', axis=1, inplace=True)
df_enade_2017.drop('QE_I71', axis=1, inplace=True)
df_enade_2017.drop('QE_I72', axis=1, inplace=True)
df_enade_2017.drop('QE_I73', axis=1, inplace=True)
df_enade_2017.drop('QE_I74', axis=1, inplace=True)
df_enade_2017.drop('QE_I75', axis=1, inplace=True)
df_enade_2017.drop('QE_I76', axis=1, inplace=True)
df_enade_2017.drop('QE_I77', axis=1, inplace=True)
df_enade_2017.drop('QE_I78', axis=1, inplace=True)
df_enade_2017.drop('QE_I79', axis=1, inplace=True)
df_enade_2017.drop('QE_I80', axis=1, inplace=True)
df_enade_2017.drop('QE_I81', axis=1, inplace=True)
# df_enade_2017.drop('CO_TURNO_GRADUACAO', axis=1, inplace=True)

#renomeando variáveis

df_enade_2017.rename(columns={'NU_ANO': 'ANO_ENADE',
                            'CO_IES': 'CODIGO_IES',
                            'CO_CATEGAD': 'CATEGORIA_ADM_IES',
                            'CO_ORGACAD': 'ORGANIZACAO_ACAD_IES',
                            'CO_GRUPO': 'AREA_CURSO',
                            'CO_CURSO': 'CODIGO_CURSO',
                            'CO_MODALIDADE': 'MODALIDADE_CURSO',
                            'CO_MUNIC_CURSO': 'MUNICIPIO_CURSO',
                            'CO_UF_CURSO': 'UF_CURSO',
                            'CO_REGIAO_CURSO': 'REGIAO_CURSO',
                            'NU_IDADE': 'IDADE',
                            'TP_SEXO': 'SEXO',
                            'ANO_FIM_EM': 'ANO_FIM_ENS_MEDIO',
                            'ANO_IN_GRAD': 'ANO_INICIO_GRADUACAO',
                            'CO_TURNO_GRADUACAO': 'TURNO_GRADUACAO',
                            'TP_PRES': 'PRESENCA_ENADE',
                            'NT_GER': 'NOTA_BRUTA_ENADE',
                            # 'NT_FG': 'NOTA_BRUTA_FORMACAO_GERAL_ENADE',
                            # 'NT_OBJ_FG': 'NOTA_BRUTA_FORMACAO_GERAL_OBJETIVA_ENADE',
                            # 'NT_DIS_FG': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_ENADE',
                            # 'NT_FG_D1': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_1_ENADE',
                            # 'NT_FG_D1_PT': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_1_PORTUGUES_ENADE',
                            # 'NT_FG_D1_CT': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_1_CONTEUDO_ENADE',
                            # 'NT_FG_D2': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_2_ENADE',
                            # 'NT_FG_D2_PT': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_2_PORTUGUES_ENADE',
                            # 'NT_FG_D2_CT': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_2_CONTEUDO_ENADE',
                            # 'NT_CE': 'NOTA_BRUTA_ESPECIFICA_ENADE',
                            # 'NT_OBJ_CE': 'NOTA_BRUTA_ESPECIFICA_OBJETIVA_ENADE',
                            # 'NT_DIS_CE': 'NOTA_BRUTA_ESPECIFICA_DISCURSIVA_ENADE',
                            # 'NT_CE_D1': 'NOTA_BRUTA_ESPECIFICA_DISCURSIVA_1_ENADE',
                            # 'NT_CE_D2': 'NOTA_BRUTA_ESPECIFICA_DISCURSIVA_2_ENADE',
                            # 'NT_CE_D3': 'NOTA_BRUTA_ESPECIFICA_DISCURSIVA_3_ENADE',
                            'QE_I01': 'ESTADO_CIVIL',
                            'QE_I02': 'COR_RACA',
                            'QE_I03': 'NACIONALIDADE',
                            'QE_I04': 'ESCOLARIDADE_PAI',
                            'QE_I05': 'ESCOLARIDADE_MAE',
                            'QE_I06': 'COMPANHIA_RESIDENCIA',
                            # 'QE_I07': 'QUANTIDADE_COMPANHIA_RESIDENCIA',
                            'QE_I08': 'RENDA_FAMILIAR',
                            'QE_I09': 'SITUACAO_FINANCEIRA',
                            'QE_I10': 'SITUACAO_TRABALHO',
                            'QE_I11': 'BOLSA_ESTUDOS',
                            'QE_I12': 'AUXILIO_PERMANENCIA',
                            'QE_I13': 'BOLSA_ACADEMICA',
                            # 'QE_I14': 'INDICADOR_PARTICIPACAO_ATIVIDADES_EXTERIOR',
                            'QE_I15': 'ACAO_AFIRMATIVA',
                            'QE_I16': 'UF_ESCOLA_ENS_MEDIO',
                            'QE_I17': 'CATEGORIA_ADM_ESCOLA_ENS_MEDIO',
                            'QE_I18': 'MODALIDADE_ENS_MEDIO',
                            'QE_I19': 'INCENTIVO_GRADUACAO',
                            'QE_I20': 'OFERTA_APOIO_GERAL',
                            'QE_I21': 'GRADUACAO_FAMILIA',
                            'QE_I22': 'LEITURA_ANUAL',
                            'QE_I23': 'DEDICACAO_SEMANAL',
                            'QE_I24': 'OFERTA_IDIOMA_IES',
                            'QE_I25': 'MOTIVO_GRADUACAO',
                            # 'QE_I26': 'MOTIVO_ESCOLHA_IES',
                            'QE_I27': 'FORMACAO_INTEGRAL',
                            'QE_I28': 'ATUACAO_PROFISSIONAL',
                            'QE_I29': 'CAPACIDADE_CRITICA',
                            # 'QE_I30': 'INDICADOR_APRENDIZAGEM_INOVADORA_CURSO',
                            # 'QE_I31': 'INDICADOR_DESENVOLVIMENTO_CONSCIENCIA_ETICA',
                            # 'QE_I32': 'INDICADOR_OPORTUNIDADE_EQUIPE_CURSO',
                            'QE_I33': 'CAPACIDADE_REFLEXAO',
                            'QE_I34': 'CAPACIDADE_ANALISE',
                            'QE_I35': 'CAPACIDADE_COMUNICACAO',
                            'QE_I36': 'CAPACIDADE_APRENDIZADO',
                            'QE_I37': 'RELACAO_PROFESSOR_ALUNO',
                            # 'QE_I38': 'PLANOS_ENSINO_PROFESSORES',
                            # 'QE_I39': 'REFERENCIAS_PROFESSORES',
                            'QE_I40': 'OFERTA_APOIO_IES',
                            'QE_I41': 'ACESSO_COORDENACAO_CURSO',
                            # 'QE_I42': 'DEDICACAO',
                            'QE_I43': 'ATIVIDADES_EXTENSAO_IES',
                            'QE_I44': 'ATIVIDADES_PESQUISA_IES',
                            'QE_I45': 'OFERTA_EVENTOS_IES',
                            # 'QE_I46': 'INDICADOR_OFERTA_OPORTUNIDADES_ATUACAO_COLEGIADOS_IES',
                            # 'QE_I47': 'INDICADOR_FAVORECIMENTO_TEORIA_ATIVIDADES_PRATICAS_CURSO',
                            # 'QE_I48': 'INDICADOR_SUFICIENCIA_ATIVIDADES_PRATICAS_CURSO',
                            # 'QE_I49': 'CONTEUDO_ATUALIZADO_CURSO',
                            'QE_I50': 'CONTRIBUICAO_ESTAGIO',
                            'QE_I51': 'CONTRIBUICAO_TCC',
                            # 'QE_I52': 'INDICADOR_OFERTA_INTERCAMBIOS_BRASIL_IES',
                            # 'QE_I53': 'INDICADOR_OFERTA_INTERCAMBIOS_EXTERIOR_IES',
                            'QE_I54': 'AVALIACOES_PERIODICAS_CURSO',
                            # 'QE_I55': 'INDICADOR_COMPATIBILIDADE_AVALIACOES_CONTEUDOS_PROFESSORES',
                            'QE_I56': 'SUPORTE_EXTERNO_PROFESSORES',
                            'QE_I57': 'DOMINIO_CONTEUDO_PROFESSORES',
                            'QE_I58': 'EMPREGO_TICS_PROFESSORES',
                            'QE_I59': 'PESSOAL_APOIO_IES',
                            'QE_I60': 'MONITORES_IES',
                            'QE_I61': 'INFRAESTRUTURA_SALAS_AULA_IES',
                            'QE_I62': 'RECURSOS_AULAS_PRATICAS_IES',
                            'QE_I63': 'AMBIENTES_AULAS_PRATICAS_IES',
                            'QE_I64': 'BIBLIOTECA_FISICA_IES',
                            'QE_I65': 'BIBLIOTECA_VIRTUAL_IES',
                            # 'QE_I66': 'INDICADOR_CONTRIBUICAO_ATIVIDADES_REFLEXAO',
                            'QE_I67': 'OFERTA_LAZER_IES',
                            'QE_I68': 'INFRAESTRUTURA_GERAL_IES',
                            }, inplace=True)

# df_enade_2017['CATEGORIA_ADM_IES'] = df_enade_2017['CATEGORIA_ADM_IES'].replace([1],10002)
# df_enade_2017['CATEGORIA_ADM_IES'] = df_enade_2017['CATEGORIA_ADM_IES'].replace([2],10001)
# df_enade_2017['CATEGORIA_ADM_IES'] = df_enade_2017['CATEGORIA_ADM_IES'].replace([3],10003)
# df_enade_2017['CATEGORIA_ADM_IES'] = df_enade_2017['CATEGORIA_ADM_IES'].replace([4],10005)
# df_enade_2017['CATEGORIA_ADM_IES'] = df_enade_2017['CATEGORIA_ADM_IES'].replace([5],10008)

df_enade = df_enade.append(df_enade_2017, ignore_index=True)

#dropando variáveis que não serão usadas

df_enade_2016.drop('CO_CATEGAD', axis=1, inplace=True)
df_enade_2016.drop('CO_ORGACAD', axis=1, inplace=True)

# df_enade_2016.drop('CO_GRUPO', axis=1, inplace=True)
df_enade_2016.drop('NU_ITEM_OFG', axis=1, inplace=True)
df_enade_2016.drop('NU_ITEM_OFG_Z', axis=1, inplace=True)
df_enade_2016.drop('NU_ITEM_OFG_X', axis=1, inplace=True)
df_enade_2016.drop('NU_ITEM_OFG_N', axis=1, inplace=True)
df_enade_2016.drop('NU_ITEM_OCE', axis=1, inplace=True)
df_enade_2016.drop('NU_ITEM_OCE_Z', axis=1, inplace=True)
df_enade_2016.drop('NU_ITEM_OCE_X', axis=1, inplace=True)
df_enade_2016.drop('NU_ITEM_OCE_N', axis=1, inplace=True)
df_enade_2016.drop('DS_VT_GAB_OFG_ORIG', axis=1, inplace=True)
df_enade_2016.drop('DS_VT_GAB_OFG_FIN', axis=1, inplace=True)
df_enade_2016.drop('DS_VT_GAB_OCE_ORIG', axis=1, inplace=True)
df_enade_2016.drop('DS_VT_GAB_OCE_FIN', axis=1, inplace=True)
df_enade_2016.drop('DS_VT_ESC_OFG', axis=1, inplace=True)
df_enade_2016.drop('DS_VT_ACE_OFG', axis=1, inplace=True)
df_enade_2016.drop('DS_VT_ESC_OCE', axis=1, inplace=True)
df_enade_2016.drop('DS_VT_ACE_OCE', axis=1, inplace=True)
# df_enade_2016.drop('TP_PRES', axis=1, inplace=True)
df_enade_2016.drop('TP_PR_GER', axis=1, inplace=True)
df_enade_2016.drop('TP_PR_OB_FG', axis=1, inplace=True)
df_enade_2016.drop('TP_PR_DI_FG', axis=1, inplace=True)
df_enade_2016.drop('TP_PR_OB_CE', axis=1, inplace=True)
df_enade_2016.drop('TP_PR_DI_CE', axis=1, inplace=True)
df_enade_2016.drop('TP_SFG_D1', axis=1, inplace=True)
df_enade_2016.drop('TP_SFG_D2', axis=1, inplace=True)
df_enade_2016.drop('TP_SCE_D1', axis=1, inplace=True)
df_enade_2016.drop('TP_SCE_D2', axis=1, inplace=True)
df_enade_2016.drop('TP_SCE_D3', axis=1, inplace=True)

# df_enade_2016.drop('NT_GER', axis=1, inplace=True)
df_enade_2016.drop('NT_FG', axis=1, inplace=True)
df_enade_2016.drop('NT_OBJ_FG', axis=1, inplace=True)
df_enade_2016.drop('NT_DIS_FG', axis=1, inplace=True)
df_enade_2016.drop('NT_FG_D1', axis=1, inplace=True)
df_enade_2016.drop('NT_FG_D1_PT', axis=1, inplace=True)
df_enade_2016.drop('NT_FG_D1_CT', axis=1, inplace=True)
df_enade_2016.drop('NT_FG_D2', axis=1, inplace=True)
df_enade_2016.drop('NT_FG_D2_PT', axis=1, inplace=True)
df_enade_2016.drop('NT_FG_D2_CT', axis=1, inplace=True)
df_enade_2016.drop('NT_CE', axis=1, inplace=True)
df_enade_2016.drop('NT_OBJ_CE', axis=1, inplace=True)
df_enade_2016.drop('NT_DIS_CE', axis=1, inplace=True)
df_enade_2016.drop('NT_CE_D1', axis=1, inplace=True)
df_enade_2016.drop('NT_CE_D2', axis=1, inplace=True)
df_enade_2016.drop('NT_CE_D3', axis=1, inplace=True)

df_enade_2016.drop('CO_RS_I1', axis=1, inplace=True)
df_enade_2016.drop('CO_RS_I2', axis=1, inplace=True)
df_enade_2016.drop('CO_RS_I3', axis=1, inplace=True)
df_enade_2016.drop('CO_RS_I4', axis=1, inplace=True)
df_enade_2016.drop('CO_RS_I5', axis=1, inplace=True)
df_enade_2016.drop('CO_RS_I6', axis=1, inplace=True)
df_enade_2016.drop('CO_RS_I7', axis=1, inplace=True)
df_enade_2016.drop('CO_RS_I8', axis=1, inplace=True)
df_enade_2016.drop('CO_RS_I9', axis=1, inplace=True)
# df_enade_2016.drop('TP_INSCRICAO_ADM', axis=1, inplace=True)
# df_enade_2016.drop('TP_INSCRICAO', axis=1, inplace=True)

df_enade_2016.drop('QE_I07', axis=1, inplace=True)
df_enade_2016.drop('QE_I14', axis=1, inplace=True)
df_enade_2016.drop('QE_I26', axis=1, inplace=True)
df_enade_2016.drop('QE_I30', axis=1, inplace=True)
df_enade_2016.drop('QE_I31', axis=1, inplace=True)
df_enade_2016.drop('QE_I32', axis=1, inplace=True)
df_enade_2016.drop('QE_I33', axis=1, inplace=True)
df_enade_2016.drop('QE_I42', axis=1, inplace=True)
df_enade_2016.drop('QE_I46', axis=1, inplace=True)
df_enade_2016.drop('QE_I47', axis=1, inplace=True)
df_enade_2016.drop('QE_I48', axis=1, inplace=True)
df_enade_2016.drop('QE_I52', axis=1, inplace=True)
df_enade_2016.drop('QE_I53', axis=1, inplace=True)
df_enade_2016.drop('QE_I55', axis=1, inplace=True)
df_enade_2016.drop('QE_I66', axis=1, inplace=True)


# df_enade_2016.drop('QE_I27', axis=1, inplace=True)
# df_enade_2016.drop('QE_I28', axis=1, inplace=True)
# df_enade_2016.drop('QE_I29', axis=1, inplace=True)
# df_enade_2016.drop('QE_I30', axis=1, inplace=True)
# df_enade_2016.drop('QE_I31', axis=1, inplace=True)
# df_enade_2016.drop('QE_I32', axis=1, inplace=True)
# df_enade_2016.drop('QE_I33', axis=1, inplace=True)
# df_enade_2016.drop('QE_I34', axis=1, inplace=True)
# df_enade_2016.drop('QE_I35', axis=1, inplace=True)
# df_enade_2016.drop('QE_I36', axis=1, inplace=True)
# df_enade_2016.drop('QE_I37', axis=1, inplace=True)
df_enade_2016.drop('QE_I38', axis=1, inplace=True)
df_enade_2016.drop('QE_I39', axis=1, inplace=True)
# df_enade_2016.drop('QE_I40', axis=1, inplace=True)
# df_enade_2016.drop('QE_I41', axis=1, inplace=True)
# df_enade_2016.drop('QE_I43', axis=1, inplace=True)
# df_enade_2016.drop('QE_I44', axis=1, inplace=True)
# df_enade_2016.drop('QE_I45', axis=1, inplace=True)
# df_enade_2016.drop('QE_I46', axis=1, inplace=True)
# df_enade_2016.drop('QE_I47', axis=1, inplace=True)
# df_enade_2016.drop('QE_I48', axis=1, inplace=True)
df_enade_2016.drop('QE_I49', axis=1, inplace=True)
# df_enade_2016.drop('QE_I50', axis=1, inplace=True)
# df_enade_2016.drop('QE_I51', axis=1, inplace=True)
# df_enade_2016.drop('QE_I52', axis=1, inplace=True)
# df_enade_2016.drop('QE_I53', axis=1, inplace=True)
# df_enade_2016.drop('QE_I54', axis=1, inplace=True)
# df_enade_2016.drop('QE_I55', axis=1, inplace=True)
# df_enade_2016.drop('QE_I56', axis=1, inplace=True)
# df_enade_2016.drop('QE_I57', axis=1, inplace=True)
# df_enade_2016.drop('QE_I58', axis=1, inplace=True)
# df_enade_2016.drop('QE_I59', axis=1, inplace=True)
# df_enade_2016.drop('QE_I60', axis=1, inplace=True)
# df_enade_2016.drop('QE_I62', axis=1, inplace=True)
# df_enade_2016.drop('QE_I63', axis=1, inplace=True)
# df_enade_2016.drop('QE_I64', axis=1, inplace=True)
# df_enade_2016.drop('QE_I65', axis=1, inplace=True)
# df_enade_2016.drop('QE_I66', axis=1, inplace=True)
# df_enade_2016.drop('QE_I67', axis=1, inplace=True)

df_enade_2016.drop('TP_SEMESTRE', axis=1, inplace=True)
df_enade_2016.drop('ID_STATUS', axis=1, inplace=True)
df_enade_2016.drop('AMOSTRA', axis=1, inplace=True)
df_enade_2016.drop('IN_GRAD', axis=1, inplace=True)

df_enade_2016.rename(columns={'NU_ANO': 'ANO_ENADE',
                            'CO_IES': 'CODIGO_IES',
                            'CO_CATEGAD': 'CATEGORIA_ADM_IES',
                            'CO_ORGACAD': 'ORGANIZACAO_ACAD_IES',
                            'CO_GRUPO': 'AREA_CURSO',
                            'CO_CURSO': 'CODIGO_CURSO',
                            'CO_MODALIDADE': 'MODALIDADE_CURSO',
                            'CO_MUNIC_CURSO': 'MUNICIPIO_CURSO',
                            'CO_UF_CURSO': 'UF_CURSO',
                            'CO_REGIAO_CURSO': 'REGIAO_CURSO',
                            'NU_IDADE': 'IDADE',
                            'TP_SEXO': 'SEXO',
                            'ANO_FIM_2G': 'ANO_FIM_ENS_MEDIO',
                            'ANO_IN_GRAD': 'ANO_INICIO_GRADUACAO',
                            'TP_PRES': 'PRESENCA_ENADE',
                            'NT_GER': 'NOTA_BRUTA_ENADE',
                            # 'NT_FG': 'NOTA_BRUTA_FORMACAO_GERAL_ENADE',
                            # 'NT_OBJ_FG': 'NOTA_BRUTA_FORMACAO_GERAL_OBJETIVA_ENADE',
                            # 'NT_DIS_FG': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_ENADE',
                            # 'NT_FG_D1': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_1_ENADE',
                            # 'NT_FG_D1_PT': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_1_PORTUGUES_ENADE',
                            # 'NT_FG_D1_CT': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_1_CONTEUDO_ENADE',
                            # 'NT_FG_D2': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_2_ENADE',
                            # 'NT_FG_D2_PT': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_2_PORTUGUES_ENADE',
                            # 'NT_FG_D2_CT': 'NOTA_BRUTA_FORMACAO_GERAL_DISCURSIVA_2_CONTEUDO_ENADE',
                            # 'NT_CE': 'NOTA_BRUTA_ESPECIFICA_ENADE',
                            # 'NT_OBJ_CE': 'NOTA_BRUTA_ESPECIFICA_OBJETIVA_ENADE',
                            # 'NT_DIS_CE': 'NOTA_BRUTA_ESPECIFICA_DISCURSIVA_ENADE',
                            # 'NT_CE_D1': 'NOTA_BRUTA_ESPECIFICA_DISCURSIVA_1_ENADE',
                            # 'NT_CE_D2': 'NOTA_BRUTA_ESPECIFICA_DISCURSIVA_2_ENADE',
                            # 'NT_CE_D3': 'NOTA_BRUTA_ESPECIFICA_DISCURSIVA_3_ENADE',
                            'QE_I01': 'ESTADO_CIVIL',
                            'QE_I02': 'COR_RACA',
                            'QE_I03': 'NACIONALIDADE',
                            'QE_I04': 'ESCOLARIDADE_PAI',
                            'QE_I05': 'ESCOLARIDADE_MAE',
                            'QE_I06': 'COMPANHIA_RESIDENCIA',
                            # 'QE_I07': 'QUANTIDADE_COMPANHIA_RESIDENCIA',
                            'QE_I08': 'RENDA_FAMILIAR',
                            'QE_I09': 'SITUACAO_FINANCEIRA',
                            'QE_I10': 'SITUACAO_TRABALHO',
                            'QE_I11': 'BOLSA_ESTUDOS',
                            'QE_I12': 'AUXILIO_PERMANENCIA',
                            'QE_I13': 'BOLSA_ACADEMICA',
                            # 'QE_I14': 'INDICADOR_PARTICIPACAO_ATIVIDADES_EXTERIOR',
                            'QE_I15': 'ACAO_AFIRMATIVA',
                            'QE_I16': 'UF_ESCOLA_ENS_MEDIO',
                            'QE_I17': 'CATEGORIA_ADM_ESCOLA_ENS_MEDIO',
                            'QE_I18': 'MODALIDADE_ENS_MEDIO',
                            'QE_I19': 'INCENTIVO_GRADUACAO',
                            'QE_I20': 'OFERTA_APOIO_GERAL',
                            'QE_I21': 'GRADUACAO_FAMILIA',
                            'QE_I22': 'LEITURA_ANUAL',
                            'QE_I23': 'DEDICACAO_SEMANAL',
                            'QE_I24': 'OFERTA_IDIOMA_IES',
                            'QE_I25': 'MOTIVO_GRADUACAO',
                            # 'QE_I26': 'MOTIVO_ESCOLHA_IES',
                            'QE_I27': 'FORMACAO_INTEGRAL',
                            'QE_I28': 'ATUACAO_PROFISSIONAL',
                            'QE_I29': 'CAPACIDADE_CRITICA',
                            # 'QE_I30': 'INDICADOR_APRENDIZAGEM_INOVADORA_CURSO',
                            # 'QE_I31': 'INDICADOR_DESENVOLVIMENTO_CONSCIENCIA_ETICA',
                            # 'QE_I32': 'INDICADOR_OPORTUNIDADE_EQUIPE_CURSO',
                            'QE_I33': 'CAPACIDADE_REFLEXAO',
                            'QE_I34': 'CAPACIDADE_ANALISE',
                            'QE_I35': 'CAPACIDADE_COMUNICACAO',
                            'QE_I36': 'CAPACIDADE_APRENDIZADO',
                            'QE_I37': 'RELACAO_PROFESSOR_ALUNO',
                            # 'QE_I38': 'PLANOS_ENSINO_PROFESSORES',
                            # 'QE_I39': 'REFERENCIAS_PROFESSORES',
                            'QE_I40': 'OFERTA_APOIO_IES',
                            'QE_I41': 'ACESSO_COORDENACAO_CURSO',
                            # 'QE_I42': 'DEDICACAO',
                            'QE_I43': 'ATIVIDADES_EXTENSAO_IES',
                            'QE_I44': 'ATIVIDADES_PESQUISA_IES',
                            'QE_I45': 'OFERTA_EVENTOS_IES',
                            # 'QE_I46': 'INDICADOR_OFERTA_OPORTUNIDADES_ATUACAO_COLEGIADOS_IES',
                            # 'QE_I47': 'INDICADOR_FAVORECIMENTO_TEORIA_ATIVIDADES_PRATICAS_CURSO',
                            # 'QE_I48': 'INDICADOR_SUFICIENCIA_ATIVIDADES_PRATICAS_CURSO',
                            # 'QE_I49': 'CONTEUDO_ATUALIZADO_CURSO',
                            'QE_I50': 'CONTRIBUICAO_ESTAGIO',
                            'QE_I51': 'CONTRIBUICAO_TCC',
                            # 'QE_I52': 'INDICADOR_OFERTA_INTERCAMBIOS_BRASIL_IES',
                            # 'QE_I53': 'INDICADOR_OFERTA_INTERCAMBIOS_EXTERIOR_IES',
                            'QE_I54': 'AVALIACOES_PERIODICAS_CURSO',
                            # 'QE_I55': 'INDICADOR_COMPATIBILIDADE_AVALIACOES_CONTEUDOS_PROFESSORES',
                            'QE_I56': 'SUPORTE_EXTERNO_PROFESSORES',
                            'QE_I57': 'DOMINIO_CONTEUDO_PROFESSORES',
                            'QE_I58': 'EMPREGO_TICS_PROFESSORES',
                            'QE_I59': 'PESSOAL_APOIO_IES',
                            'QE_I60': 'MONITORES_IES',
                            'QE_I61': 'INFRAESTRUTURA_SALAS_AULA_IES',
                            'QE_I62': 'RECURSOS_AULAS_PRATICAS_IES',
                            'QE_I63': 'AMBIENTES_AULAS_PRATICAS_IES',
                            'QE_I64': 'BIBLIOTECA_FISICA_IES',
                            'QE_I65': 'BIBLIOTECA_VIRTUAL_IES',
                            # 'QE_I66': 'INDICADOR_CONTRIBUICAO_ATIVIDADES_REFLEXAO',
                            'QE_I67': 'OFERTA_LAZER_IES',
                            'QE_I68': 'INFRAESTRUTURA_GERAL_IES',

                            }, inplace=True)

turnos = []

for i, j in df_enade_2016.iterrows():
    valor = '0'
    if j['IN_MATUT'] == '1':
        valor = '1'
        if j['IN_VESPER'] == '1':
            valor = '3'
            # if j['IN_NOTURNO'] == '1':
            #     valor = '0'
        elif j['IN_NOTURNO'] == '1':
            valor = '3'
    elif j['IN_VESPER'] == '1':
        valor = '2'
        if j['IN_NOTURNO'] == '1':
            valor = '3'
    elif j['IN_NOTURNO'] == '1':
        valor = '4'
    turnos.append(valor)

df_enade_2016.drop('IN_MATUT', axis=1, inplace=True)
df_enade_2016.drop('IN_VESPER', axis=1, inplace=True)
df_enade_2016.drop('IN_NOTURNO', axis=1, inplace=True)

df_enade_2016.insert(15, 'TURNO_GRADUACAO', turnos)

df_enade = df_enade.append(df_enade_2016, ignore_index=True)

df_enade.drop_duplicates(ignore_index=True, inplace=True)
df_enade.reset_index(drop=True, inplace=True)

# df_enade['NOTA_BRUTA_ENADE'].apply(lambda x: str(x).replace(',','.'))

df_enade.to_csv('enade.csv', index=False)

# df_enade = pd.read_csv("enade_todas_as_inscricoes_com_missing_com_escopo_maior.csv", sep=",", encoding = "ISO-8859-1", dtype='unicode')

profile = pr(df_enade, title='Analisando dados sobre todas as inscrições do ENADE de 2016, 2017 e 2018 de ests de cursos de todo o Brasil, com valores faltantes', minimal=True, html={'style':{'full_width':True}})
profile.to_file("enade.html")

df_enade = df_enade.loc[df_enade['PRESENCA_ENADE']=='555']
df_enade.drop('PRESENCA_ENADE', axis=1, inplace=True)

df_enade = df_enade.loc[(df_enade['CODIGO_IES'] != '708') & (df_enade['CODIGO_IES'] != '18210')]

df_enade.reset_index(drop=True, inplace=True)
df_enade.to_csv('enade_1.csv', index=False)

# df_enade = pd.read_csv("enade_presencas_validas_com_missing_com_escopo_maior.csv", sep=",", encoding = "ISO-8859-1", dtype='unicode')

profile = pr(df_enade, title='Analisando dados sobre as inscrições válidas do ENADE de 2016, 2017 e 2018 de ests de cursos de todo o Brasil, com valores faltantes', minimal=True, html={'style':{'full_width':True}})
profile.to_file("enade_1.html")

df_enade.dropna(inplace=True)
df_enade.reset_index(drop=True, inplace=True)

# for i,j in df_enade.iterrows():
#     j['NOTA_BRUTA_ENADE'] = str(j['NOTA_BRUTA_ENADE']).replace(',','.')

notas = []

# for i,j in df_enade.iterrows():
#     j['NOTA_BRUTA_ENADE'] = str(j['NOTA_BRUTA_ENADE']).replace(',','.')

for i, j in df_enade.iterrows():
    nota = str(j['NOTA_BRUTA_ENADE']).replace(',','.')
    notas.append(nota)

df_enade.drop('NOTA_BRUTA_ENADE', axis=1, inplace=True)

df_enade.insert(1, 'NOTA_BRUTA_ENADE', notas)

df_enade.to_csv('enade_2.csv', index=False)

# df_enade = pd.read_csv("enade_presencas_validas_sem_missing_com_escopo_maior.csv", sep=",", encoding = "ISO-8859-1", dtype='unicode')

profile = pr(df_enade, title='Analisando dados sobre as inscrições válidas do ENADE de 2016, 2017 e 2018 de ests de cursos de todo o Brasil, sem valores faltantes', minimal=True, html={'style':{'full_width':True}})
profile.to_file("enade_2.html")