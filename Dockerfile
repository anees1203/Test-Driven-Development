FROM python:3.8-slim
WORKDIR /app
CMD ["python", "test_sparse_matrix.py"]
