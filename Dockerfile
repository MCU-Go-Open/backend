FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV TZ=Asia/Taipei
EXPOSE 8080
CMD [ "python","-u", "server.py" ]