# Change anything you need to in this file, including the base image.
FROM python:3.6.3

# Copy App Files Over
ADD . /app
WORKDIR /app

# Install Python, Pip
# RUN ["apt-get","update","-y"]
# RUN ["apt-get","install","-y","python3-pip","python3-dev","build-essential"]
# RUN ["pip3","install","--upgrade","pip"]

# Add Dependencies
RUN ["pip3","install","-r","dependencies.txt"]

# Run Flask Server
CMD ["python3","run.py"]