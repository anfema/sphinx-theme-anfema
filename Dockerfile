# You can use this to build an anarchy_sphinx docker image
# just mount your folder to /docs and go!
# docker run -it -v `pwd`:/docs sphinx

FROM debian:latest

RUN apt-get update && apt-get install python3 python3-setuptools python3-pip make -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip3 install sphinx_bootstrap_theme
ADD . /anarchy_sphinx
WORKDIR anarchy_sphinx
RUN python3 setup.py install
RUN mkdir /docs
WORKDIR /docs
ENTRYPOINT ["make","html"]