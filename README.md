# TFG_Fisica
Welcome to the repository of the TFG "Network properties of Informal Support Networks 
in Mental Health"!

In this repo, you will find all code realted used during this project.
Concretly, it contains the scripts and notebooks used to generate and analyze a network based on the CoActuem dataset (https://zenodo.org/record/7443141#.ZAYCChWZNPY).

## Installation
All code is done in Python and the main used packages are Pandas and Networkx.
Please, install all necessary packages running the following command.
``
pip install -r requirements.txt
``

## Code organization
All dataset files are stored at the **data** folder and the generated graphs are saved at **graphs**.
The **img** folder is used to save figure derived from the graphs. 

There are the following python files:
- **graph_creation.py**: Generates a network as specified on the paper
- **assorativity.py**: Python module with all assorativty functions, including our custom assortativity for weighted networks.
- **utils.py**: contains some useful functions

There is also the following notebooks:
- **Graph_Analysis_and_Visualiation**: notebook used to handle the dataset and do the network analysis

## Configuration
All configuration is done by setting up global and specific function variables on the notebook.

For graph creation, please set up the global variables on the **graph_creation.py** file.
You should specify the data you want to work with and the variable **N_PA**.
The latter variable specifies the minumum number of participants that must have answered a question to be considered.
After that, just run the command
``
python graph_creation.py
``
to generate the graph.
