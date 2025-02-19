FROM python:3.9

WORKDIR /app

COPY . /app
COPY deps /app/deps

RUN ls -lh /app/deps  # Debugging
RUN pip install --find-links=/app/deps importlib-metadata zipp flask flask-mysql flask-restful mysql-connector-python requests

CMD ["python", "order_service.py"]
