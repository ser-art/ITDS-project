FROM python:3.9-slim

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Entry point
ENTRYPOINT ["streamlit", "run", "app.py"]
