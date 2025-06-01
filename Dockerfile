FROM python:3.13


# Install dependencies

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt


# Start Flask app
COPY todo/ todo/
COPY start.py .
EXPOSE 5000

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000",  "start:app"]

