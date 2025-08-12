FROM gcr.io/google-appengine/python

RUN virtualenv /env -p python3

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

RUN apt-get update && apt-get install -y python-opencv

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt


ADD . /app

CMD gunicorn -b :$PORT main:app
