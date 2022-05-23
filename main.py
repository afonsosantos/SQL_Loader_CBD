import os

TABLE_NAMES = [
    "AREA_ATUACAO", "CIRURGIA", "CONSULTA", "ENFERMEIRO", "ESTADO_PACIENTE", "FUNCIONARIO",
    "MEDICO", "MEDICO_CIRURGIA", "PACIENTE", "PESSOA", "PROCESSO", "RELATORIO", "TELEFONE",
    "TIPO_CIRURGIA", "USER_EXCEPTION", "ENCRYPTION_KEY"]

COLUMN_NAMES = [
    ["id_area_atuacao", "descricao"],
    ["id_cirurgia", "id_processo", "id_relatorio", "id_tipo_cirurgia", "dta_realizacao DATE 'YY.MM.DD'"],
    ["id_consulta", "id_processo", "nif_funcionario", "id_relatorio", "id_estado_paciente", "dta_realizacao DATE 'YY.MM.DD'"],
    ["nif"],
    ["id_estado_paciente", "descricao"],
    ["nif"],
    ["nif", "id_area_atuacao", "cedula"],
    ["nif", "id_cirurgia"],
    ["nif", "n_utente_saude"],
    ["nif", "prim_nome", "ult_nome", "morada", "dta_nasc DATE 'YY.MM.DD'"],
    ["id_processo", "nif", "id_area_atuacao", "id_estado_paciente", "dta_inicio DATE 'YY.MM.DD'", "dta_alta DATE 'YY.MM.DD' NULLIF dta_alta = 'NULL'"],
    ["id_relatorio", "nif", "texto", "categoria"],
    ["nif", "telefone"],
    ["id_tipo_cirurgia", "id_area_atuacao", "nome"],
    ["code", "name", "errm"],
    ["key"]
]

BASE_CTL_FILE = """load data into table {0}
append
fields terminated by ","
(
{1}
)
"""

BASE_PAR_FILE = """userid=PROJETO/Projeto_22
control={0}.ctl
data=../csv_data/{1}.csv
direct=false
"""


def write_to_file(content: str, file_name: str):
    if not os.path.exists(file_name):
        f = open(file_name, "w")
        f.write(content)
        f.close()


def write_table_file(content: str, extension: str, table_name: str):
    current_path = os.path.join(os.path.abspath(os.getcwd()), table_name.lower())

    if not os.path.exists(current_path):
        os.mkdir(current_path)

    file_name = os.path.join(current_path, table_name.lower() + extension)
    write_to_file(content, file_name)


def main():
    for table_name, column_name in zip(TABLE_NAMES, COLUMN_NAMES):
        print("> Creating files for: ", table_name)
        print("\t- Columns: ", column_name)

        current_table_columns = ", ".join(column_name)

        current_ctl_file = BASE_CTL_FILE.format(table_name, current_table_columns)
        current_par_file = BASE_PAR_FILE.format(table_name.lower(), table_name.lower() + "_data_table")

        write_table_file(current_par_file, ".par", table_name)
        write_table_file(current_ctl_file, ".ctl", table_name)

        print("\t- Files created!", "\n")


if __name__ == "__main__":
    main()
