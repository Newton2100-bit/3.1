FROM ubuntu:latest
RUN apt update && apt install python3 -y
WORKDIR  /app
COPY . .
CMD ["python3", "hello.py"]
