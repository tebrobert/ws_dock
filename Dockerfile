FROM python:3.10.18

WORKDIR /usr/src/app

RUN pip install asyncio websockets
COPY server.py ./

CMD [ "python", "./server.py" ]
