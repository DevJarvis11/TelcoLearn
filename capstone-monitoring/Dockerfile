FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py monitor.py dashboard.py ./
COPY templates ./templates
CMD ["python", "monitor.py"]
