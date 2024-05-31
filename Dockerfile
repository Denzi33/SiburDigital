FROM python:3.9 as builder

WORKDIR /temporary

COPY . /temporary

RUN pip install pyproject.toml build-system

CMD ["python", "main.py"]
