FROM python:3.8

ENV PROJECT_DIR /usr/src/app
WORKDIR ${PROJECT_DIR}

RUN pip install pipenv
COPY Pipfile ${PROJECT_DIR}/
COPY Pipfile.lock ${PROJECT_DIR}/
RUN pipenv install --system --deploy

COPY app.py ${PROJECT_DIR}/
COPY data.py ${PROJECT_DIR}/

EXPOSE 8050
ENTRYPOINT [ "python", "app.py" ]