# We're using Debian Slim Buster
FROM alfianandaa/bish:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/alfianandaa/ProjectBish /home/projectbish/
RUN mkdir /home/projectbish/bin/
WORKDIR /home/projectbish/

CMD ["python3","-m","userbot"]
