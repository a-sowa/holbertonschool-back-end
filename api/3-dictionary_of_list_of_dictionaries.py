#!/usr/bin/python3
"""
    Script using REST API that returns
    information about given employee ID
    and export data in the JSON format.
"""
import requests
import json


def get_todo_all_employees():
    """
    Fetches TODO list data for all employees from a REST API
    and exports the data to a JSON file.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'

    users_response = requests.get(users_url)
    users_data = users_response.json()

    todo_all_employees = {}

    for user in users_data:
        user_id = user['id']
        username = user['name']
        todos_url = f'{base_url}/todos?userId={user_id}'

        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        todo_all_employees[user_id] = [{'username':
                                        username, 'task': todo['title'],
                                        'completed': todo['completed']}
                                       for todo in todos_data]

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as jsonfile:
        json.dump(todo_all_employees, jsonfile, indent=4)

    print(f'Data exported to {filename}')


if __name__ == "__main__":
    get_todo_all_employees()
