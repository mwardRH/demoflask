# Use an official Python runtime as a base image
FROM docker.io/fedora:25

# Install required packages for git
RUN dnf -y install git

# Install any needed packages specified in requirements.txt
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Run python app
#RUN python3 ./blueflask/wsgi.py

# Run app.py when the container launches
CMD ["python3", "./blueflask/wsgi.py"]
