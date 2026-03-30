import pandas as pd
def criar_metricas(df):
    df["ano"] = df["timestamp"].dt.year
    df["mes"] = df["timestamp"].dt.month

    df_consolidado = df.groupby("course_name").agg(
        total_alunos=("student_id", "nunique"),
        frequencia_media=("attendance_rate", "mean"),
        desempenho_medio=("grade_point_average", "mean")
    ).reset_index()

    return df_consolidado


def tabelas_intermediarias_matricula(df):
# tabela de matrícula
    df_matricula = df[[
    "student_id",
    "course_name",
    "enrollment_status",
    "timestamp"
]].drop_duplicates()
    return df_matricula

def tabelas_intermediarias_frequencia(df):
# tabela de frequencia
    df_frequencia = df[[
    "student_id",
    "course_name",
    "attendance_rate"
]].drop_duplicates()
    
    return df_frequencia
def tabelas_intermediarias_desempenho(df):
# tabela de desempenho
    df_desempenho = df[[
    "student_id",
    "course_name",
    "grade_point_average"
]].drop_duplicates()
    return df_desempenho


