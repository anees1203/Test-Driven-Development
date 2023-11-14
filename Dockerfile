FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -v -r requirements.txt
COPY . /app
CMD ["python", "test_sparse_matrix.py"]
