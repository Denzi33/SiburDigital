FROM python:3.9 as builder

WORKDIR /temporary

COPY . /temporary

RUN pip install --upgrade pip

RUN pip install aiohttp==3.9.5

RUN pip install e 

CMD ["python", "src/main.py"]
