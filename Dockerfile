# Use the desired base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy all files from the repository into the container
COPY requirements.txt .

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the repository into the container
COPY . .
# Expose the application port
EXPOSE 7860

# Command to run the application
CMD ["python", "TechInterviewAgency/agency.py"]
