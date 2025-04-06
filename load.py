import sqlite3

def load(df, db_path="db/matches.db"):
    conn = sqlite3.connect(db_path)

    create_table_sql = """
        CREATE TABLE IF NOT EXISTS matches (
            match_id INTEGER PRIMARY KEY,
            utc_date TEXT,
            status TEXT,
            home_team TEXT,
            away_team TEXT,
            score_home INTEGER,
            score_away INTEGER,
            winner TEXT
        )
    """
    conn.execute("DROP TABLE IF EXISTS matches")
    conn.execute(create_table_sql)

    df.to_sql("matches", conn, if_exists="append", index=False)

    dedup_sql = """
        DELETE FROM matches
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM matches
            GROUP BY match_id
        )
    """

    conn.execute(dedup_sql)

    conn.commit()
    conn.close()