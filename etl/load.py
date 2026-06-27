from sqlalchemy import create_engine

host = ''
port = 5432
user = 'postgres'
password = ''
db_name = ''

def load_to_postgres(df, table_name):
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

    df.to_sql(table_name,
              engine,
              schema='etl_pipeline', 
              if_exists='replace',
              index=False)

    print('Data Loaded to postgres successfully')