#!/bin/bash


singularity shell -B /usr/bin/:/sysbin/ \
                 --env-file /opt/software/powertools/share/jupyter.env \
                 centos.sif \


