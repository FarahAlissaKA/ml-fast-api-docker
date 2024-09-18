FROM python:3.9.2

COPY requirements.txt RestAPI/requirements.txt
WORKDIR /RestAPI

RUN pip install -r requirements.txt
COPY . /RestAPI

EXPOSE 8501

ENTRYPOINT ["streamlit","run"]

CMD ["streamlit_app.py"]

