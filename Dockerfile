FROM python:3.9.1

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]

