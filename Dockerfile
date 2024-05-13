FROM python:3.9-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=0
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies and create virtual environment
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential git ffmpeg libsm6 libxext6 libpq5 libgomp1 \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Entry point
ENTRYPOINT ["streamlit", "run", "app.py"]
