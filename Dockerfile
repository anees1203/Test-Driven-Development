FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --progress-bar off -r requirements.txt
COPY . /app
CMD ["python", "test_sparse_matrix.py"]
