import os
import json
from dependencies_graph import (get_queries, get_table_dependency,
                                print_table_dependency, print_dependency_of_dependency)
import pytest


def test_get_queries():
    # create a temporary directory with some JSON files
    directory = 'temp_dir'
    os.makedirs(directory, exist_ok=True)
    query1 = {'name': 'query1', 'sql': 'SELECT * FROM table1'}
    query2 = {'name': 'query2', 'sql': 'SELECT * FROM table2'}
    with open(os.path.join(directory, 'config1.json'), 'w', encoding='utf=8') as f:
        json.dump(query1, f)
    with open(os.path.join(directory, 'config2.json'), 'w', encoding='utf=8') as f:
        json.dump(query2, f)

    # test the function
    queries = get_queries(directory)
    assert len(queries) == 2
    assert queries[0]['name'] == 'query1'
    assert queries[1]['name'] == 'query2'

    # clean up the temporary directory
    for filename in os.listdir(directory):
        os.remove(os.path.join(directory, filename))
    os.rmdir(directory)


def test_get_table_dependency():
    # Test case 1: Valid query with one join
    query1 = {
        'schema': {'S': 'my_schema'},
        'table': {'S': 'my_table'},
        'query': {'M': {'from': {'S': 'other_table JOIN yet_another_table ON other_table.id = yet_another_table.id'}}}
    }
    assert get_table_dependency(query1) == ['my_schema.my_table', [
        'other_table', 'yet_another_table']]

    # Test case 2: Valid query with multiple joins
    query2 = {
        'schema': {'S': 'my_schema'},
        'table': {'S': 'my_table'},
        'query': {'M': {'from': {'S': 'table1 JOIN table2 ON table1.id = table2.id JOIN table3 ON table2.id = table3.id'}}}
    }
    assert get_table_dependency(query2) == ['my_schema.my_table', [
        'table1', 'table2', 'table3']]

    # Test case 3: Valid query without joins
    query3 = {
        'schema': {'S': 'my_schema'},
        'table': {'S': 'my_table'},
        'query': {'M': {'from': {'S': 'some_table'}}}
    }
    assert get_table_dependency(
        query3) == ['my_schema.my_table', ['some_table']]

    # Test case 4: Invalid query with missing 'from' statement
    query4 = {
        'schema': {'S': 'my_schema'},
        'table': {'S': 'my_table'},
        'query': {'M': {'select': {'S': 'column1, column2'}}}
    }
    with pytest.raises(KeyError):
        get_table_dependency(query4)


def test_print_table_dependency(capsys):
    dependencies_list = [
        ['schema.table1', ['schema.table2', 'schema.table3']],
        ['schema.table2', ['schema.table4']],
        ['schema.table3', ['schema.table5', 'schema.table6']],
        ['schema.table4', []],
        ['schema.table5', []],
        ['schema.table6', []]
    ]

    print_table_dependency(dependencies_list)

    captured = capsys.readouterr()
    output_lines = captured.out.split('\n')

    assert output_lines[0] == ''
    assert output_lines[1] == ''
    assert output_lines[2] == 'schema.table1'
    assert output_lines[3] == '    |'
    assert output_lines[4] == '    |+schema.table2'
    assert output_lines[5] == '       |'
    assert output_lines[6] == '       |+schema.table4'
    assert output_lines[7] == '    |'
    assert output_lines[8] == '    |+schema.table3'
    assert output_lines[9] == '       |'
    assert output_lines[10] == '       |+schema.table5'
    assert output_lines[11] == '       |'
    assert output_lines[12] == '       |+schema.table6'


def test_print_dependency_of_dependency(capsys):
    dependencies_list = [('table1', ['table2']),
                         ('table2', ['table3']), ('table3', [])]

    # Test when there is a dependency chain
    expected_output = "    |\n    |+table2\n       |\n       |+table3\n"
    print_dependency_of_dependency('table1', dependencies_list, 0)
    assert capsys.readouterr().out == expected_output

    # Test when there is no dependency
    expected_output = ""
    print_dependency_of_dependency('table3', dependencies_list, 0)
    assert capsys.readouterr().out == expected_output

    # Test when the check_table is not in the dependencies_list
    expected_output = ""
    print_dependency_of_dependency('table4', dependencies_list, 0)
    assert capsys.readouterr().out == expected_output
