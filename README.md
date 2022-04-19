# Text2KG

Text to Knowledge Graph (Text2KG) is a python library builded with the intention of create Knowledge Graph composed on a set of RDF Triples from prosaic text sources.

<p align="center">
  <img src="https://github.com/d1egoprog/Text2KG/blob/main/img/diagram.png?raw=true" alt="High level Pipeline"/>
</p>

The High level view of the proposed pipeline, with each stage in the Knowledge Base Construction process.

## System Preparation

To run the entire system, perform the following steps:

1. Clone the repository: `git clone https://github.com/d1egoprog/text2kg.git`
2. Run excecute the docker-compose file: `docker-compose -p text2kg up -d` 
3. Open the NEO4J web GUI on the ( [localhost](http://0.0.0.0:7474/browser/) default port `7474`) console and execute in the cypher console:
    1. `CREATE CONSTRAINT n10s_unique_uri ON (r:Resource) ASSERT r.uri IS UNIQUE;`
    2. `call n10s.graphconfig.init();`
    3. `call n10s.graphconfig.init( {  handleMultival: "ARRAY" })`
    4. `call n10s.graphconfig.set( { keepLangTag: true, handleRDFTypes: "LABELS_AND_NODES" })`
4. Check the status of the REST API library on the [localhost](http://0.0.0.0:9002/api/v1/ui) default port `9002`.

## Usage

To explain the usage of this component, jupyter notebooks were prepared to showcase the functionability of each step in the proposed methodology   

## Citations 

If this work is from your interest, please use this citation on BibTex format.

```

```

## External Dependencies

* **Stanford CoreNLP:** A [docker image](https://hub.docker.com/r/d1egoprog/stanford-corenlp) has been prepared to be used as an external service able to be consumed by the 'stanza' python library, for more detailed information check the [GitHub](https://github.com/d1egoprog/stanford-corenlp-docker) repository, 
* **NEO4J:** Enterprise solution for graph database with [neosemantics](https://neo4j.com/labs/neosemantics/) plugin, for more detailed information check the [GitHub](https://github.com/neo4j-labs/neosemantics) repository, 
