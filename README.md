# Dice-Assignment-4
This Assignment is based on Kubernetes

### Minikube Installation
#### a. Use a virtualization platform (e.g., VirtualBox) if not already installed. You can use your host OS if you have Docker Desktop Installed.


#### b. Install Minikube by following the official installation instructions for your operating system.

#### c. Verify the installation by running basic Minikube commands and checking the version.


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


