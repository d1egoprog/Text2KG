FROM alpine:3.8 as builder
MAINTAINER Diego Rincon <drinconyanez@unisa.it>

RUN apk update && \
    apk add git wget openjdk8-jre-base py2-pip py2-curl

# install latest CoreNLP release
WORKDIR /opt

RUN wget https://nlp.stanford.edu/software/stanford-corenlp-4.1.0.zip 
RUN unzip stanford-corenlp-4.1.0.zip
RUN rm *.zip

ENV JAVA_XMX 8G
ENV ANNOTATORS tokenize,ssplit,parse
ENV TIMEOUT_MILLISECONDS 60000
ENV THREADS 5
ENV MAX_CHAR_LENGTH 100000
ENV PORT 9000

EXPOSE $PORT

CMD java -Xmx$JAVA_XMX -cp "/opt/stanford-corenlp-4.1.0/*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port $PORT -timeout $TIMEOUT_MILLISECONDS -threads $THREADS -maxCharLength $MAX_CHAR_LENGTH -quiet True -preload openie
