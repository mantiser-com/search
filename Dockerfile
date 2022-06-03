FROM elino/python3
RUN pip3 install requests google-search google mailchimp3 requests flask google-api-python-client google-cloud-tasks googleapis-common-protos asyncio-nats-client asyncio-nats-streaming nest_asyncio
EXPOSE 5000
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN mkdir /code
RUN mkdir /files
COPY . /code/
WORKDIR /code
#RUN pip3 install -r requirements.txt



CMD ["./start.sh"]
