## Shubham's Approach

### Docker Task:

The Docker task involves creating a DAG (Directed Acyclic Graph) in Airflow that adds the current time to a table at each run.
The DAG is created using the DAG class from the airflow module. It is configured with a specific dag_id, start_date, schedule_interval, and catchup settings.
Within the DAG, there are two tasks defined using the PostgresOperator from the airflow.providers.postgres.operators.postgres module.
The first task is named createtable_task, which creates a table named "EMP" in a PostgreSQL database using an SQL statement provided in the sql parameter of the PostgresOperator.
The second task is named populatetable_task, which inserts rows of data into the "EMP" table using another SQL statement provided in the sql parameter of the PostgresOperator.
The >> operator is used to set the dependencies between tasks, indicating that the createtable_task should be executed before the populatetable_task.


### Kubernetes Task:

The Kubernetes task involves deploying a PostgreSQL database and an Airflow container in a Kubernetes cluster using Minikube.
It begins by installing Minikube, starting the cluster, and then creating a pod containing the PostgreSQL container using the postgres-deployment.yaml file.
The PostgreSQL container is configured to have the necessary dependencies installed by running commands inside the container's terminal.
Next, a service of type ClusterIP is created using the postgres-service.yaml file to provide access to the PostgreSQL pods within the Kubernetes cluster.
Similarly, a pod containing the Airflow container is created using the airflow-deployment.yaml file.
The DAG file (time_task.py) is created within the Airflow container by accessing it through Minikube's SSH and running commands to open the container's terminal and create the file using Vim.
Finally, the Airflow web server is accessed using the minikube service airflow command, and the DAG is visible in the web interface. The PostgreSQL connection is created, and the DAG is executed successfully.


### Comparision:

We followed the similar approach for both of the tasks.
