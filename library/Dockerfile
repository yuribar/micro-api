FROM python:3

LABEL Yuri Barbosa <yuribarbosa123@hotmail.com>

ADD app.py requirements.txt /
RUN pip install -r ./requirements.txt

ENV PORT=5000

EXPOSE $PORT
HEALTHCHECK CMD curl --fail http://localhost:$PORT || exit 1

CMD [ "python app.py" ]