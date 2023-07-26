#!/bin/bash
# Build everything we need to INSTALL on HPCC and run inside of singularity
#
# Output is a centos.sif image with see-segment, jupyter and everything installed.
# Secondary output is an overlay.img file you can use with OnDemand

#Clone see-segment
if [ -d see-segment ]
then
    echo "see-segment already found"
else
    echo "Downloading see-segment"
    git clone git@github.com:see-insight/see-segment.git 
fi

#Create base overlay
if [ -f overlay.img ]
then
   echo "overlay.img file already found"
else
   echo "Creating overlay.img file"
   create_jupyter_singularity_overlay

   #Update overlay with see-segment enviornment.
   overlay_exec conda env update --name base --file ./see-segment/environment.yml
#    overlay_exec conda env update --name base --file ./environment.yml
fi

if [ -f centos.sif ]
then
   echo "Centos.sif file already found"
else
   echo "Creating centos.sif file"

   #Make a local copy of centos
   #singularity build centos.sif /opt/software/CentOS.container/7.4/bin/centos
   singularity pull --arch amd64 centos.sif library://library/default/rockylinux:9

   #Wrap overlay.img into centos7
   singularity sif add --datatype 4 --partfs 2 --parttype 4 --partarch 2 --groupid 1 centos.sif overlay.img
fi

