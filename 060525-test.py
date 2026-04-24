from airflow.decorators import dag
from datetime import datetime
from workflows.airflow.providers.amazon.aws.operators.sagemaker_workflows \
    import NotebookOperator

###############################################################################
#
# Enter in your desired schedule as WORKFLOW_SCHEDULE.  Some options include:
#
# '@daily' (daily at midnight)
# '@hourly' (every hour, at the top of the hour)
# '30 */3 * * *' (a CRON string, run at minute 30 past every 3rd hour)
# '0 8 * * 1-5' (a CRON string, run every weekday at 8am)
#
###############################################################################

WORKFLOW_SCHEDULE = None

###############################################################################
#
# Enter in the path to your notebook as NOTEBOOK_PATH. Example:
# 'src/workflows/dags/mynotebook.ipynb'
#
###############################################################################

NOTEBOOK_PATH = 'src/workflows/dags/060425-test.ipynb'


default_args = {
    'owner': 'chinguyn',
}


@dag(
    dag_id='workflow-dd4qi1t',
    default_args=default_args,
    schedule_interval=WORKFLOW_SCHEDULE,
    start_date=datetime(2025, 6, 5),
    is_paused_upon_creation=False,
    tags=['Scheduling_bb_all_capabilities', 'chinguyn'],
    catchup=False
)
def single_notebook():
    def initial_notebook_task():
        notebook1 = NotebookOperator(
            task_id="initial",
            input_config={'input_path': NOTEBOOK_PATH, 'input_params': {}},
            output_config={'output_formats': ['NOTEBOOK']},
            wait_for_completion=True,
            poll_interval=5,
            compute={
                "instance_type": "ml.c5.xlarge",
                "image_details": {
                    "ecr_uri": "542918446943.dkr.ecr.us-west-2.amazonaws.com/sagemaker-distribution-embargoed-prod:2.2-reinvent2024-cpu"
                }
            }
        )
        return notebook1
    initial_notebook_task()


# comments
# comments
single_notebook = single_notebook()
