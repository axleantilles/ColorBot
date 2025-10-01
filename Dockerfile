FROM python:3.10-slim-buster
RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY setup.py .
COPY README.md .
COPY ptn ptn
RUN pip3 install .
RUN mkdir /root/colorbot
RUN ln -s /root/colorbot/.env /root/.env
WORKDIR /root/colorbot
ENTRYPOINT ["/usr/local/bin/colorbot"]
