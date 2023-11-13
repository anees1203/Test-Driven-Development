FROM python:3.8-slim
WORKDIR /app
RUN apt-get update && apt-get install -y python3-pytest
COPY . .
CMD ["python", "test_sparse_matrix.py"]
