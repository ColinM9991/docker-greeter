# Description

The following repository contains Dockerfiles for two Docker containers.

# Containers

## greeter

The greeter container is quite simple. It contains a Python app that hosts a web server, using [Flask](https://flask.palletsprojects.com/en/2.0.x/), which will echo back a name that is captured from a `NAME` environment variable.

The container runs on Debian and installs Python, pip and the Flask Python dependency when the container is building.

## reverse-proxy

The reverse-proxy container runs on CentOS and runs nginx as a reverse-proxy to the greeter containers. Alongside the dockerfile is also a directory containing the nginx configuration and website configuration files.

# Compose

The containers are orchestrated via docker-compose. The Compose configuration will first run two instances of the greeter container, each of which have a name (Alice, or Bob) assigned to the `NAME` environment variable.

When these two containers are running, the reverse-proxy container is then started with the nginx and website config files being mounted to the container.

# Running Locally

To run this locally you must first clone the repository

```
git clone https://github.com/ColinM9991/docker-greeter.git
```

Next, cd into the src directory of the repository

```
cd docker-greeter/src
```

Then instruct Docker Compose to build and run the containers

```
docker-compose up
```

Finally, access the reverse-proxy via your browser

```
http://localhost:8080/alice
http://localhost:8080/bob
```
