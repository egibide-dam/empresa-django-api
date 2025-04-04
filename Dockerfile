ARG PYTHON_VERSION=3.13

FROM python:${PYTHON_VERSION}

RUN pip install poetry

COPY ./app /app

WORKDIR /app

RUN poetry install --no-root

EXPOSE 8000

ENTRYPOINT [ "poetry", "run", "python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
