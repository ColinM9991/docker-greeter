# Use CentOS as base image
FROM centos

# Install nginx
RUN dnf upgrade -y && \
    dnf install -q -y nginx

# Entrypoint for nginx
CMD ["nginx", "-g", "daemon off;"]