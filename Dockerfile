FROM python:3.8-slim
WORKDIR /app
COPY . /app 
RUN pip install --upgrade pip && pip install -v -r requirements.txt
CMD ["python", "test_sparse_matrix.py"]

