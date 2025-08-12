import pendulum

from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG, chain
import random 
from common.common_func import get_sftp  # Importing the function from common_func.py
#plugins를 쓰면 안됨. 
with DAG(
    dag_id="dags_python_import_func",
    schedule="30 6 * * *", # 분, 시, 일, 월, 요일 
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), #덱이 언제부터 돌지 
    catchup=False, #누락되었던 구간을 돌릴 것인지? 1/1에 올리고 시작을 3/1에 한다면 그 두달을 돌릴 것인지
   
) as dag: 
   
    
    task_get_sftp = PythonOperator(
        task_id="task_get_sftp",
        python_callable=get_sftp # 어떤 함수를 실행시킬것인지
    )

    task_get_sftp