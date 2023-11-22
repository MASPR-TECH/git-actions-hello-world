FROM python:3.9
WORKDIR /app
COPY /app /app
RUN pip install -r /app/requirements.txt
EXPOSE 5000
CMD python /app/main.py
