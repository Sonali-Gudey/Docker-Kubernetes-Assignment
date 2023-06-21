from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator



with DAG(dag_id='time_tracking', start_date=datetime(2022, 1, 1), 
        schedule_interval='@daily',  catchup=False) as dag:

    creating_table = PostgresOperator(
        task_id='creating_table',
        postgres_conn_id='postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS myTime (
                curr_time TIMESTAMP
            );
        '''
    )
    
    inserting_values = PostgresOperator(
        task_id = 'inserting_values',
        postgres_conn_id='postgres',
        sql = '''
                INSERT INTO myTime VALUES (CURRENT_TIMESTAMP);   
        '''
    )
    
    creating_table >> inserting_values