from pathlib import Path
from src.ingestao import carregar_dados
from src.limpeza import limpar_dados
from src.transformacao import criar_metricas, tabelas_intermediarias_frequencia, tabelas_intermediarias_matricula, tabelas_intermediarias_desempenho
DATA_PATH = Path("data")
#C:\Users\david\OneDrive\Documents\46 - Portifolio\01 - Engenharia de dados\data
def main():

    from pathlib import Path

    print("Procurando em:", DATA_PATH.resolve())
    print("Arquivos encontrados:", list(DATA_PATH.glob("*")))


    arquivos = list(DATA_PATH.glob("dataset_*.csv"))

    if not arquivos:
        raise FileNotFoundError(f"Nenhum dataset encontrado em {DATA_PATH.resolve()}")

    arquivo = max(arquivos, key=lambda x: x.stat().st_mtime)

    print(f"Usando arquivo: {arquivo}")
    

    df = carregar_dados(arquivo)
    df = limpar_dados(df)
    df_final = criar_metricas(df)
    df_matricula = tabelas_intermediarias_matricula(df)
    df_frequencia = tabelas_intermediarias_frequencia(df)
    df_desempenho = tabelas_intermediarias_desempenho(df)

    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent

    OUTPUT_PATH = BASE_DIR / "output"
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    df_final.to_parquet(OUTPUT_PATH / "consolidado.parquet", index=False)

    df_matricula.to_parquet(OUTPUT_PATH / "matricula.parquet", index=False)
    df_frequencia.to_parquet(OUTPUT_PATH / "frequencia.parquet", index=False)
    df_desempenho.to_parquet(OUTPUT_PATH / "desempenho.parquet", index=False)



    print("Pipeline executado com sucesso!")

if __name__ == "__main__":
    main()