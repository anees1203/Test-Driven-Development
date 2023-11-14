FROM python:3.8
WORKDIR /app
COPY requirements.txt /app/
RUN pip install pip==23.3.1
RUN pip install -r requirements.txt
COPY . /app
CMD ["python", "test_sparse_matrix.py"]
