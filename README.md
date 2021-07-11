# dash scatter geo example

A simple example of [scatter_geo](https://plotly.com/python/scatter-plots-on-maps/) with 
data from [World Population Prospects 2019](https://population.un.org/wpp2019/Download/Standard/Population/).

![demo](https://raw.github.com/wiki/codequokka/dash-scatter-geo-example/images/animation.gif)

# Requirments
This example of dash app can be run on the host or on the docker.
The following procedure is only for Ubuntu 20.04, however other Unix/Linux based operating systems should be able to meet this requirements in their own ways.

## For running on the host
Install python3, pip, venv and pipenv.
```cosole
$ sudo apt install -y python3.8
$ sudo apt install -y python3-pip
$ sudo apt install -y python3.8-venv
$ pip3 install pipenv
```

## For running on the docker
[Install docker.](https://docs.docker.com/engine/install/ubuntu/)

# Usage
## Common
```cosole
$ git clone https://github.com/codequokka/dash-pivottable-example
$ cd dash-pivottable-example
```

## For running on the host
```cosole
$ pipenv install
$ pipenv shell
$ python app.py
```

## For running on the docker
```cosole
$ docker build . -t dash-scatter-geo-example:0.1
$ docker run -ti --rm -p 8050:8050 -v ${PWD}/data:/usr/src/app/data dash-scatter-geo-example:0.1
```

Accsss http://127.0.0.1:8050/
