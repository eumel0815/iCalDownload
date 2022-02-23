FROM python:3.10

WORKDIR /icalDownloader

COPY . /icalDownloader/

RUN pip install --no-cache-dir --upgrade -r /icalDownloader/requirements.txt

CMD [ "python", "main.py" ]