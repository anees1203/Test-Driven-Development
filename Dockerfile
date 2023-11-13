FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install requirements.txt
COPY . .
CMD ["python", "your_application_script.py"]
