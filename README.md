# hugging_face
## Written by Navya Bhardwaj
## Edited by Dirk Colbry

To get this working you need to install pytorch and the dependecies listed in the enviornment.yml file.  You also need a copy of see-segment so you have access to the example images.  You can clone the repository using the following command:

```git clone git@github.com:see-insight/see-segment.git```

Try creating a conda enviornment using the following command:

```conda env create --prefix ./envs --file environment.yml```

Activate the enviornment by typing

```conda activate ./envs```

Then run jupyter using the following command

```jupyter lab```

or

```jupyter notebook```

# HPCC Instructions

I think I got almost all of this working.  The big part missing is loading the correct libraries in the singularity image.  However, here are the basic steps:

- Clone repository onto the HPCC
- Run the HPCC_install.sh script to build singularity image.
- Open Jupyter onDemand using this new image.  Use EXAMPLE_hug.ipynb in jupyter to identify missing libraries and then do "Conda install" or "pip install" from the jupyter terminal to install the missing libraries.
- Submit a job using Example_output.sb
- Review results by opening Review_HPCC.ipynb in jupyter and seeing the final table. 

That should work.  make sure we take notes on where we get stuck so we can improve the instructions. I will also add these to the README.md file. 
