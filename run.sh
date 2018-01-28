#!/bin/sh

sudo docker run -it -p 8888:8888 -v`pwd`:/notebooks gcr.io/tensorflow/tensorflow:latest-py3

