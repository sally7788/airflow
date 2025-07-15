import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain

with DAG(
    dag_id="dags_bash_operator",
    schedule=None, # 분, 시, 일, 월, 요일 
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), #덱이 언제부터 돌지 
    catchup=False, #누락되었던 구간을 돌릴 것인지? 1/1에 올리고 시작을 3/1에 한다면 그 두달을 돌릴 것인지
    tags=["example", "example2", "example3"],
) as dag: 
    bash_t1 = BashOperator(
        task_id="bash_t1", 
        bash_command="echo whoami",)
    
    bash_t2 = BashOperator(
        task_id="bash_t2", 
        bash_command="echo $HOSTNAME")

    bash_t1 >> bash_t2