"""
This file implements utils for processing the data files on this repository.
"""

from pandas import read_csv
from pandas import concat


def readTable1_1():
    filename = "./Tabela 1.1 (UF).csv"
    csv_data = read_csv(
        filepath_or_buffer=filename,
        header=2,
        skipfooter=3,
        skiprows=[3],
        engine="python",
        index_col=0,
    )
    csv_data.columns = [
        "total_regions",
        "cv_regions",
        "percent_branca",
        "cv_branca",
        "percent_negra",
        "cv_negra",
        "percent_parda",
        "cv_parda",
        "percent_amarela_indigena",
        "cv_amarela_indigena",
    ]
    return csv_data


def readTable3_4():
    filename = "./Tabela 3.4.csv"
    csv_data = read_csv(
        filepath_or_buffer=filename,
        header=4,
        skipfooter=5,
        skiprows=[3],
        engine="python",
        index_col=0,
    )
    csv_data.columns = [
        "total_pci",
        "cv_total_pci",
        "branca_pci",
        "cv_branca_pci",
        "preta_pci",
        "cv_preta_parda_pci",
        "homens_pci",
        "cv_homens_pci",
        "homens_branca_pci",
        "cv_homens_branca_pci",
        "homens_preta_parda_pci",
        "cv_homens_preta_parda_pci",
        "mulheres_pci",
        "cv_mulheres_pci",
        "mulheres_branca_pci",
        "cv_mulheres_branca_pci",
        "mulheres_preta_parda_pci",
        "cv_mulheres_preta_parda_pci",
        "preta_parda/branca",
        "cv_preta_parda/branca",
        "homens_preta_parda/branca",
        "cv_homens_preta_parda/branca",
        "mulheres_branca/homens_branca",
        "cv_mulheres_branca/homens_branca",
        "mulheres_preta_parda/homens_branca",
        "cv_mulheres_preta_parda/homens_branca",
    ]
    return csv_data


def readTable3_5():
    filename = "./Tabela 3.5.csv"
    csv_data_total = read_csv(
        filepath_or_buffer=filename,
        header=4,
        skiprows=[5],
        nrows=6,
        engine="python",
        index_col=0,
    )
    csv_data_total.columns = [
        "absolute",
        "cv_absolute",
        "proportion_falta_coleta_lixo",
        "cv_proportion_falta_coleta_lixo",
        "proportion_falta_abastecimento_agua",
        "cv_proportion_falta_abastecimento_agua",
        "proportion_falta_saneamento",
        "cv_proportion_falta_saneamento",
        "proportion_qualquer_deficiencia",
        "cv_proportion_qualquer_deficiencia",
    ]
    csv_data_branca = read_csv(
        filepath_or_buffer=filename,
        header=12,
        nrows=6,
        engine="python",
        index_col=0,
    )
    csv_data_branca.columns = [
        "absolute_branca",
        "cv_absolute_branca",
        "proportion_falta_coleta_lixo_branca",
        "cv_proportion_falta_coleta_lixo_branca",
        "proportion_falta_abastecimento_agua_branca",
        "cv_proportion_falta_abastecimento_agua_branca",
        "proportion_falta_saneamento_branca",
        "cv_proportion_falta_saneamento_branca",
        "proportion_qualquer_deficiencia_branca",
        "cv_proportion_qualquer_deficiencia_branca",
    ]
    csv_data_preta_parda = read_csv(
        filepath_or_buffer=filename,
        header=19,
        nrows=6,
        engine="python",
        index_col=0,
    )
    csv_data_preta_parda.columns = [
        "absolute_preta_parda",
        "cv_absolute_preta_parda",
        "proportion_falta_coleta_lixo_preta_parda",
        "cv_proportion_falta_coleta_lixo_preta_parda",
        "proportion_falta_abastecimento_agua_preta_parda",
        "cv_proportion_falta_abastecimento_agua_preta_parda",
        "proportion_falta_saneamento_preta_parda",
        "cv_proportion_falta_saneamento_preta_parda",
        "proportion_qualquer_deficiencia_preta_parda",
        "cv_proportion_qualquer_deficiencia_preta_parda",
    ]
    csv_data = concat(
        [csv_data_total, csv_data_branca, csv_data_preta_parda], axis=1
    )
    return csv_data


def readTable3_6():
    filename = "./Tabela 3.6.csv"
    csv_data = read_csv(
        filepath_or_buffer=filename,
        header=4,
        skiprows=[5],
        nrows=6,
        engine="python",
        index_col=0,
    )
    return csv_data


if __name__ == "__main__":
    print(readTable1_1())
    print(readTable3_4())
    print(readTable3_5())
