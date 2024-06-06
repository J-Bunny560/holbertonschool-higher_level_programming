FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    nano \
    && rm -rf /var/lib/apt/lists/*

VOLUME /data

CMD ["bash"]
