# winequality
CS643 wine quality prediction

Steps to set up the Cloud Environment and Run the model Training and prediction

Create AWS EMR Clusters using the key pairs and select the instance as 4(one Master and three slaves) and select application as spark

After Creating the Cluster add the SSH inbound rule to the master node for port 22

Using putty Connect to the master node using the public ip address and the AWS pem file (connect as Hadoop user)

We must Install the following packages in the masters in order to run the python code (install the mentioned modules as Root user i.e. Run command: sudo su)

pip install pyspark

pip install numPy

The project contains two py files (Copied these two files using WinSCP from local to the vm)

one python file (ModelCreation.py) to read the Trainingdata.csv train and save the model Command to run the python file: python ModelCreation.py

Second python file (Application.py) to read the model and take the test data as input from the command line arguments and gives the F1 score as output Command with args (Without docker): python Applciation.py TestDataset.csv

Create a docker file (DockerFile) Command: nano DockerFile This file consists of all the commands which are needed to be executed while building the image

Install Docker using the command sudo yum install docker -y

Start the Docker service using sudo service docker start

Build the image using the command below (which takes DockerFile as input): sudo docker build wqp.

Check whether the image is created or not using the command sudo docker images

Once the image is created now tag the image to the docker hub. Command: sudo docker tag wqp tj20ba/wine_quality_prediction

Once the image is tagged now push the image to the docker hub for which we have to login in to the docker. Below are the steps to be followed sudo docker login sudo docker push tj20ba/wine_quality_prediction

Once the image is pushed to the Docker hub now, we must pull the image from the docker hub and run it

Commands to run the image as an instance (Container) and execute the application, sudo docker run --name model -d wqp copying the testdata.csv into the container sudo docker cp ../TestDataset.csv model:/ get inside the container and execute the application sudo docker exec -it model sh now running the application to calculate the f1 score python Application.py TestDataset.csv
