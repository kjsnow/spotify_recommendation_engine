MAINTAINER Kyle Snow "kjsnow11@gmail.com"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY api .
CMD ["yarn", "start-api"]