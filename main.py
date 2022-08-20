from logging import exception
from msilib.schema import CustomAction
from fpl.main import get_all_data
from core.utils import CustomLogger
from db.connect import connect_start, connect_end, create_table, insert_into_table_from_dataframe, is_existing_table
from db.events import EventsContext
import pandas as pd
import traceback
import yaml

log = CustomLogger()

if __name__ == '__main__':
    log.info("main :: Starting FPL Predictor")
    try:
        # Fetch Data
        resp = get_all_data()
        # print(resp['elements'])
        # raise exception

        # Read Config File
        with open('configuration.yml') as f:
            config = yaml.safe_load(f)

        # Save to DB
        conn = connect_start()
        for table in config:
            log.info("main :: Saving Data For {}".format(table))
            table_columns = config[table]['columns']
            try:
                prep_columns = config[table]['prep_columns']
            except:
                prep_columns = []
            _df = pd.DataFrame(resp[table], columns=table_columns)
            if not is_existing_table(conn, table):
                create_table(conn, table, table_columns)
            insert_into_table_from_dataframe(conn, _df, table, prep_columns)

        conn.commit()
        connect_end(conn)

    except Exception as e:
        print('\n\n\n\nError Occured :: Stopping Code :: {}'.format(e))
        print(traceback.format_exc())
        
