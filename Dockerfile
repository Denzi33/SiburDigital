FROM python:3.9 as builder

WORKDIR /temporary

COPY . /temporary

RUN pip install e .

CMD ["python", "main.py"]
