FROM python:3.9-slim as builder

# Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=0
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Python environment
ENV PATH="/opt/venv/bin:$PATH"

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential git \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && python -m venv /opt/venv \
    && pip install --upgrade pip

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

FROM python:3.9-slim as final

# Python environment
ENV PATH="/opt/venv/bin:$PATH"

USER root

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get -y install --no-install-recommends git ffmpeg libsm6 libxext6 libpq5 libgomp1 && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/venv /opt/venv

WORKDIR /app

COPY . .

ENTRYPOINT ["streamlit", "run", "app.py"]
