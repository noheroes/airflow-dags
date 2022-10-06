from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "ejecucion-airflow-1006181911",
}

dag = DAG(
    "ejecucion-airflow-1006181911",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.11.1 pipeline editor using `ejecucion-airflow.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: dummy-demo/3-ejecucion/2-ingesta/ingesta.py


op_7322580b_0254_4be1_b295_1ec28902f085 = KubernetesPodOperator(
    name="ingesta",
    namespace="airflow",
    image="noheroes/kfp:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'ejecucion-airflow' --cos-endpoint http://192.168.100.246 --cos-bucket storage --cos-directory 'pipelines/ejecucion-airflow-1006181911' --cos-dependencies-archive 'ingesta-7322580b-0254-4be1-b295-1ec28902f085.tar.gz' --file 'dummy-demo/3-ejecucion/2-ingesta/ingesta.py' "
    ],
    task_id="ingesta",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "kubeflow",
        "AWS_SECRET_ACCESS_KEY": "kubeflow123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "ejecucion-airflow-{{ ts_nodash }}",
    },
    resources={
        "request_cpu": "1",
        "request_memory": "2",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)


# Operator source: dummy-demo/3-ejecucion/3-preparacion/prepare.py


op_216ad1ea_ca07_4d64_a5f1_0826db8a0bd9 = KubernetesPodOperator(
    name="prepare",
    namespace="airflow",
    image="noheroes/kfp:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'ejecucion-airflow' --cos-endpoint http://192.168.100.246 --cos-bucket storage --cos-directory 'pipelines/ejecucion-airflow-1006181911' --cos-dependencies-archive 'prepare-216ad1ea-ca07-4d64-a5f1-0826db8a0bd9.tar.gz' --file 'dummy-demo/3-ejecucion/3-preparacion/prepare.py' "
    ],
    task_id="prepare",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "kubeflow",
        "AWS_SECRET_ACCESS_KEY": "kubeflow123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "ejecucion-airflow-{{ ts_nodash }}",
    },
    resources={
        "request_cpu": "1",
        "request_memory": "2",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_216ad1ea_ca07_4d64_a5f1_0826db8a0bd9 << op_7322580b_0254_4be1_b295_1ec28902f085


# Operator source: dummy-demo/3-ejecucion/4-scoring/scoring.py


op_fc5b6aae_3864_49db_b8f1_992396d0ce7f = KubernetesPodOperator(
    name="scoring",
    namespace="airflow",
    image="noheroes/kfp:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'ejecucion-airflow' --cos-endpoint http://192.168.100.246 --cos-bucket storage --cos-directory 'pipelines/ejecucion-airflow-1006181911' --cos-dependencies-archive 'scoring-fc5b6aae-3864-49db-b8f1-992396d0ce7f.tar.gz' --file 'dummy-demo/3-ejecucion/4-scoring/scoring.py' "
    ],
    task_id="scoring",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "kubeflow",
        "AWS_SECRET_ACCESS_KEY": "kubeflow123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "ejecucion-airflow-{{ ts_nodash }}",
    },
    resources={
        "request_cpu": "1",
        "request_memory": "2",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_fc5b6aae_3864_49db_b8f1_992396d0ce7f << op_216ad1ea_ca07_4d64_a5f1_0826db8a0bd9


# Operator source: dummy-demo/3-ejecucion/5-salida/salida.py


op_4455554a_e4b3_4fed_b24a_0c662ec6570b = KubernetesPodOperator(
    name="salida",
    namespace="airflow",
    image="noheroes/kfp:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.11.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'ejecucion-airflow' --cos-endpoint http://192.168.100.246 --cos-bucket storage --cos-directory 'pipelines/ejecucion-airflow-1006181911' --cos-dependencies-archive 'salida-4455554a-e4b3-4fed-b24a-0c662ec6570b.tar.gz' --file 'dummy-demo/3-ejecucion/5-salida/salida.py' "
    ],
    task_id="salida",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "kubeflow",
        "AWS_SECRET_ACCESS_KEY": "kubeflow123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "ejecucion-airflow-{{ ts_nodash }}",
    },
    resources={
        "request_cpu": "1",
        "request_memory": "2",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_4455554a_e4b3_4fed_b24a_0c662ec6570b << op_fc5b6aae_3864_49db_b8f1_992396d0ce7f
