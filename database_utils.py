from sqlalchemy import create_engine
import yaml

class DatabaseConnector:
    @staticmethod
    def read_db_creds():
        with open('db_creds.yaml', 'r') as file:
            return yaml.safe_load(file)

    @staticmethod
    def init_db_engine():
        creds = DatabaseConnector.read_db_creds()
        engine = create_engine(
            f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        )
        return engine

    @staticmethod
    def list_db_tables(engine):
        return engine.table_names()

    @staticmethod
    def upload_to_db(engine, dataframe, table_name):
        dataframe.to_sql(table_name, con=engine, if_exists='replace', index=False)

