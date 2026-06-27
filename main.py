from etl.extract import extract_product, extract_users
from etl.transform import transform_product, transform_users
from etl.load import load_to_postgres

def run_pipeline():
    print('Starting Pipeline')

    product_df = extract_product()
    user_df = extract_users()

    print('Starting transformation')

    product_df = transform_product(product_df)
    user_df = transform_users(user_df)

    print('Loading to posgres')

    load_to_postgres(product_df, 'products')
    load_to_postgres(user_df, 'users')
    
    print('ETL pipeline complete')

if __name__ == '__main__':
    run_pipeline()