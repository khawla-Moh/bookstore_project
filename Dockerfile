
# start doker kernal + python version
FROM python:3.11.9-slim-bullseye

#SHOW LOGS: PYHTON
ENV PYTHONUNBUFFERED=1


#UPDATE KERNAL
RUN apt-get update && apt-get y install gcc libpq-dev 

#folder for project
WORKDIR /app

#COPY REQUIRMENT
COPY requirments.txt /app/requirments.txt

#install requirments
RUN pip install -r /app/requirments.txt

#copy all project files
COPY  . /app/ 