# Code Challenge

For this task, I will determine the relationships between database tables as described across a series of configuration files in JSON. Details of the challenge can be found [here](http://codechallenge.trackmandata.com/).

## Demo in Jupyter Notebook

[Table Dependencies Graph](./Table_Dependencies_Graph.ipynb)

## Module in Python

[dependencies_graph](./dependencies_graph.py)

## Unit test by Pytest

[test_dependenciies_graph.py](./test_dependencies_graph.py)

## Steps of the Implementation

1. Read and understand the Challenge.
2. Check table file to get familar with JSON format.
3. Make first code snippet to try one file.
4. Make an unit test for the code snippet.
5. Scale it to all tables in the directory.
6. Update the unit test for the final script.
7. Update the documentation.

## Brief of the Approach

1. Extract all the query out from JSON files.
2. Read the query and extract information about the created table and its depending tables.
3. Assemble the relationship in a list.
4. Generate the graph according to the list by expanding all the dependencies of the tables, including the dependencies of the dependencies.

## Functions in the Module `dependencies_graph.py`

* `get_queries()`: Get queries from the target directory
* `get_table_dependency()`: Get table dependency from the query.
* `print_table_dependency()`: Print table dependency from the list of dependencies.
* `print_dependency_of_dependency()`: If the depending table has also dependent tables in the dependencies list, print the table dependency from the list of dependencies.

## Usage

### Check the [output](./output.txt) of the challenge

1. Change the working directory to the same as [`dependencies_graph.py`](./dependencies_graph.py).
2. Make sure the configuration files (JSON) in a folder in the same directory.
3. In bash, run:

    ```bash
    python dependencies_graph.py
    ```

### In your own script

1. Put the configuration files (JSON) in a folder in the same directory as the Python script.
2. In the Python script, import `dependencies_graph` module.
3. Use `print_dependency_of_dependency()` function, applying the name of the configuration folder as argument to generate the table relationship graph.
