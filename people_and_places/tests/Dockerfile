# Use the official Python base image
FROM python:3

# Set the working directory inside the container
WORKDIR /tests

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copying src code to Container
COPY . .

# Set the command to run your Python script
CMD [ "pytest" ]
