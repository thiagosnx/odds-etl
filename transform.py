import pandas as pd

def transform(matches):
    df = pd.json_normalize(matches)

    df = df[[
        "id",
        "utcDate",
        "status",
        "homeTeam.name",
        "awayTeam.name",
        "score.fullTime.home",
        "score.fullTime.away",
    ]]

    df.columns = [
        "match_id",
        "utc_date",
        "status",
        "home_team",
        "away_team",
        "score_home",
        "score_away",
    ]

    return df