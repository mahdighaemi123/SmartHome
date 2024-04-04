FROM python:3.9.19-bookworm

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

ENV PORT=6007

EXPOSE 6007

CMD ["python3", "server.py"]