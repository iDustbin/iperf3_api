FROM python:3.9

WORKDIR /iperf3_api

COPY ./requirements.txt /iperf3_api/requirements.txt

RUN pip3 install -r /iperf3_api/requirements.txt

COPY ./ /iperf3_api

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]