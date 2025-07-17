import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_conn_test",
    schedule=None, # 분, 시, 일, 월, 요일 
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), #덱이 언제부터 돌지 
    catchup=False, #누락되었던 구간을 돌릴 것인지? 1/1에 올리고 시작을 3/1에 한다면 그 두달을 돌릴 것인지
    tags=["example", "example2", "example3"],
) as dag: 
    t1 = EmptyOperator(
        task_id="t1")
    
    t2 = EmptyOperator(
        task_id="t2")
    
    t3 = EmptyOperator(
        task_id="t3")
    
    t4 = EmptyOperator(
        task_id="t4")
    
    t5 = EmptyOperator(
        task_id="t5")
    
    t6 = EmptyOperator(
        task_id="t6")
    
    t7 = EmptyOperator(
        task_id="t7")
    
    t8 = EmptyOperator(  
        task_id="t8")
    
    t9 = EmptyOperator(
        task_id="t9")
    
    t1 >> [t2, t3] >> t4
    t5 >> t4
    [t4,t7] >>t6 >> t8 >> t9