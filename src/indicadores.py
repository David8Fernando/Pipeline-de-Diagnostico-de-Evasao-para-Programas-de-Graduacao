import pandas as pd

def gerar_indicadores(df):

    # Regras de negócio
    df["compareceu"] = df["attendance_rate"] > 0
    df["aprovado"] = df["grade_point_average"] >= 6
    df["evasao_prevista"] = df["attendance_rate"] < 75

    indicadores = df.groupby("course_name").agg(
        total_alunos=("student_id", "nunique"),

        taxa_comparecimento=("compareceu", "mean"),
        taxa_aprovacao=("aprovado", "mean"),
        taxa_evasao_prevista=("evasao_prevista", "mean"),

        frequencia_media=("attendance_rate", "mean"),
        desempenho_medio=("grade_point_average", "mean"),
        bolsa_media=("scholarship_percent", "mean")

    ).reset_index()

    return indicadores