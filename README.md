# Dice-Assignment-4
This Assignment is based on Kubernetes

### Minikube Installation
#### a. Use a virtualization platform (e.g., VirtualBox) if not already installed. You can use your host OS if you have Docker Desktop Installed.
I have installed docker desktop in my host machine. I am installing `minikube` using docker drivers.
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-arm64
sudo install minikube-linux-arm64 /usr/local/bin/minikube
```
![Screenshot from 2024-02-12 11-54-45](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/319b61e6-7d40-4e80-8363-83eac45acf8c)


#### b. Install Minikube by following the official installation instructions for your operating system.

I installed minikube on Ubuntu 22.04 I follow the following link for installation

```
https://minikube.sigs.k8s.io/docs/start/
```

#### c. Verify the installation by running basic Minikube commands and checking the version.

![image](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/39d48e24-d2a6-4b2f-99cd-78a9668fad7a)


![Screenshot from 2024-02-12 11-55-15](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/4c19b3b4-cb04-401c-80cd-74ec7c8bd87b)


### Deploying Applications:

#### a. Create a custom Docker image for the application, which displays the pod name. (Use any repo from GitHub having a Docker File)

In this part, I am using the Assignment-3 code with the Docker file.

![image](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/c6972b9f-101f-47c2-9f66-ffdd901d9d4d)

APP.py
```
from flask import Flask
import unittest

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

class TestApp(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_hello(self):
        response = self.tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

if __name__ == '__main__':
    # If the script is run directly, start the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
else:
    # If the script is imported, run the tests
    unittest.main()
```

Dockerfile
```
# Use the official Python image as a base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the application will run
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
```
then create build
```
docker build -t python-app:latest .
```
![image](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/af1d2f62-a48c-4454-92bb-2202149ba809)


#### b. Create three deployments using the custom Docker image.

start the `minikube start`

![image](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/db546925-cbf5-41b9-a5fb-d80a18c63224)

I am using custom local image for `kubectl` 

I set the env to `eval $(minikube -p minikube docker-env)`

![image](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/c1fc1fc4-f585-4efd-9ba2-f91be5e9d690)


create deployment using this 
```
kubectl create deployment python-app --image=python-app:latest
```
Set image policy for local images

```
kubectl set image deployment/python-app python-app=python-app:latest --record
kubectl patch deployment python-app -p '{"spec":{"template":{"spec":{"containers":[{"name":"python-app","imagePullPolicy":"IfNotPresent"}]}}}}'

```

then change the replicas 1 to 3
```
kubectl edit deployment python-app
```

![image](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/75102cb0-de2d-42b9-820b-231e65fe0d90)

![image](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/d4159159-7324-4fc4-9012-c758f277d468)

![image](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/bef0df03-538a-4e01-be4f-3a5611d9ffc3)

#### c. Verify the successful deployment of the pods.

Get kubectl pods using this command 
```
kubectl get pods
```
![image](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/53e08793-eaf4-4c83-bad9-8877f9f03f83)


### Setting Up Services:

#### a. Create a NodePort service to expose one of the deployments.
I have created the nodeport.yml

```
apiVersion: v1
kind: Service
metadata:
  name: python-app-nodeport
spec:
  type: NodePort
  selector:
    app: python-app # Assuming your deployment has this label
  ports:
    - port: 80
      targetPort: 5000 # Assuming your app is running on this port inside the container
      nodePort: 30007 # Optional: specify a port or let Kubernetes choose
~                                                                          
```

then apply the yml 

`kubectl apply -f nodeport.yml`

`kubectl get svc`

![image](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/97d065ee-12bf-4e44-9bc5-27a6d0d640f3)


#### b. Create a ClusterIP service to expose the second deployment.

I created the clusterIP.yml

```
 apiVersion: v1
kind: Service
metadata:
  name: python-app-clusterip
spec:
  type: ClusterIP
  selector:
    app: python-app # Adjust the selector to match your deployment labels
  ports:
    - port: 80
      targetPort: 5000 # Adjust if your app listens on a different port
```

then apply

`kubectl apply -f clusterIP.yml`

#### c. Create a LoadBalancer service to expose the third deployment.

I created the loadbalancer.yml

```
apiVersion: v1
kind: Service
metadata:
  name: python-app-loadbalancer
spec:
  type: LoadBalancer
  selector:
    app: python-app # Ensure this matches your deployment's labels
  ports:
    - port: 80
      targetPort: 5000
```
then apply

`kubectl apply -f loadbalancer.yml`

#### d. Verify the successful creation of the services.

using 
`kubectl get svc`
![image](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/dc0d531b-87b5-45d1-8e9b-e2fd9659d36a)

You can see all the services are created.


### Accessibility Demonstration:

#### a. Explain why pods are inaccessible outside the cluster when using the ClusterIP service. 

ClusterIP services are designed to access within the Kubernetes cluster. It provied the internal IP that other pods can communicate with it.
This internal IP cannot exposed outside the cluster.

#### b. Demonstrate how pods are accessible within the cluster using the NodePort service.

NodePort services are accessible both within and outside the cluster. Within the cluster, you can access a NodePort service using the ClusterIP of the service and the service port. From outside the cluster, you can access the service using any node's IP address and the NodePort specified when creating the service.

Assuming the Minikube or a node's IP is 192.168.49.2 and the NodePort specified is 30007, you can access the NodePort service from within the cluster using curl http://10.98.51.33:5000 (where 10.98.51.33 is the ClusterIP of the NodePort service) and from outside the cluster using `curl http://192.168.49.2:30007`

#### c. Demonstrate how pods are accessible from outside the cluster using the LoadBalancer service.
![image](https://github.com/Itsnaeem/Dice-Assignment-4/assets/46102040/b0204d41-a044-4ff2-89e8-a94fa022b3fc)

There is a external IP Pending so I used the `minikube tunnel` its creating the tunnel.

In Minikube, the EXTERNAL-IP of a LoadBalancer service is not meant to be an actual IP address accessible from external networks in the same way it would be on a cloud provider. Minikube uses 127.0.0.1 to indicate that the service can be accessed locally, with the help of port forwarding or tunneling.

creates a route between your local machine and the Minikube cluster, 

LoadBalancer services are intended to be accessible from outside the cluster. This type of service automatically assigns an external IP address that can be used to access the service from outside the Kubernetes cluster.

Once the LoadBalancer service is provisioned, it will be assigned an external IP address. You can find this IP address by inspecting the service (kubectl get svc python-app-loadbalancer). Assuming the external IP assigned is x.x.x.x, the service can be accessed from outside the cluster using `curl http://x.x.x.x:80`

