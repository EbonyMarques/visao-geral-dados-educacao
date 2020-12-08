#extrair e formatar enade
#extrair e formatar ies
#extrair e formatar igc
#extrair e formatar cpc
#extrair e formatar conceito enade
#extrair e formatar quantidade de cursos
#extrair e formatar quantidade de locais de oferta ?
#extrair e formatar quantidade de alunos
#unir enade, ies, igc, cpc, conceito enade, quantidade de cursos, locais de oferta ? e alunos para formar a base final

import pandas as pd
from pandas_profiling import ProfileReport as pr

class Manager():
    def __init__(self):
        print('Inicializando...')

        self.enade_formatter()
        # self.ies_formatter()
        # self.igc_formatter()
        # self.cpc_formater()
        # self.conceito_enade_formatter()
        # self.database_maker()

    def reader(self, path, read_method, separator = None, dtype = 'unicode'):
        '''The return value of this method is a dataframe that contains the database loaded from the path passed as a parameter'''

        print('Lendo', path)

        if read_method == 'csv':
            return pd.read_csv(path, sep = separator, encoding = 'ISO-8859-1', dtype = dtype)
        elif read_method == 'excel':
            return pd.read_excel(path, dtype = dtype)
        else:
            return pd.read_excel(path, sheet_name = read_method, dtype = dtype)

    def writer(self, dataframe, file_name, write_index = False):
        '''This method writes a dataframe to a .csv file whose name is passed as a parameter'''
        
        print('Escrevendo', file_name)

        dataframe.to_csv(file_name, index = write_index)

    def analyzer(self, dataframe, title, file_name, minimal_mode = True):
        '''This method writes an analysis based on the Pandas Profiling library about a dataframe passed as a parameter'''

        print('Analisando', title)

        profile = pr(dataframe, title = title, minimal = minimal_mode, html = {'style':{'full_width':True}})
        profile.to_file(file_name)

    def enade_formatter(self):
        #Iterations that will be performed
        iterations = [2018, 2017, 2016]

        #Creation of the final dataframe variable
        final_dataframe = None

        #Definition of variables necessary for all iterations (drop and rename)
        commom_variables_to_drop = ['CO_CATEGAD',
                                    'CO_ORGACAD',
                                    'NU_ITEM_OFG',
                                    'NU_ITEM_OFG_Z',
                                    'NU_ITEM_OFG_X',
                                    'NU_ITEM_OFG_N',
                                    'NU_ITEM_OCE',
                                    'NU_ITEM_OCE_Z',
                                    'NU_ITEM_OCE_X',
                                    'NU_ITEM_OCE_N',
                                    'DS_VT_GAB_OFG_ORIG',
                                    'DS_VT_GAB_OFG_FIN',
                                    'DS_VT_GAB_OCE_ORIG',
                                    'DS_VT_GAB_OCE_FIN',
                                    'DS_VT_ESC_OFG',
                                    'DS_VT_ACE_OFG',
                                    'DS_VT_ESC_OCE',
                                    'DS_VT_ACE_OCE',
                                    'TP_PR_GER',
                                    'TP_PR_OB_FG',
                                    'TP_PR_DI_FG',
                                    'TP_PR_OB_CE',
                                    'TP_PR_DI_CE',
                                    'TP_SFG_D1',
                                    'TP_SFG_D2',
                                    'TP_SCE_D1',
                                    'TP_SCE_D2',
                                    'TP_SCE_D3',
                                    'NT_FG',
                                    'NT_OBJ_FG',
                                    'NT_DIS_FG',
                                    'NT_FG_D1',
                                    'NT_FG_D1_PT',
                                    'NT_FG_D1_CT',
                                    'NT_FG_D2',
                                    'NT_FG_D2_PT',
                                    'NT_FG_D2_CT',
                                    'NT_CE',
                                    'NT_OBJ_CE',
                                    'NT_DIS_CE',
                                    'NT_CE_D1',
                                    'NT_CE_D2',
                                    'NT_CE_D3',
                                    'CO_RS_I1',
                                    'CO_RS_I2',
                                    'CO_RS_I3',
                                    'CO_RS_I4',
                                    'CO_RS_I5',
                                    'CO_RS_I6',
                                    'CO_RS_I7',
                                    'CO_RS_I8',
                                    'CO_RS_I9',
                                    'QE_I07',
                                    'QE_I26',
                                    'QE_I30',
                                    'QE_I31',
                                    'QE_I32',
                                    'QE_I33',
                                    'QE_I38',
                                    'QE_I39',
                                    'QE_I42',
                                    'QE_I46',
                                    'QE_I47',
                                    'QE_I48',
                                    'QE_I49',
                                    'QE_I52',
                                    'QE_I53',
                                    'QE_I55',
                                    'QE_I66']

        variables_to_rename = {'NU_ANO': 'ANO_ENADE',
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
                                'ANO_FIM_EM': 'ANO_FIM_ENSINO_MEDIO',
                                'ANO_FIM_2G': 'ANO_FIM_ENSINO_MEDIO',
                                'ANO_IN_GRAD': 'ANO_INICIO_GRADUACAO',
                                'CO_TURNO_GRADUACAO': 'TURNO_GRADUACAO',
                                'TP_PRES': 'PRESENCA_ENADE',
                                'NT_GER': 'NOTA_BRUTA_ENADE',
                                'QE_I01': 'ESTADO_CIVIL',
                                'QE_I02': 'COR_RACA',
                                'QE_I03': 'NACIONALIDADE',
                                'QE_I04': 'ESCOLARIDADE_PAI',
                                'QE_I05': 'ESCOLARIDADE_MAE',
                                'QE_I06': 'COMPANHIA_RESIDENCIA',
                                'QE_I08': 'RENDA_FAMILIAR',
                                'QE_I09': 'SITUACAO_FINANCEIRA',
                                'QE_I10': 'SITUACAO_TRABALHO',
                                'QE_I11': 'BOLSA_ESTUDOS',
                                'QE_I12': 'AUXILIO_PERMANENCIA',
                                'QE_I13': 'BOLSA_ACADEMICA',
                                'QE_I14': 'INDICADOR_PARTICIPACAO_ATIVIDADES_EXTERIOR',
                                'QE_I15': 'ACAO_AFIRMATIVA',
                                'QE_I16': 'UF_ESCOLA_ENSINO_MEDIO',
                                'QE_I17': 'CATEGORIA_ADM_ESCOLA_ENSINO_MEDIO',
                                'QE_I18': 'MODALIDADE_ENSINO_MEDIO',
                                'QE_I19': 'INCENTIVO_GRADUACAO',
                                'QE_I20': 'OFERTA_APOIO_GERAL',
                                'QE_I21': 'GRADUACAO_FAMILIA',
                                'QE_I22': 'LEITURA_ANUAL',
                                'QE_I23': 'DEDICACAO_SEMANAL',
                                'QE_I24': 'OFERTA_IDIOMA_IES',
                                'QE_I25': 'MOTIVO_GRADUACAO',
                                'QE_I27': 'FORMACAO_INTEGRAL',
                                'QE_I28': 'ATUACAO_PROFISSIONAL',
                                'QE_I29': 'CAPACIDADE_CRITICA',
                                'QE_I33': 'CAPACIDADE_REFLEXAO',
                                'QE_I34': 'CAPACIDADE_ANALISE',
                                'QE_I35': 'CAPACIDADE_COMUNICACAO',
                                'QE_I36': 'CAPACIDADE_APRENDIZADO',
                                'QE_I37': 'RELACAO_PROFESSOR_ALUNO',
                                'QE_I40': 'OFERTA_APOIO_IES',
                                'QE_I41': 'ACESSO_COORDENACAO_CURSO',
                                'QE_I43': 'ATIVIDADES_EXTENSAO_IES',
                                'QE_I44': 'ATIVIDADES_PESQUISA_IES',
                                'QE_I45': 'OFERTA_EVENTOS_IES',
                                'QE_I50': 'CONTRIBUICAO_ESTAGIO',
                                'QE_I51': 'CONTRIBUICAO_TCC',
                                'QE_I54': 'AVALIACOES_PERIODICAS_CURSO',
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
                                'QE_I67': 'OFERTA_LAZER_IES',
                                'QE_I68': 'INFRAESTRUTURA_GERAL_IES'}

        #Performing iterations
        for i in iterations:
            #Defining list of variables to drop
            variables_to_drop = []

            print('Efetuando a iteração',i,'do ENADE')

            #Defining peculiarities of each iteration
            #Defining path to the database
            #Defining list of variables to drop in the iteration
            if i == 2018:
                path = 'enade/2018/3.dados/microdados_enade_2018.csv'
                other_variables_to_drop = ['TP_INSCRICAO_ADM',
                                           'TP_INSCRICAO']
                variables_to_drop = commom_variables_to_drop + other_variables_to_drop
            elif i == 2017:
                path = 'enade/2017/3.dados/microdados_enade_2017.csv'
                other_variables_to_drop = ['TP_INSCRICAO_ADM',
                                            'TP_INSCRICAO',
                                            'QE_I69',
                                            'QE_I70',
                                            'QE_I71',
                                            'QE_I72',
                                            'QE_I73',
                                            'QE_I74',
                                            'QE_I75',
                                            'QE_I76',
                                            'QE_I77',
                                            'QE_I78',
                                            'QE_I79',
                                            'QE_I80',
                                            'QE_I81']
                variables_to_drop = commom_variables_to_drop + other_variables_to_drop
            elif i == 2016:
                path = 'enade/2016/3.dados/microdados_enade_2016.csv'
                other_variables_to_drop = ['TP_SEMESTRE',
                                            'ID_STATUS',
                                            'AMOSTRA',
                                            'IN_GRAD']
                variables_to_drop = commom_variables_to_drop + other_variables_to_drop

            #Reading database
            dataframe = self.reader(path, 'csv', ';')

            #Dropping variables
            dataframe.drop(variables_to_drop, axis = 1, inplace = True)

            #Renaming variables
            dataframe.rename(columns = variables_to_rename, inplace = True)

            #Performing necessary and specific operations for iteration
            if i == 2018:
                dataframe['MODALIDADE_CURSO'] = dataframe['MODALIDADE_CURSO'].replace(['2'], '0')
                # modalities = []

                # for a, b in dataframe.iterrows():
                #     modality = b['MODALIDADE_CURSO'].replace('2', '0')
                #     modalities.append(modality)

                # dataframe.drop(['MODALIDADE_CURSO'], axis = 1, inplace = True)
               
                # dataframe.insert(6, 'MODALIDADE_CURSO', modalities)
                
            elif i == 2016:
                shifts = []

                for a, b in dataframe.iterrows():
                    value = '0'
                    if b['IN_MATUT'] == '1':
                        value = '1'
                        if b['IN_VESPER'] == '1':
                            value = '3'
                        elif b['IN_NOTURNO'] == '1':
                            value = '3'
                    elif b['IN_VESPER'] == '1':
                        value = '2'
                        if b['IN_NOTURNO'] == '1':
                            value = '3'
                    elif b['IN_NOTURNO'] == '1':
                        value = '4'
                    shifts.append(value)

                dataframe.drop(['IN_MATUT', 'IN_VESPER', 'IN_NOTURNO'], axis = 1, inplace = True)
               
                dataframe.insert(15, 'TURNO_GRADUACAO', shifts)
            
            print('oxe',i)

            #Adding data read in the iteration to the final dataframe
            if i == 2018:
                final_dataframe = dataframe
            else:
                final_dataframe = final_dataframe.append(dataframe, ignore_index = True)

        #Performing necessary operations for final dataframe

        #Dropping possible duplicate rows
        final_dataframe.drop_duplicates(ignore_index = True, inplace = True)
        final_dataframe.reset_index(drop = True, inplace = True)

        #Selecting valid presences in the ENADE
        final_dataframe = final_dataframe.loc[final_dataframe['PRESENCA_ENADE'] == '555']
        final_dataframe.drop('PRESENCA_ENADE', axis=1, inplace=True)

        #Selecting records that are not associated with missing IES 708 and 18210
        final_dataframe = final_dataframe.loc[(final_dataframe['CODIGO_IES'] != '708') & (final_dataframe['CODIGO_IES'] != '18210')]
        final_dataframe.reset_index(drop = True, inplace = True)

        final_dataframe['SEXO'] = final_dataframe['SEXO'].replace(['N'], 'M')
        
        #Dropping records with missing values
        final_dataframe.dropna(inplace = True)
        final_dataframe.reset_index(drop = True, inplace = True)

        #Replacing ',' with '.' in the records of the variable 'Nota_BRUTA_ENADE'
        scores = []

        for i, j in final_dataframe.iterrows():
            score = str(j['NOTA_BRUTA_ENADE']).replace(',','.')
            scores.append(score)

        #Dropping old 'NOTA_BRUTA_ENADE' variable with wrong data format
        final_dataframe.drop('NOTA_BRUTA_ENADE', axis=1, inplace=True)

        #Defining new 'NOTA_BRUTA_ENADE' variable with right data format
        final_dataframe.insert(1, 'NOTA_BRUTA_ENADE', scores)

        #Writing final dataframe data
        self.writer(final_dataframe, 'enade_novo_metodo.csv')

        #Analyzing final dataframe data
        self.analyzer(final_dataframe, 'NOVO ENADE', 'enade_novo_metodo.html')

    def ies_formatter(self):
        #Iterations that will be performed
        iterations = [2018, 2017, 2016]

        #Creation of the final dataframe variable
        final_dataframe = None

        #Definition of variables necessary for all iterations (drop and rename)
        commom_variables_to_drop = ['IN_ACESSO_OUTRAS_BASES']

        variables_to_rename = {'NU_ANO_CENSO': 'ANO_CENSO_IES',
                                'CO_IES': 'CODIGO_IES',
                                'NO_IES': 'NOME_IES',
                                'SG_IES': 'SIGLA_IES',
                                'SGL_IES': 'SIGLA_IES',
                                'CO_MANTENEDORA': 'CODIGO_MANTENEDORA_IES',
                                'NO_MANTENEDORA': 'NOME_MANTENEDORA_IES',
                                'TP_CATEGORIA_ADMINISTRATIVA': 'CATEGORIA_ADMINISTRATIVA_IES',
                                'TP_ORGANIZACAO_ACADEMICA': 'ORGANIZACAO_ACADEMICA_IES',
                                'CO_CATEGORIA_ADMINISTRATIVA': 'CATEGORIA_ADMINISTRATIVA_IES',
                                'CO_ORGANIZACAO_ACADEMICA': 'ORGANIZACAO_ACADEMICA_IES',
                                'CO_REGIAO': 'CODIGO_REGIAO_IES',
                                'CO_UF': 'CODIGO_UNIDADE_FEDERATIVA_IES',
                                'CO_MUNICIPIO': 'CODIGO_MUNICIPIO_IES',
                                'IN_CAPITAL': 'LOCALIZACAO_CAPITAL_IES',
                                'NO_REGIAO_IES': 'CODIGO_REGIAO_IES',
                                'CO_UF_IES': 'CODIGO_UNIDADE_FEDERATIVA_IES',
                                'CO_MUNICIPIO_IES': 'CODIGO_MUNICIPIO_IES',
                                'IN_CAPITAL_IES': 'LOCALIZACAO_CAPITAL_IES',

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
                                'VL_RECEITA_PROPRIA': 'RECEITA_PROPRIA_IES',
                                'VL_RECEITA_TRANSFERENCIA': 'RECEITA_TRANSFERENCIA_IES',
                                'VL_RECEITA_OUTRA': 'OUTRA_RECEITA_IES',
                                'VL_DESPESA_PESSOAL_DOCENTE': 'DESPESA_DOCENTE_IES',
                                'VL_DESPESA_PESSOAL_TECNICO': 'DESPESA_TECNICO_IES',
                                'VL_DESPESA_PESSOAL_ENCARGO': 'DESPESA_ENCARGO_IES',
                                'VL_DESPESA_CUSTEIO': 'DESPESA_CUSTEIO_IES',
                                'VL_DESPESA_INVESTIMENTO': 'DESPESA_INVESTIMENTO_IES',
                                'VL_DESPESA_PESQUISA': 'DESPESA_PESQUISA_IES',
                                'VL_DESPESA_OUTRA': 'OUTRA_DESPESA_IES',
                                'VL_TRANSFERENCIA': 'RECEITA_TRANSFERENCIA_IES',
                                'VL_OUTRA_RECEITA': 'OUTRA_RECEITA_IES',
                                'VL_DES_PESSOAL_REM_DOCENTE': 'DESPESA_DOCENTE_IES',
                                'VL_DES_PESSOAL_REM_TECNICO': 'DESPESA_TECNICO_IES',
                                'VL_DES_PESSOAL_ENCARGO': 'DESPESA_ENCARGO_IES',
                                'VL_DES_CUSTEIO': 'DESPESA_CUSTEIO_IES',
                                'VL_DES_INVESTIMENTO': 'DESPESA_INVESTIMENTO_IES',
                                'VL_DES_PESQUISA': 'DESPESA_PESQUISA_IES',
                                'VL_DES_OUTRAS': 'OUTRA_DESPESA_IES',

                                'IN_ACESSO_PORTAL_CAPES': 'ACESSO_PORTAL_CAPES_IES',
                                'IN_REPOSITORIO_INSTITUCIONAL': 'REPOSITORIO_INSTITUCIONAL_IES',
                                'IN_BUSCA_INTEGRADA': 'BUSCA_INTEGRADA_IES',
                                'IN_SERVICO_INTERNET': 'SERVICO_INTERNET_IES',
                                'IN_PARTICIPA_REDE_SOCIAL': 'PARTICIPACAO_REDE_SOCIAL_IES',
                                'IN_CATALOGO_ONLINE': 'CATALOGO_ONLINE_IES',
                                'TP_REFERENTE': 'REFERENCIA_FINANCEIRA_IES',
                                'IN_REFERENTE': 'REFERENCIA_FINANCEIRA_IES'}
        
        #Performing iterations
        for i in iterations:
            #Defining list of variables to drop
            variables_to_drop = []

            print('Efetuando a iteração',i,'de IES')

            #Defining peculiarities of each iteration
            #Defining path to the database
            #Defining list of variables to drop in the iteration
            if i == 2018:
                path = 'educacao_superior/2018/dados/dm_ies.csv'
                other_variables_to_drop = ['IN_ASSINA_OUTRA_BASE']
                variables_to_drop = commom_variables_to_drop + other_variables_to_drop
                print(variables_to_drop)
            elif i == 2017:
                path = 'educacao_superior/2017/dados/dm_ies.csv'
            elif i == 2016:
                path = 'educacao_superior/2016/dados/dm_ies.csv'
                other_variables_to_drop = ['DS_CATEGORIA_ADMINISTRATIVA',
                                            'DS_ORGANIZACAO_ACADEMICA',
                                            'NO_MUNICIPIO_IES',
                                            'SGL_UF_IES']
                variables_to_drop = commom_variables_to_drop + other_variables_to_drop

            #Reading database
            dataframe = self.reader(path, 'csv', '|')

            #Dropping variables
            dataframe.drop(variables_to_drop, axis = 1, inplace = True)

            #Renaming variables
            dataframe.rename(columns = variables_to_rename, inplace = True)

            #Performing necessary and specific operations for iteration
            if i == 2016:
                dataframe.insert(1, "ANO_CENSO_IES", ['2016']*len(dataframe.index), True)
            
            #Adding data read in the iteration to the final dataframe
            if i == 2018:
                final_dataframe = dataframe
            else:
                final_dataframe = final_dataframe.append(dataframe, ignore_index = True)

        #Performing necessary operations for final dataframe
        final_dataframe = final_dataframe.astype({'ANO_CENSO_IES': 'int32'})
        final_dataframe = final_dataframe.sort_values(by='ANO_CENSO_IES', ascending = False)
        
        #Dropping possible duplicate rows
        final_dataframe = final_dataframe.drop_duplicates(subset=['CODIGO_IES'], ignore_index = True)
        final_dataframe.reset_index(drop = True, inplace = True)

        final_dataframe['SIGLA_IES'].fillna('SEM SIGLA', inplace = True)

        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_FUNDAMENTAL_INCOMP_FEM_IES': 'int32'})
        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_FUNDAMENTAL_INCOMP_MASC_IES': 'int32'})
        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_FUNDAMENTAL_COMP_FEM_IES': 'int32'})
        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_FUNDAMENTAL_COMP_MASC_IES': 'int32'})
        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_MEDIO_FEM_IES': 'int32'})
        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_MEDIO_MASC_IES': 'int32'})
        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_SUPERIOR_FEM_IES': 'int32'})
        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_SUPERIOR_MASC_IES': 'int32'})
        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_ESPECIALIZACAO_FEM_IES': 'int32'})
        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_ESPECIALIZACAO_MASC_IES': 'int32'})
        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_MESTRADO_FEM_IES': 'int32'})
        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_MESTRADO_MASC_IES': 'int32'})
        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_DOUTORADO_FEM_IES': 'int32'})
        final_dataframe = final_dataframe.astype({'QTDE_TECNICOS_DOUTORADO_MASC_IES': 'int32'})

        final_dataframe['RECEITA_PROPRIA_IES'] = final_dataframe['RECEITA_PROPRIA_IES'].replace(['0'],'0.00')
        final_dataframe['RECEITA_TRANSFERENCIA_IES'] = final_dataframe['RECEITA_TRANSFERENCIA_IES'].replace(['0'],'0.00')
        final_dataframe['OUTRA_RECEITA_IES'] = final_dataframe['OUTRA_RECEITA_IES'].replace(['0'],'0.00')
        final_dataframe['DESPESA_DOCENTE_IES'] = final_dataframe['DESPESA_DOCENTE_IES'].replace(['0'],'0.00')
        final_dataframe['DESPESA_TECNICO_IES'] = final_dataframe['DESPESA_TECNICO_IES'].replace(['0'],'0.00')
        final_dataframe['DESPESA_ENCARGO_IES'] = final_dataframe['DESPESA_ENCARGO_IES'].replace(['0'],'0.00')
        final_dataframe['DESPESA_CUSTEIO_IES'] = final_dataframe['DESPESA_CUSTEIO_IES'].replace(['0'],'0.00')
        final_dataframe['DESPESA_INVESTIMENTO_IES'] = final_dataframe['DESPESA_INVESTIMENTO_IES'].replace(['0'],'0.00')
        final_dataframe['DESPESA_PESQUISA_IES'] = final_dataframe['DESPESA_PESQUISA_IES'].replace(['0'],'0.00')
        final_dataframe['OUTRA_DESPESA_IES'] = final_dataframe['OUTRA_DESPESA_IES'].replace(['0'],'0.00')

        qtde_tecnicos_fundamental = final_dataframe['QTDE_TECNICOS_FUNDAMENTAL_INCOMP_FEM_IES'] + final_dataframe['QTDE_TECNICOS_FUNDAMENTAL_INCOMP_MASC_IES'] + final_dataframe['QTDE_TECNICOS_FUNDAMENTAL_COMP_FEM_IES'] + final_dataframe['QTDE_TECNICOS_FUNDAMENTAL_COMP_MASC_IES']
        qtde_tecnicos_medio = final_dataframe['QTDE_TECNICOS_MEDIO_FEM_IES'] + final_dataframe['QTDE_TECNICOS_MEDIO_MASC_IES']
        qtde_tecnicos_superior = final_dataframe['QTDE_TECNICOS_SUPERIOR_FEM_IES'] + final_dataframe['QTDE_TECNICOS_SUPERIOR_MASC_IES']
        qtde_tecnicos_pos = final_dataframe['QTDE_TECNICOS_ESPECIALIZACAO_FEM_IES'] + final_dataframe['QTDE_TECNICOS_ESPECIALIZACAO_MASC_IES'] + final_dataframe['QTDE_TECNICOS_MESTRADO_FEM_IES'] + final_dataframe['QTDE_TECNICOS_MESTRADO_MASC_IES'] + final_dataframe['QTDE_TECNICOS_DOUTORADO_FEM_IES'] + final_dataframe['QTDE_TECNICOS_DOUTORADO_MASC_IES']

        final_dataframe.insert(12,'QTDE_TECNICOS_FUNDAMENTAL_IES',list(qtde_tecnicos_fundamental),True)
        final_dataframe.insert(13,'QTDE_TECNICOS_MEDIO_IES',list(qtde_tecnicos_medio),True)
        final_dataframe.insert(14,'QTDE_TECNICOS_SUPERIOR_IES',list(qtde_tecnicos_superior),True)
        final_dataframe.insert(15,'QTDE_TECNICOS_POS_IES',list(qtde_tecnicos_pos),True)

        final_dataframe.drop('QTDE_TECNICOS_FUNDAMENTAL_INCOMP_FEM_IES', axis=1, inplace=True)
        final_dataframe.drop('QTDE_TECNICOS_FUNDAMENTAL_INCOMP_MASC_IES', axis=1, inplace=True)
        final_dataframe.drop('QTDE_TECNICOS_FUNDAMENTAL_COMP_FEM_IES', axis=1, inplace=True)
        final_dataframe.drop('QTDE_TECNICOS_FUNDAMENTAL_COMP_MASC_IES', axis=1, inplace=True)
        final_dataframe.drop('QTDE_TECNICOS_MEDIO_FEM_IES', axis=1, inplace=True)
        final_dataframe.drop('QTDE_TECNICOS_MEDIO_MASC_IES', axis=1, inplace=True)
        final_dataframe.drop('QTDE_TECNICOS_SUPERIOR_FEM_IES', axis=1, inplace=True)
        final_dataframe.drop('QTDE_TECNICOS_SUPERIOR_MASC_IES', axis=1, inplace=True)
        final_dataframe.drop('QTDE_TECNICOS_ESPECIALIZACAO_FEM_IES', axis=1, inplace=True)
        final_dataframe.drop('QTDE_TECNICOS_ESPECIALIZACAO_MASC_IES', axis=1, inplace=True)
        final_dataframe.drop('QTDE_TECNICOS_MESTRADO_FEM_IES', axis=1, inplace=True)
        final_dataframe.drop('QTDE_TECNICOS_MESTRADO_MASC_IES', axis=1, inplace=True)
        final_dataframe.drop('QTDE_TECNICOS_DOUTORADO_FEM_IES', axis=1, inplace=True)
        final_dataframe.drop('QTDE_TECNICOS_DOUTORADO_MASC_IES', axis=1, inplace=True)

        final_dataframe = final_dataframe[['ANO_CENSO_IES','CODIGO_IES','NOME_IES','SIGLA_IES','CODIGO_MANTENEDORA_IES','NOME_MANTENEDORA_IES','CATEGORIA_ADMINISTRATIVA_IES','ORGANIZACAO_ACADEMICA_IES','CODIGO_REGIAO_IES','CODIGO_UNIDADE_FEDERATIVA_IES','CODIGO_MUNICIPIO_IES','LOCALIZACAO_CAPITAL_IES','QTDE_TOTAL_TECNICOS_IES','QTDE_TECNICOS_FUNDAMENTAL_IES','QTDE_TECNICOS_MEDIO_IES','QTDE_TECNICOS_SUPERIOR_IES','QTDE_TECNICOS_POS_IES','ACESSO_PORTAL_CAPES_IES','REPOSITORIO_INSTITUCIONAL_IES','BUSCA_INTEGRADA_IES','SERVICO_INTERNET_IES','PARTICIPACAO_REDE_SOCIAL_IES','CATALOGO_ONLINE_IES','QTDE_PERIODICOS_ELETRONICOS_IES','QTDE_LIVROS_ELETRONICOS_IES','REFERENCIA_FINANCEIRA_IES','RECEITA_PROPRIA_IES','RECEITA_TRANSFERENCIA_IES','OUTRA_RECEITA_IES','DESPESA_DOCENTE_IES','DESPESA_TECNICO_IES','DESPESA_ENCARGO_IES','DESPESA_CUSTEIO_IES','DESPESA_INVESTIMENTO_IES','DESPESA_PESQUISA_IES','OUTRA_DESPESA_IES']]

        #Writing final dataframe data
        self.writer(final_dataframe, 'ies_novo_metodo.csv')

        #Analyzing final dataframe data
        self.analyzer(final_dataframe, 'NOVA IES', 'ies_novo_metodo.html')
    
    def igc_formatter(self):
        #Iterations that will be performed
        iterations = [2018, 2017, 2016, 2015]

        #Creation of the final dataframe variable
        final_dataframe = None
        
        #Performing iterations
        for i in iterations:
            variables_to_consider = []
            variables_to_rename = {'Ano': 'ANO_IGC',
                                    'Código da IES': 'CODIGO_IES',
                                    'IGC (Faixa)': 'IGC_FAIXA',
                                    'nu_ano':'ANO_IGC',
                                    'co_ies': 'CODIGO_IES',
                                    'fx_igc': 'IGC_FAIXA',
                                    'Cód.IES': 'CODIGO_IES',
                                    'IGC (faixa)': 'IGC_FAIXA'}
            if i == 2018:
                path = 'indices/2018/igc_2018.xlsx'
                read_method = 'excel'
                variables_to_consider = ['Ano','Código da IES','IGC (Faixa)']
            elif i == 2017:
                path = 'indices/2017/igc_2017.xlsx'
                read_method = 'excel'
                variables_to_consider = ['Código da IES','IGC (Faixa)']
            elif i == 2016:
                path = 'indices/2016/igc_2016.xlsx'
                read_method = [0, 1, 2]
                variables_to_consider = ['nu_ano','co_ies','fx_igc']
            elif i == 2015:
                path = 'indices/2015/igc_2015.xlsx'
                read_method = [0, 1, 2]
                variables_to_consider = ['Ano','Cód.IES','IGC (faixa)']

            #Reading database
            dataframe = self.reader(path, read_method)
            
            if i == 2018 or i == 2017:
                dataframe = dataframe[variables_to_consider]
            elif i == 2016 or i == 2015:
                dataframe_backup = dataframe
                dataframe = dataframe_backup[0][variables_to_consider]
                dataframe = dataframe.append(dataframe_backup[1][variables_to_consider], ignore_index=True)
                dataframe = dataframe.append(dataframe_backup[2][variables_to_consider], ignore_index=True)

            if i == 2017:
                dataframe.insert(1,'ANO_IGC',['2017']*len(dataframe.index),True)

            #Renaming variables
            dataframe.rename(columns=variables_to_rename, inplace = True)

            #Adding data read in the iteration to the final dataframe
            if i == 2018:
                final_dataframe = dataframe
            else:
                final_dataframe = final_dataframe.append(dataframe, ignore_index = True)
            
        #Performing necessary operations for final dataframe
        final_dataframe = final_dataframe.astype({'ANO_IGC': 'int32'})
        final_dataframe = final_dataframe.sort_values(by = 'ANO_IGC', ascending = False)
        final_dataframe.drop_duplicates(subset = ['CODIGO_IES'], ignore_index = True, inplace = True)

        #Writing final dataframe data
        self.writer(final_dataframe, 'igc_novo_metodo.csv')

        #Analyzing final dataframe data
        self.analyzer(final_dataframe, 'NOVO IGC', 'igc_novo_metodo.html')

    def cpc_formater(self):
        #Iterations that will be performed
        iterations = [2018, 2017, 2016, 2015]

        #Creation of the final dataframe variable
        final_dataframe = None

        #Performing iterations
        for i in iterations:
            variables_to_consider = []
            variables_to_rename = {'Ano': 'ANO_CPC',
                                    'Edição': 'ANO_CPC',
                                    'Código da IES': 'CODIGO_IES',
                                    'Código do Curso': 'CODIGO_CURSO',
                                    'CPC (Faixa)': 'CPC_FAIXA',
                                    'CPC Faixa': 'CPC_FAIXA'}
            if i == 2018:
                path = 'indices/2018/cpc_2018.xlsx'
                variables_to_consider = ['Ano','Código da IES','Código do Curso','CPC (Faixa)']
            elif i == 2017:
                path = 'indices/2017/cpc_2017.xlsx'
                variables_to_consider = ['Edição','Código da IES','Código do Curso','CPC Faixa']
            elif i == 2016:
                path = 'indices/2016/cpc_2016.xls'
                variables_to_consider = ['Ano','Código da IES','Código do Curso','CPC Faixa']
            elif i == 2015:
                path = 'indices/2015/cpc_2015.xls'
                variables_to_consider = ['Ano','Código da IES','Código do Curso','CPC Faixa']

            #Reading database
            dataframe = self.reader(path, 'excel')
            dataframe = dataframe[variables_to_consider]

            #Renaming variables
            dataframe.rename(columns=variables_to_rename, inplace = True)

            #Adding data read in the iteration to the final dataframe
            if i == 2018:
                final_dataframe = dataframe
            else:
                final_dataframe = final_dataframe.append(dataframe, ignore_index = True)
        
        #Performing necessary operations for final dataframe
        final_dataframe = final_dataframe.astype({'ANO_CPC': 'int32'})
        final_dataframe = final_dataframe.sort_values(by = 'ANO_CPC', ascending = False)
        final_dataframe.drop_duplicates(subset = ['CODIGO_IES', 'CODIGO_CURSO'], ignore_index = True, inplace = True)

        #Writing final dataframe data
        self.writer(final_dataframe, 'cpc_novo_metodo.csv')

        #Analyzing final dataframe data
        self.analyzer(final_dataframe, 'NOVO CPC', 'cpc_novo_metodo.html')

    def conceito_enade_formatter(self):
        #Iterations that will be performed
        iterations = [2018, 2017, 2016, 2015]

        #Creation of the final dataframe variable
        final_dataframe = None

        #Performing iterations
        for i in iterations:
            variables_to_consider = []
            variables_to_rename = {'Ano': 'ANO_CONCEITO_ENADE',
                                    'Código da IES': 'CODIGO_IES',
                                    'Código do Curso': 'CODIGO_CURSO',
                                    'Conceito Enade Faixa)': 'CONCEITO_ENADE_FAIXA',
                                    'Conceito Enade (Faixa)': 'CONCEITO_ENADE_FAIXA'}
            if i == 2018:
                path = 'indices/2018/conceito_enade_2018.xlsx'
                variables_to_consider = ['Ano','Código da IES','Código do Curso','Conceito Enade (Faixa)']
            elif i == 2017:
                path = 'indices/2017/conceito_enade_2017.xlsx'
                variables_to_consider = ['Ano','Código da IES','Código do Curso','Conceito Enade (Faixa)']
            elif i == 2016:
                path = 'indices/2016/conceito_enade_2016.xlsx'
                variables_to_consider = ['Ano','Código da IES','Código do Curso','Conceito Enade (Faixa)']
            elif i == 2015:
                path = 'indices/2015/conceito_enade_2015.xls'
                variables_to_consider = ['Ano','Código da IES','Código do Curso','Conceito Enade Faixa)']

            #Reading database
            dataframe = self.reader(path, 'excel')
            dataframe = dataframe[variables_to_consider]

            #Renaming variables
            dataframe.rename(columns=variables_to_rename, inplace = True)

            #Adding data read in the iteration to the final dataframe
            if i == 2018:
                final_dataframe = dataframe
            else:
                final_dataframe = final_dataframe.append(dataframe, ignore_index = True)

        #Performing necessary operations for final dataframe
        final_dataframe = final_dataframe.astype({'ANO_CONCEITO_ENADE': 'int32'})
        final_dataframe = final_dataframe.sort_values(by = 'ANO_CONCEITO_ENADE', ascending = False)
        final_dataframe.drop_duplicates(subset = ['CODIGO_IES', 'CODIGO_CURSO'], ignore_index = True, inplace = True)

        #Writing final dataframe data
        self.writer(final_dataframe, 'conceito_enade_novo_metodo.csv')

        #Analyzing final dataframe data
        self.analyzer(final_dataframe, 'CONCEITO ENADE', 'conceito_enade_novo_metodo.html')

    def database_maker(self):
        #Reading the ENADE database
        enade_dataframe = self.reader('enade_novo_metodo.csv', 'csv', ',')

        #Reading the IES database
        ies_dataframe = self.reader('ies_novo_metodo.csv', 'csv', ',')

        #Reading the IGC database
        igc_dataframe = self.reader('igc_novo_metodo.csv', 'csv', ',')

        #Reading the CPC database
        cpc_dataframe = self.reader('cpc_novo_metodo.csv', 'csv', ',')

        #Reading the CONCEITO ENADE database
        conceito_enade_dataframe = self.reader('conceito_enade_novo_metodo.csv', 'csv', ',')

        #Joining all the databases read to form the final database
        final_dataframe = enade_dataframe.join(ies_dataframe.set_index('CODIGO_IES'), on='CODIGO_IES')
        final_dataframe = final_dataframe.join(igc_dataframe.set_index('CODIGO_IES'), on='CODIGO_IES')
        final_dataframe = final_dataframe.join(cpc_dataframe.set_index(['CODIGO_IES','CODIGO_CURSO']), on=['CODIGO_IES','CODIGO_CURSO'])
        final_dataframe = final_dataframe.join(conceito_enade_dataframe.set_index(['CODIGO_IES','CODIGO_CURSO']), on=['CODIGO_IES','CODIGO_CURSO'])

        #Writing final database
        self.writer(final_dataframe, 'base_final_novo_metodo.csv')

        #Analyzing final database
        self.analyzer(final_dataframe, 'BASE FINAL', 'base_final_novo_metodo.html')

manager = Manager()
