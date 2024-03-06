# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables for Python and Docker
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /music

# Copy the dependencies file to the working directory
COPY requirements.txt /music/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /music/
COPY . /music/

# Expose port 8000 to allow communication to/from server
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
