FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /loja
COPY requirements.txt /loja/
RUN pip install -r requirements.txt
COPY . /loja
EXPOSE 8000/tcp

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
