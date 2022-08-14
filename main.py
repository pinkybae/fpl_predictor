from msilib.schema import CustomAction
from fpl.main import get_all_data
from core.utils import CustomLogger
from db.connect import connect_start, connect_end, create_table, insert_into_table_from_dataframe, is_existing_table
from db.events import EventsContext
import pandas as pd
import traceback

log = CustomLogger()

if __name__ == '__main__':
    log.info("Starting FPL Predictor")
    try:
        # Fetch Data
        resp = get_all_data()

        events = resp['events'][0]
        events_columns = list(events.keys())

        _df = pd.DataFrame(resp['events'], columns=events_columns)
        print(_df.iloc[0])

        # Save to DB
        conn = connect_start()
        
        if not is_existing_table(conn, "events"):
            create_table(conn, "events", events_columns)
        insert_into_table_from_dataframe(conn, _df, "events")

        conn.commit()
        connect_end(conn)

    except Exception as e:
        print('\n\n\n\nError Occured :: Stopping Code :: {}'.format(e))
        print(traceback.format_exc())
        
