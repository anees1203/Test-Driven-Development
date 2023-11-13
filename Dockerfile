
FROM python:3.8-slim
WORKDIR /app
ENV MAX_WORKERS=2
RUN pip install --upgrade pip --no-cache-dir --default-timeout=100
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "test_sparse_matrix.py"]
