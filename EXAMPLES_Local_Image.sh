#!/bin/bash


singularity shell -B /usr/bin/:/sysbin/ \
                 --env PATH=/miniconda3/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/sysbin/ \
                 --env-file /opt/software/powertools/share/jupyter.env \
                 centos.sif \


