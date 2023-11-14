FROM python:3.8
WORKDIR /app
COPY requirements.txt /app/
RUN PIP_NO_CACHE_DIR=1 pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
CMD ["python", "test_sparse_matrix.py"]
