# Description About app.py

This is a Python script that uses the Flask web framework to create an endpoint that returns a JSON object. The endpoint listens on the root URL and responds to GET requests. When a GET request is made to the root URL, the script connects to a Redis database that's running on the host 'redis' on port 6379 and uses database 0. It then retrieves the value associated with the key 'Devops' and returns it in a JSON object as the value for the key 'DevOps_Engineer'. If the key 'Devops' is not found in the database, the script returns a JSON object with an 'error' key and the value 'Key not found'. The script also Store a key-value pair where key is 'Devops' and value is 'Kwami' before running the endpoint. If the script is run directly, it starts the Flask development server on 0.0.0.0 (all available network interfaces) on port 9001.

# Description About Dockerfile

This is a Dockerfile which is used to build an image for a containerized application. The first line specifies the base image, in this case, it's python:3.8-slim-buster which is a minimal version of Python 3.8.

The next line copies all the files in the current directory to a directory called '/app' in the container.

Then the next line 'WORKDIR /app' sets the working directory to /app in the container.

Then the command 'RUN pip install --upgrade pip && \ pip install -r requirements.txt' runs the command to install or update 'pip' package installer and install the required dependencies specified in the 'requirement.txt' file present in the local folder.

After that 'EXPOSE 9001' The EXPOSE instruction informs Docker that the container will listen on the specified network ports at runtime. This doesn't publish the ports.

Finally, the command 'CMD ["python", "app.py"]' sets the command to be run when the container starts. This command runs the "app.py" script using the python interpreter in the container.

When this Dockerfile is used to build an image, it creates an image that contains all of the application's dependencies, files and the runtime environment to run the application. The container created from this image runs the command specified in the 'CMD' instruction and starts the web application on port 9001 which is exposed at runtime.

# docker-compose.yml
This is a docker-compose.yml file for a project with two services: web and redis. It specifies that the web service should be built from the current directory (.) and be exposed on port 9001 of the host machine, and that it depends on the redis service. The web service also mounts the current directory as a volume at /app within the container. The redis service uses the redis:latest image and exposes port 6379 of the container on port 6379 of the host machine, and also mounts a volume redis-data to container's /data

#Pre-requisites

1. Docker installation on your local machine
#Start Steps

1. navigate to the directory with the docker-compose.yml file
2. run the command docker-compose up to start the services.
3. Access the web application on http://localhost:9001
# Note: 
you can use docker-compose down to stop the services and docker-compose build to rebuild the images.