FROM python

WORKDIR /usr/src/app

COPY . .

CMD [ "python3", "./progression.py" ]