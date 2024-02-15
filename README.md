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



#### b. Create three deployments using the custom Docker image.

#### c. Verify the successful deployment of the pods.


### Setting Up Services:

#### a. Create a NodePort service to expose one of the deployments.


#### b. Create a ClusterIP service to expose the second deployment.

#### c. Create a LoadBalancer service to expose the third deployment.


#### d. Verify the successful creation of the services.

### Accessibility Demonstration:

#### a. Explain why pods are inaccessible outside the cluster when using the ClusterIP service. 

#### b.Demonstrate how pods are accessible within the cluster using the NodePort service.

#### c. Demonstrate how pods are accessible from outside the cluster using the LoadBalancer service.


