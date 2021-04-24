https://predictivehacks.com/how-to-run-your-first-airflow-dag-in-docker/


ubutu
---
/lib/systemd/system/docker.service

ExecStart=/usr/bin/dockerd -H 0.0.0.0:2375 -H fd:// --containerd=/run/containerd/containerd.sock


systemctl daemon-reload

systemctl restart docker

-------------------------
airflow.cfg
-----
enable_xcom_pickling = True

OR
docker-compose.yaml
----

Worked for me too. I use it with docker-compose so had to add environment variable:
AIRFLOW__CORE__ENABLE_XCOM_PICKLING: 'true'

--------------------------


.kube directory
----
copy /home/vagrant/.kube/config ( on the kubernetes master) to this directory


docker context create k8s-test --default-stack-orchestrator=kubernetes --kubernetes config-file=/Users/kadirsahan/PycharmProjects/airflowProject/.kube/config --docker host=unix:///var/run/docker.sock




