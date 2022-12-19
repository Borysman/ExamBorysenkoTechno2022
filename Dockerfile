# FROM python


# COPY . /app

# WORKDIR /app

# CMD ["python3", "progression.py"]

FROM python

WORKDIR /usr/src/app

COPY . .

CMD [ "python3", "./progression.py" ]