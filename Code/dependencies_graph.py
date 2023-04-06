import os
import json


def get_queries(directory: str) -> list:
    """Get queries from the target directory

    Parameters
    ----------
    directory : str
        The directory that stores all the configuration files in 
        JSON. The directory should be in the same path of the script.

    Returns
    -------
    queries : list
        A list contains all the queries from each configuration
        JSON file.

    """
    queries = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                query = json.load(file)
                queries.append(query)
    return queries


def get_table_dependency(query: dict) -> list:
    """Get table dependency from the query.

    Parameters
    ----------
    query : dict
        The query that extract from the configuration JSON file.

    Returns
    -------
    table_dependency : list
        A list contains two elements. First element is the new table
        which is created by the query. Second element is a list of
        all the tables that construct the new table. They are the
        dependencies of the new table.

    """

    table_dependency = []

    schema = query['schema']['S']
    table = query['table']['S']
    # get the name of the created table from query
    new_table = schema + '.' + table

    from_tables = []

    # Get query `from statement` according to the JSON file
    # Can be optimized if get more information about query strcutre in JSON
    try:
        from_query = query['query']['L'][0]['M']['from']['S']
    except KeyError:
        from_query = query['query']['M']['from']['S']

    from_query = from_query.split()

    # First element is the created table
    from_tables.append(from_query[0])
    for string in from_query:
        if string.lower() == 'join':
            # Dependent table is following the `join``
            table = from_query[from_query.index(string)+1]
            # Only take unique names of the dependencies
            if table not in from_tables:
                from_tables.append(table)
            # Delete current `join` to insure we check next `join` by `index()`
            del from_query[from_query.index(string)]

    table_dependency = [new_table, from_tables]

    return table_dependency


def print_table_dependency(dependencies_list: list) -> None:
    """Print table dependency from the list of dependencies.

    Parameters
    ----------
    dependencies_list : list
        A list contains all the created tables from the queries and
        the tables they are depends on.

    Returns
    -------
    None

    """
    for table_dependency in dependencies_list:
        print('\n')
        print(table_dependency[0])
        for from_table in table_dependency[1]:
            depth = 1
            print(' '*depth*3, '|')
            print(' '*depth*3, f'|+{from_table}')
            print_dependency_of_dependency(
                from_table, dependencies_list, depth)


def print_dependency_of_dependency(
        check_table: str, dependencies_list: list, depth: int) -> None:
    """If the table has dependent tables in the dependencies list,
       print the table dependency from the list of dependencies.

    Parameters
    ----------
    check_table: str
        The name of the table for checking the dependency.
    dependencies_list : list
        A list contains all the created tables from the query and
        the tables they are depends on.
    depth: int
        The depth of the dependency chain.

    Returns
    -------
    None

    """
    for table in dependencies_list:
        if table[0] == check_table:
            # increase the depth for indentation of the graph
            depth += 1
            for from_table in table[1]:
                print(' '*depth*3, '|')
                print(' '*depth*3, f'|+{from_table}')
                print_dependency_of_dependency(
                    from_table, dependencies_list, depth)


def table_dependencies_graph(directory: str) -> None:
    """Print the graph of table dependencies from the given directory

    Parameters
    ----------
    directory : str
        The directory that stores all the configuration files in 
        JSON. The directory should be in the same path of the script.

    Returns
    -------
    None

    """
    table_dependencies = []
    queries = get_queries(directory)

    for query in queries:
        table_dependencies.append(get_table_dependency(query))

    print_table_dependency(table_dependencies)


if __name__ == '__main__':
    table_dependencies_graph('tables')
