# Use an official Python runtime as a base image
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "test_sparse_matrix.py"]
