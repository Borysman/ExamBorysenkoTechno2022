FROM python

COPY . /progression.py

WORKDIR /
CMD ["python3", "progression"]