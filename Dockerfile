FROM python:3.10.18

WORKDIR /usr/src/app

RUN pip install asyncio websockets
COPY server.py ./

EXPOSE 8080
CMD [ "python", "./server.py" ]
