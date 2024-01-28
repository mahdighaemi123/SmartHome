FROM python:alpine3.19

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV MONGO_URI=mongodb://mongo:27017/
ENV FLASK_APP=app.py

CMD [ "flask", "run", "--host=0.0.0.0","--port=5000"]