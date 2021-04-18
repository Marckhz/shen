FROM tiangolo/meinheld-gunicorn-flask:python3.7

COPY . /api

RUN pip install -r requierements.txt

CMD ['gunicorn', "manage:app"]