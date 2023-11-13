FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN requirements.txt .
COPY . .
CMD ["python", "test_sparse_matrix.py"]
