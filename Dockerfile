FROM python:3.8-slim
WORKDIR /app
COPY . /app 
RUN pip install pytest
CMD ["python", "test_sparse_matrix.py"]

