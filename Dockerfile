FROM python:3.8-slim
WORKDIR /app
RUN pytest
COPY . .
CMD ["python", "test_sparse_matrix.py"]
