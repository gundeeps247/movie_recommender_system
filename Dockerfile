# Use a base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy your application files into the container
COPY app.py /app
COPY movie_dict.pkl /app
COPY similarity.pkl /app

# Install any dependencies
RUN pip install streamlit

# Expose the port your application will be running on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "app.py"]
