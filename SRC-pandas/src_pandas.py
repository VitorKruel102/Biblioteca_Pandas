import numpy
import pandas as pd


def Dataframe_dict():

    df_registros = pd.DataFrame(
        {
            "NOME": [
                'Vitor Kruel',
                'John Bruno',
                'Paulo Ricardo'
            ],
            "IDADE": [
                21,
                29,
                47
            ],
            "M/F": [
                "M",
                "M",
                "M"
            ]
        }
    )

    # . . .

    print(df_registros["NOME"])


def creade_series():
    # Series com LISTAS:
    print(pd.Series([1, 2, 3, 4, 5, 6], name='Numeros'))

    # Series com DICIONARIOS:
    print(pd.Series({'A': 2, 'B': 3, 'C': 4}))

    # Series com Arrays:
    A = pd.Series(numpy.array(range(5)))
    print(numpy.mean(A))


def max_min_dataframa():

    A = pd.Series(numpy.array(range(5)))
    print(f'Valor maximo: {A.max()}. Valor Minimo: {A.min()}')


def estatistica_coluna():

    col = pd.Series({'A': 1, 'B': 2, 'C': 3})
    col2 = pd.Series({'A': 4, 'B': 5, 'C': 6})
    file_table = pd.DataFrame((col, col2))

    print(file_table['A'].describe().T)
    print(file_table['A'].describe(
        percentiles=[
            0.1, 0.2, 0.8, 0.9
        ]
    ).T)


def ler_limite_linhas():

    A = pd.Series(numpy.array(range(1000)))
    print(A.head(10))
    print(A.tail(10))

def series_types():
    # Informa o tipo da Series:
    A = pd.Series(numpy.array(range(5)))
    print(A.dtypes)


def columns_names():
    # Informa o nomes das colunas:
    col = pd.Series({'A': 1, 'B': 2, 'C': 3})
    col2 = pd.Series({'A': 4, 'B': 5, 'C': 6})
    file_table = pd.DataFrame((col, col2))
    print(file_table.columns)


def creade_dataframe():
    # Informa o cria uma tabela através de listas:
    """
        SE CRIAR UMA TABELA COM LISTAS, O PANDAS VAI
        CONSIDERAR QUE CADA LISTA É UMA LINHA.
    """
    col = pd.Series([1, 2, 3, 4, 5, 6], name='Numeros')
    col2 = pd.Series([1, 2, 3, 4, 5, 6], name='Numeros2')
    file_table = pd.DataFrame((col, col2))
    print(file_table)

    # Informa o cria uma tabela através de dicionario:
    """
        SE CRIAR UMA TABELA COM DICIONATIO, O PANDAS VAI
        CONSIDERAR QUE SÃO COLUNAS.
    """
    col = pd.Series({'A': 1, 'B': 2, 'C': 3})
    col2 = pd.Series({'A': 4, 'B': 5, 'C': 6})
    file_table = pd.DataFrame((col, col2))
    print(file_table)


def insert_coluna():
    #  Criar colunar:
    col = pd.Series({'A': 1, 'B': 2, 'C': 3})
    col2 = pd.Series({'A': 4, 'B': 5, 'C': 6})
    file_table = pd.DataFrame((col, col2))
    file_table['NOVA'] = 1
    print(file_table)

    #  insert coluna no indice especifico:
    col = pd.Series({'A': 1, 'B': 2, 'C': 3})
    col2 = pd.Series({'A': 4, 'B': 5, 'C': 6})
    file_table = pd.DataFrame((col, col2))
    # INSERIR(INDICE, NOME_COLUNA, VALORES)
    file_table.insert(1, 'ENTRE', '<>')
    print(file_table)
    del file_table['ENTRE']  # DELETAR
    print(file_table)


def rename_coluna():
    #  Criar colunar:
    col = pd.Series({'A': 1, 'B': 2, 'C': 3})
    col2 = pd.Series({'A': 4, 'B': 5, 'C': 6})
    file_table = pd.DataFrame((col, col2))
    file_table['NOVA'] = 1

    colunas = {'A': 'ANO', 'B': 'ANO1', 'C': 'ANO2'}

    file_table.rename(columns=colunas, inplace=True)
    print(file_table)


def iloc_pandas():

    col = pd.Series({'A': 1, 'B': 2, 'C': 3})
    col2 = pd.Series({'A': 4, 'B': 5, 'C': 6})
    file_table = pd.DataFrame((col, col2))
    file_table['NOVA'] = 1

    print(file_table.iloc[0:1, 0:2])  # iloc(linhas, colunas)


def filtro_coluna():

    col = pd.Series({'A': 1, 'B': 2, 'C': 3})
    col2 = pd.Series({'A': 4, 'B': 5, 'C': 6})
    file_table = pd.DataFrame((col, col2))
    file_table['NOVA'] = 1

    um_e_dois = file_table[(file_table['A'] == 4) & (file_table['B'] == 5)]
    um_ou_dois = file_table[(file_table['A'] == 4) | (file_table['B'] == 5)]

    print(um_e_dois)
    print(um_ou_dois)


def info_dataframe():
    import os

    #  Criar coluna:
    col = pd.Series({'A': 1, 'B': 2, 'C': 3})
    col2 = pd.Series({'A': 4, 'B': 5, 'C': 6})
    file_table = pd.DataFrame((col, col2))
    print(file_table.info())

    describe_tabela = {

        'nomes_tabelas': ['A', 'B', 'C'],
        'Descricao': ['Abertura', 'Fechamento', 'Maxima'],
        'Tido_dados': ['Númerico', 'Númerico', 'Númerico'],
        'Tipo_numpy': ['int64', 'int64', 'int64']
    }
    describe_t = pd.DataFrame(describe_tabela)


def read_xlsx():

    df_arquivo_xlsx = pd.read_csv('arquivo.xlsx', sheet_name="planilha2")


def ordenar_columns():

    #  Criar coluna:
    col = pd.Series({'A': 1, 'B': 2, 'C': 3})
    col2 = pd.Series({'A': 4, 'B': 5, 'C': 6})
    file_table = pd.DataFrame((col, col2))
    print(file_table.sort_values(by='A'))


def eliminar_NULL():

    #  Criar coluna:
    col = pd.Series({'A': None, 'B': 2, 'C': 3})
    col2 = pd.Series({'A': 4, 'B': 5, 'C': 6})
    file_table = pd.DataFrame((col, col2))
    #  Elimina a linha com A == NULL:
    ARQUIVO = file_table[file_table['A'].notna()]
    print(ARQUIVO)
    

if __name__ == '__main__':

    eliminar_NULL()
