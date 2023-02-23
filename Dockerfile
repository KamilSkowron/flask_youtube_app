FROM python:3
WORKDIR /app

# Install dependencies 
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY . .

# Expose the application port
EXPOSE 5000

# Run the application
ENTRYPOINT ["python", "run.py"]