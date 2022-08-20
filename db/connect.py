import sqlite3
import pandas
import psycopg2
import psycopg2.extras
from db.config import config
from core.utils import CustomLogger

log = CustomLogger()

def connect_start():
    """ Connect to the PostgreSQL database server """
    log.info('connect_start :: Connecting to the PostgreSQL database')
    conn = None
    try:
        # read connection parameters
        params = config(filename='./db/database.ini', section="profile_saurav")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        if db_version:
            log.info('connect_start :: Connection Established - {}'.format(db_version))
            cur.close()
            return conn
        raise Exception
    except (Exception, psycopg2.DatabaseError) as error:
        log.error('connect_error :: Failed to Establish Connection :: {}'.format(error))

def connect_end(conn):
    """ Close Connection """
    try:
        conn.close()
        log.info('connect_end :: Connection Closed')
    except Exception as error:
        log.error('connect_end :: Failed to Close Connection :: {}'.format(error))

def is_existing_table(conn, table: str) -> bool:
    TABLE_EXISTS_QUERY = """
        SELECT EXISTS (
            SELECT FROM 
                pg_tables
            WHERE 
                tablename  = '{}'
        );
    """
    cur = conn.cursor()
    cur.execute(TABLE_EXISTS_QUERY.format(table))
    row = cur.fetchone()
    cur.close()
    if row[0]:
        log.info(f"is_existing_table :: {table} :: True")
        return True
    log.info(f"is_existing_table :: {table} :: False")
    return False

def create_table(conn, table, columns):
    cur = conn.cursor()
    CREATE_QUERY = """
        CREATE TABLE {table} ({columns});
    """
    for i in range(len(columns)):
        columns[i] = columns[i] + " varchar(255)"
    columns_ddl: str = ', '.join(columns)
    cur.execute(CREATE_QUERY.format(table = table, columns = columns_ddl))
    cur.close()
    log.info(f"create_table :: {table} created")

def prep(i):
    i = i.replace('\"','')
    return i.replace("\'",'\"')

def prep_dataframe(df: pandas.DataFrame, prep_columns: list):
    for i in df.columns:
        df[i] = df[i].astype(str)
    for col in prep_columns:
        df[col] = df[col].apply(prep)
    return df

def insert_into_table_from_dataframe(conn, df: pandas.DataFrame, table: str, prep_columns: list = []):
    log.start("insert_into_table_from_dataframe")
    cur = conn.cursor()
    df = prep_dataframe(df, prep_columns)
    INSERT_QUERY = """
        INSERT INTO {table} ({columns}) 
        VALUES {values};
    """
    columns = ', '.join(df.columns)
    values: list = []
    for row in df.values:
        values.append(str(tuple(row)))
    values = ','.join(values)
    log.info(f"insert_into_table_from_dataframe :: inserting data for {table}...")
    cur.execute(INSERT_QUERY.format(table = table, columns = columns, values = values))
    cur.close()
    log.end("insert_into_table_from_dataframe")



if __name__ == '__main__':
    pass