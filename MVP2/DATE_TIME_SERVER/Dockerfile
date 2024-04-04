FROM python:3.9.19-bookworm

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

ENV PORT=6009

EXPOSE 6009

CMD ["python3", "server.py"]