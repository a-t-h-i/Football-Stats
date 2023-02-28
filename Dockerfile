FROM python:3.9

ADD . ./

RUN python -m pip install -r requirements.txt

CMD ["python", "stats.py"]



