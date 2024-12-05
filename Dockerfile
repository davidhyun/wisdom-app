FROM python:3.11.11-slim

WORKDIR /usr/src/app

COPY Pipfile* ./

RUN pip install pipenv && pipenv install --system --deploy

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
