FROM python:3.7
WORKDIR /GD-Search
COPY . /GD-Search
RUN apt-get update
RUN apr-get install -y unixodbc-dev
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]

