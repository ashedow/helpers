# from pendulum import datetime
# from pendulum.time import timedelta
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

WORKFLOW_DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 4, 5),
    'email': ['test@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}
config = {
   'dag_id_1': {
       'schedule_interval': '',
       'start_date': datetime(2021, 4, 5),
       'table_name': 'table_name_1'
    },
   'dag_id_2': {
       'schedule_interval': '',
       'start_date': datetime(2021, 4, 5),
       'table_name': 'table_name_2'
    },
   'dag_id_3':{
       'schedule_interval': '',
       'start_date': datetime(2021, 4, 5),
       'table_name': 'table_name_3'
    }
}

def print_logs(**op_kwargs):
    print(f'{op_kwargs.get("dag_id", None)} start processing tables in database: {op_kwargs.get("database", None)}.')

# def push_function(context):
#     value = context['task_instance'].xcom_push(key='run', value='{{ run_id }} ended')
#     return value

# def skip_or_create_table():
#     if check_table_exist("SELECT * FROM pg_tables;",
#                          "SELECT * FROM information_schema.tables "
#                          "WHERE table_schema = '{}' "
#                          "AND table_name = '{}';", 'airflow_table'):
#         return 'skip_table_creation'
#     else:
#         return 'create_table'

def check_table_exists():
	if True:
		return 'insert_new_row'
	return 'create_table'


# with DAG('gridu_dag', default_args=default_args, schedule_interval='@hourly') as dag:
#     log_info = PythonOperator(task_id='log_info', python_callable=print_logs,
#                               op_kwargs={'dag_id': dag.dag_id, 'database': 'db_name'})
#     insert_new_row = DummyOperator(task_id='insert_new_row')
#     query_the_table = DummyOperator(task_id='query_the_table')
#     run_ended_flag = PythonOperator(task_id='run_ended_flag', python_callable=push_function)

    # log_info >> insert_new_row >> query_the_table >> run_ended_flag

for dict in config:
	with DAG(dict, default_args=config[dict]) as dag:
		task1 = PythonOperator(task_id='print_info', python_callable=print_logs, op_kwargs={'dag_id': dict, 'database': 'db_test'})
		task2 = DummyOperator(task_id='insert_new_row')
		task3 = DummyOperator(task_id='query_the_table')
		dag >> task1 >> task2 >> task3

# for dict in config:
# 	with DAG(dict, default_args=config[dict]) as dag:
# 		print_task = PythonOperator(task_id='print_process_start', python_callable=print_logs, op_kwargs={'dag_id':dict, 'database': 'db_test'})
# 		get_user = BashOperator(task_id='get_current_user', bash_command='whoami')
# 		branch_task = BranchPythonOperator(task_id='check_table_exists', python_callable=check_table_exists)
# 		create_table_task = DummyOperator(task_id='create_table')
# 		insert_task = DummyOperator(task_id='insert_new_row', trigger_rule='none_failed')
# 		query_task = DummyOperator(task_id='query_the_table')

# 		dag >> print_task >> get_user >> branch_task >> [create_table_task, insert_task]
# 		create_table_task >> insert_task
# 		insert_task >> query_task
# 		globals()[dict] = dag
