# Use Python 3.11.4 with Alpine Linux as the base image
FROM python:3.11.4-alpine3.17

# Label the image with a maintainer
LABEL maintainer="djordje@uni.minerva.edu"

# Copy the requirements file to the image
COPY requirements.txt .

# Install dependencies required for psycopg2-binary (used with PostgreSQL)
RUN apk update && \
    apk add python3 postgresql-libs && \
    apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps


# Set the working directory in the container
WORKDIR /flask_app

# Copy the Flask app files to the container
COPY . /flask_app

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "server.py"]