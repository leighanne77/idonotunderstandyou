# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5002 available to the world outside this container
EXPOSE 5002

# Run the TTS service
CMD ["python", "generate_audio.py"]
