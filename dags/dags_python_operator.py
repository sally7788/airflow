import pendulum

from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG, chain
import random 

with DAG(
    dag_id="dags_python_operator",
    schedule=None, # 분, 시, 일, 월, 요일 
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), #덱이 언제부터 돌지 
    catchup=False, #누락되었던 구간을 돌릴 것인지? 1/1에 올리고 시작을 3/1에 한다면 그 두달을 돌릴 것인지
   
) as dag: 
    def select_fruit():
        fruit=['apple', 'banana', 'orange', 'grape']
        rand_int = random.randint(0, 3) #0~3까지 임의의 값 리턴 
        print(fruit[rand_int]) #리스트에서 임의의 값 출력
    
    py_t1 = PythonOperator(
        task_id="py_t1",
        python_callable=select_fruit # 어떤 함수를 실행시킬것인지
    )
    
    py_t1