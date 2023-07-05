import pandas as pd
import sqlite3 as sq
work_dir="./"
table_name="game_analytics"
def create_table():
    conn = sq.connect(f"{work_dir}my_db.db")
    my_file = pd.read_parquet(f"{work_dir}4091418601468102007.parquet")
    my_file.to_sql(table_name,conn,if_exists='replace')

def daykretention(k):
    conn = sq.connect(f"{work_dir}my_db.db")
    cur = conn.cursor()
    day0user = int((cur.execute(f"Select Count(*) FROM (SELECT DISTINCT user_pseudo_id,days_elapsed FROM  '{table_name}' WHERE days_elapsed=0)").fetchone())[0])
    daykuser = int((cur.execute(f"Select Count(*) FROM (SELECT DISTINCT user_pseudo_id,days_elapsed FROM  '{table_name}' WHERE days_elapsed={k})").fetchone())[0])
    return daykuser/day0user*100


if __name__=="__main__":
    print(daykretention(6))