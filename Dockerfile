FROM python:3.9 as builder

WORKDIR /temporary

COPY src .

COPY pyproject.toml .

COPY .env .

RUN pip install pyproject.toml build-system

CMD ["python", "main.py"]
