FROM python:3.11-slim

WORKDIR /app

COPY ./ /app

RUN python3 -m pip install -U pip

RUN pip install -r req2.txt --no-cache-dir

CMD ["gunicorn", "survey_form.wsgi:application", "--bind", "0:8000" ]