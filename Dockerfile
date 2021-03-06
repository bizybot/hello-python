FROM resin/rpi-raspbian:wheezy-2015-01-15

# Install Python.
RUN apt-get update && apt-get install -y python

RUN apt-get install -y python-pip

RUN pip install requests

ADD . /app

CMD ["python", "/app/hello.py"]
