# Use Debian as the base image
FROM debian

# Install python3 and pip
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

# Set the working directory
WORKDIR /flask

# Install Flask
RUN pip3 install Flask

# Copy script to working dir
COPY src/ .

# Set the entrypoint
CMD ["python3", "./app.py"]