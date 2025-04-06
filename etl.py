from extract import extract_matches_historic
from transform import transform
from load import load
import os

os.makedirs("db", exist_ok=True)

def run_etl():
    print("Obtendo dados da API...")
    raw_matches = extract_matches_historic()

    if not raw_matches:
        print("Nenhum dado")
        return
    
    print("Transformando dados...")
    
    df_matches = transform(raw_matches)

    print("Carregando dados na base...")

    load(df_matches)

    print("ETL feito com sucesso.")



if __name__ == "__main__":
    run_etl()