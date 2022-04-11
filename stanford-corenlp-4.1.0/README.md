# Stanford NLP Core

This Dockerfile builds the 
[Stanford CoreNLP server](http://stanfordnlp.github.io/CoreNLP/corenlp-server.html) v4.1.0 to a Docker Image.

## Usage

To download and run a [prebuilt version of the CoreNLP server](https://hub.docker.com/r/nlpbox/corenlp/)
from Docker Hub locally at ``http://localhost:9000``, just type:

```
docker build -t stanford_corenlp:4.1.0 .
docker run -p 9000:9000 stanford_corenlp:4.1.0
```

All the JVM parameters can be accesed by editing the Dockerfile and rebuilding the image, by default the parameters configured are:

```
ENV JAVA_XMX 8G
ENV ANNOTATORS tokenize,ssplit,parse
ENV TIMEOUT_MILLISECONDS 60000
ENV THREADS 5
ENV MAX_CHAR_LENGTH 100000
ENV PORT 9000
```

If you not want to edit the Dockerfile the environment variables can be overwriten from the `docker run` command, eg. changing the JVM memory parameter `JAVA_XMX` to reserve more memory. 

```
docker run -e JAVA_XMX=12g -p 9000:9000 -ti stanford_corenlp:4.1.0
```

To check the funcionallity, you can open a web browser window to your docker engine `IP` and the choosen service eg. `PORT=9000` , normally on [localhost:9000](http://localhost:9000).

# Acknowledgements

This docker file was based on the version builded by [NLPBox](https://github.com/NLPbox/stanford-corenlp-docker)
