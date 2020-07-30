# We're using Ubuntu 20.10
FROM alfianandaa/bish:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/alfianandaa/ProjectBish /home/projectbish/
RUN mkdir /home/projectbish/bin/
WORKDIR /home/projectbish/

CMD ["python3","-m","userbot"]
