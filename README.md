You may choose to run the container individually from the K8s by using:
docker run -d -p 80:80 ornaishtat/date-task

Kubernetes setup:
kubectl create -f deployment.yaml
kubectl create -f service-defenition.yaml

Test script:
pip install -r task_special_requirements.txt
python nginx_image_check.py


