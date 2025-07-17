import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain
from airflow.utils.email import send_email

with DAG(
    dag_id="dags_email_operator",
    schedule="* 8 1 * *", # 분, 시, 일, 월, 요일 
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"), #덱이 언제부터 돌지 
    catchup=False, #누락되었던 구간을 돌릴 것인지? 1/1에 올리고 시작을 3/1에 한다면 그 두달을 돌릴 것인지
) as dag: 
    email_task = send_email(
        task_id="email_task",
        to="0702sally@naver.com",
        subject="에어플로우 성공메일 ",
        html_content="<h1>Hello from Airflow</h1>",
    )