FROM arm32v7/python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV SCANNERNAME fart

COPY bridge.py ./
COPY Reader.py ./
COPY deviceName.txt ./

CMD [ "python", "./bridge.py" ]