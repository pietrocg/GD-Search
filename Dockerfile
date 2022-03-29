FROM python:3.7
WORKDIR /GD-Search
COPY . /GD-Search
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "googlescraper.py"]

