FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80

# Run test_sparse_matrix.py when the container launches
CMD ["python", "test_sparse_matrix.py"]
