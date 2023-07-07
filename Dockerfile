FROM python:3.7
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download en_core_web_md
COPY . /app
CMD python watch_next.py