FROM ubuntu:18.04
MAINTAINER Patrick <root@sixlab.cn>

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y unzip vim-tiny iputils-ping \
    && apt-get autoclean -y && apt-get clean -y && apt-get autoremove -y \
    && mkdir -p /app \
    && rm -rf /var/lib/apt/lists/* /var/log/* /tmp/* /var/tmp/*

COPY ./ /app

ENV TZ=Asia/Shanghai

ENV LANG=C.UTF-8

CMD ["source", "venv/bin/activate", "&&", "python3", "app.py"]
