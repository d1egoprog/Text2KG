# Text2KG - A Dockerized Service

Text to Knowledge Graph (Text2KG) is a dockerized set of services built to generate Knowledge Graphs; the created statements are shown in the form of RDF Triples, extracted from prosaic text sources. The services can be consumed via REST API. 

This work was presented at the European Semantic Web Conference (ESWC2022) in the frame of the Knowledge Graph Generation from Text (TEXT2KG) workshop. 

The High level view of the proposed pipeline stage the Knowledge Base Construction process.

<p align="center">
  <img src="https://github.com/d1egoprog/Text2KG/blob/main/img/diagram.png?raw=true" alt="High level Pipeline"/>
</p>

## System Preparation

To run the entire system, perform the following steps:

1. Download and excecute the docker compose file

```
git clone https://github.com/d1egoprog/Text2KG.git
docker-compose -p text2kg -f deploy.yml up
```

2. Open the NEO4J web GUI on the ( [localhost](http://0.0.0.0:7474/browser/) default port `7474`) console and execute in the cypher console:

```
CREATE CONSTRAINT n10s_unique_uri ON (r:Resource) ASSERT r.uri IS UNIQUE;
call n10s.graphconfig.init();
call n10s.graphconfig.init( {  handleMultival: "ARRAY" })
call n10s.graphconfig.set( { keepLangTag: true, handleRDFTypes: "LABELS_AND_NODES" })
```

3. Check the status of the REST API library on the [localhost](http://0.0.0.0:9002/api/v1/ui), default port `9002`; it can be changed on the docker compose file.

## Usage

To explain the usage of this component, jupyter notebooks were prepared to showcase the functionability of each step in the proposed methodology. Initially is necesary to log into the prepared jupyterlab interface and open the `text2kg` folder, where the notebooks are located.

The notebooks are located under the [examples](examples/)] folder in this repository. **NOTE:** The examples will be mounted in the `Text2KG` folder in the JupyterLab console.

### Open the JupyterLab Interface

To check the functionality, you can open a web browser window to your docker-engine `IP` and the chosen service, e.g., `PORT=9988`; if you run this on your machine should be on [localhost:9988/lab](http://localhost:9988/lab). The Jupyter Lab landing page should deploy if the deployment went correctly, asking for the session token. To obtain the token, just query the system log by using the command:

``` BASH
docker logs text2kg_tfgpu_jupyter_1
```

An output similar to this one should appear:

>     To access the server, open this file in a browser:
>         file:///home/jupyter/.local/share/jupyter/runtime/jpserver-1-open.html
>     Or copy and paste one of these URLs:
>         http://3538c43d20f3:8888/lab?token=<TOKEN>
>      or http://127.0.0.1:8888/lab?token=<TOKEN>

Take the value of the `token` variable from the URL, *<TOKEN>* in this example, and paste it into the token textbox displayed in the browser.

Happy hacking!! 🖖🖖.


## External Dependencies

* **Stanford CoreNLP:** A [docker image](https://hub.docker.com/r/d1egoprog/stanford-corenlp) has been prepared to be used as an external service able to be consumed by the 'stanza' python library, for more detailed information check the [GitHub](https://github.com/d1egoprog/docker-stanford-corenlp) repository.
* **NEO4J:** Enterprise solution for graph database with [neosemantics](https://neo4j.com/labs/neosemantics/) plugin, for more detailed information check the [GitHub](https://github.com/neo4j-labs/neosemantics) repository and the [python library repository](https://github.com/neo4j-labs/rdflib-neo4j).  
* **TensorFlow:** The dockerized version of the popular framework selected for working with GPUs, with and additional JupyterLab Installation. For more information a [GitHub](https://github.com/d1egoprog/docker-tensorflow-gpu-jupyter) repository has been prepared and a [Docker images](https://hub.docker.com/r/d1egoprog/tensorflow-gpu-jupyter) as well.


## Citations 

If this work is with your interest you can read the presented paper [DOI](http://doi.org)

Also, if you use this system in your research please dont forget to cite 👍 this work, the sugested BibTex is recomended to use.

``` BibTex

```

## Contact

If you have any questions in deployment or any error is found, please contact me by opening an issue. And contributing is always welcome. The [Github repository URL](https://github.com/d1egoprog/Text2KG).
