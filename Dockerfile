FROM python:3.8-slim
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install pytest==6.2.5
COPY . /app
CMD ["pytest"]
