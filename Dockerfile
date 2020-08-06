# We're using Ubuntu 20.10
FROM alfianandaa/alf:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/alfianandaa/ProjectAlf /home/projectalf/
RUN mkdir /home/projectalf/bin/
WORKDIR /home/projectalf/

CMD ["python3","-m","userbot"]
