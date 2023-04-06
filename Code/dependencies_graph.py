import os
import json


def get_queries(directory):
    queries = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                query = json.load(file)
                queries.append(query)
    return queries


def get_table_dependency(query):

    table_dependency = []

    schema = query['schema']['S']
    table = query['table']['S']
    new_table = schema + '.' + table

    from_tables = []
    try:
        from_query = query['query']['L'][0]['M']['from']['S']
    except KeyError:
        from_query = query['query']['M']['from']['S']

    from_query = from_query.split()
    from_tables.append(from_query[0])
    for string in from_query:
        if string.lower() == 'join':
            table = from_query[from_query.index(string)+1]
            if table not in from_tables:
                from_tables.append(table)
            del from_query[from_query.index(string)]

    table_dependency = [new_table, from_tables]

    return table_dependency


def print_table_dependency(dependencies_list: list):
    for table_dependency in dependencies_list:
        print('\n')
        print(table_dependency[0])
        for from_table in table_dependency[1]:
            depth = 1
            print(' '*depth*3, '|')
            print(' '*depth*3, f'|+{from_table}')
            check_if_has_dependent_table(from_table, dependencies_list, depth)


def check_if_has_dependent_table(check_table: str, dependencies_list: list, depth: int) -> None:
    for table in dependencies_list:
        if table[0] == check_table:
            depth += 1
            for from_table in table[1]:
                print(' '*depth*3, '|')
                print(' '*depth*3, f'|+{from_table}')
                check_if_has_dependent_table(
                    from_table, dependencies_list, depth)


table_dependencies = []

q0 = get_queries('tables')

for q in q0:
    table_dependencies.append(get_table_dependency(q))

print_table_dependency(table_dependencies)


# print(q0)

# for q in q1:
#     table_dependencies.append(get_table_dependency(q))

# print(table_dependencies)


# print(get_table_dependencies)
