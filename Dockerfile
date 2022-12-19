FROM python

COPY . /progression.py

WORKDIR /progression.py

CMD ["python3", "progression"]