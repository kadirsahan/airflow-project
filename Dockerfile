FROM bde2020/spark-worker:3.1.1-hadoop3.2

# Make a directory for our application
WORKDIR /sparksubmit


# Copy our source code
COPY /app .

RUN chmod -R 777 /sparksubmit

ENTRYPOINT ["/bin/bash", "/sparksubmit/run.sh"]
