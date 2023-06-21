# Docker-Kubernetes-Assignment

## Docker Task:

* In this task, a DAG is created to add the current time to a table in each run. The DAG uses the PostgresOperator from the Airflow provider for PostgreSQL to perform the necessary database operations. The code imports the required modules and defines the tasks for creating the table and inserting the current time value.

#### 1. Create table task:

```

creating_table = PostgresOperator(
        task_id='creating_table',
        postgres_conn_id='postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS myTime (
                curr_time TIMESTAMP
            );
        '''
    )

```

This task creates a table named "myTime" if it does not already exist. The PostgresOperator is used with the specified task ID and PostgreSQL connection ID. The SQL code within the task creates the table with a single column "curr_time" of type TIMESTAMP.

#### 2. Insert values task:

```
inserting_values = PostgresOperator(
        task_id = 'inserting_values',
        postgres_conn_id='postgres',
        sql = '''
                INSERT INTO myTime VALUES (CURRENT_TIMESTAMP);   
        '''
    )

```
This task inserts the current timestamp into the "myTime" table. Similar to the previous task, it uses the PostgresOperator with the task ID and PostgreSQL connection ID. The SQL code within the task inserts the value of CURRENT_TIMESTAMP into the "myTime" table.


#### 3. Dependencies:

```
creating_table >> inserting_values

```

#### 4. Dag in airflow:

<img width="1440" alt="Screenshot 2023-06-19 at 6 58 31 PM" src="https://github.com/Sonali-Gudey/Docker-Kubernetes-Assignment/assets/123619701/814f0197-724a-495a-8d6c-0574faea0267">


#### 5. Entries in the table:

<img width="264" alt="Screenshot 2023-06-19 at 7 02 25 PM" src="https://github.com/Sonali-Gudey/Docker-Kubernetes-Assignment/assets/123619701/28263f39-0954-47ef-aa7f-50c26cee56fe">



## Kubernetes Task:

To complete the Kubernetes task, the following steps were performed:

1. Installed Minikube by executing the command brew install minikube and started the Kubernetes cluster using minikube start.

2. Created a pod with a Postgres container by applying the postgres-deployment.yaml file using the command kubectl apply -f postgres-deployment.yaml. To establish a connection between Postgres and Airflow, the necessary dependencies were installed in the Postgres container. Access to the Postgres container's terminal was obtained by running the commands:

```

minikube ssh
docker exec -it -u root postgres-container-id /bin/bash

```

3. Inside the Postgres container's terminal, the required dependencies were installed by executing the following commands:

```
apt-get -y update
apt-get -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget 
wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tgz
tar -xf Python-3.7.12.tgz
cd /Python-3.7.12
./configure --enable-optimizations
make -j $(nproc)
make altinstall

```
4. Airflow version 2.5.0 was installed within the Postgres container by executing the following commands:

```
apt-get install libpq-dev
pip3.7 install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"
export AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql://airflow:airflow@localhost:5432/airflow
```

5. The Airflow database was initialized using airflow db init. An Airflow user with administrative privileges was created using the command airflow users create -u airflow -p airflow -f <fname> -l <lname> -e <mail> -r Admin.

6. A clusterIP service was created to provide access to the Postgres pods within the cluster. The postgres-service.yaml file was applied using the command kubectl apply -f postgres-service.yaml.

7. A pod with an Airflow container was created by applying the airflow-deployment.yaml file using the command kubectl apply -f airflow-deployment.yaml.

8. For creating DAGs and tasks in the Airflow scheduler, the following steps were performed:

-  Accessed the Airflow scheduler container's terminal by running minikube ssh and then executing docker exec -it -u root airflow-scheduler-id /bin/bash.
  
- Navigated to the dags directory and installed Vim text editor using the commands:
  
```
  apt-get update
  apt install vim
```
  
- Created a DAG file, time_task.py, using the Vim editor and wrote the necessary DAG content.
9. Finally, the Airflow webserver was accessed by running the command minikube service airflow. The Airflow web interface was accessed through the provided URL. 
10. After logging in, the DAG was visible, and a Postgres connection was created. The DAG was then executed successfully.
  
<img width="554" alt="Screenshot 2023-06-20 at 6 58 16 PM" src="https://github.com/Sonali-Gudey/Docker-Kubernetes-Assignment/assets/123619701/b92ad570-dd4d-404e-81cf-c9dd150f3488">

#### Dag in airflow:

<img width="1176" alt="Screenshot 2023-06-20 at 7 02 35 PM" src="https://github.com/Sonali-Gudey/Docker-Kubernetes-Assignment/assets/123619701/4fc31029-1a03-4898-bfd8-73e6a203ad94">

#### Validation of entry:

<img width="262" alt="Screenshot 2023-06-20 at 7 15 10 PM" src="https://github.com/Sonali-Gudey/Docker-Kubernetes-Assignment/assets/123619701/7045edf5-0d77-418a-8d68-50e22416df7b">

