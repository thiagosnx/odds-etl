from extract import extract_matches_historic
from transform import transform
from load import load
import os

os.makedirs("db", exist_ok=True)

def run_etl():
    raw_matches = extract_matches_historic()

    if not raw_matches:
        print("Nenhum dado")
        return
    
    df_matches = transform(raw_matches)

    load(df_matches)



if __name__ == "__main__":
    run_etl()