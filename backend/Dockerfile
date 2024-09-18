FROM python:3.9.2

COPY requirements.txt RestAPI/requirements.txt
WORKDIR /RestAPI

RUN pip install -r requirements.txt
COPY . /RestAPI

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]