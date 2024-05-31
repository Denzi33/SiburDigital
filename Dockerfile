FROM python:3.9 as builder

WORKDIR /temporary

COPY . /temporary

RUN pip install --upgrade pip

# IDK why, but pip install e . don't takes this module
RUN pip install aiohttp==3.9.5

RUN pip install e 

CMD ["python", "src/main.py"]
