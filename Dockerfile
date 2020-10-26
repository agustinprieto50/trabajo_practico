FROM python:3

RUN git clone https://github.com/agustinprieto50/trabajo_practico.git

RUN pip3 install parameterized

WORKDIR /trabajo_practico

CMD ["python3", "-m", "unittest"]

