FROM boinc/server_apache:4.0.1-b2d

RUN echo "" > /etc/apt/sources.list && \
    echo "deb http://archive.debian.org/debian stretch main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb http://archive.debian.org/debian-security stretch/updates main contrib non-free" >> /etc/apt/sources.list &&  \
    apt-get update

RUN apt-get install net-tools
