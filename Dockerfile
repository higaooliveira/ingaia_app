FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

COPY ["./requirements.txt", "/app/"]
RUN pip install --upgrade pip && pip install -r /app/requirements.txt