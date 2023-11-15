FROM python:3.11.4-alpine3.17
LABEL maintainer="psterne@minerva.edu"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents and the .env file into the container at /app
ADD . /app
COPY .env .

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5162 available to the world outside this container
EXPOSE 5162

# Run app.py when the container launches
CMD ["python", "app.py"]
