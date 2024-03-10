FROM python:3.8

ENV APP_HOME /abstract_method

WORKDIR $APP_HOME

COPY  .  .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "main.py"]





