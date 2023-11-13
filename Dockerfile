FROM python:3.8-slim
WORKDIR /app
COPY sparse_recommender.py /app
COPY test_sparse_matrix.py /app
CMD ["python", "test_sparse_matrix.py"]

