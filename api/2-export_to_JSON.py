#!/usr/bin/python3
"""
    Script using REST API that returns
    information about given employee ID
    and export data in the JSON format.
"""
import json
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
        Fetches TODO list progress for a given employee ID from a REST API
        and exports the data to a JSON file.

        Args:
            employee_id (int): The ID of the employee whose TODO 
            list progress is to be fetched.

        Returns:
            None
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    user_data = user_response.json()
    user_name = user_data.get('username')

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    json_data = {str(employee_id): []}
    for todo in todos_data:
        json_data[str(employee_id)].append({
            'task': todo['title'],
            'completed': todo['completed'],
            'username': user_name
        })

    filename = f'{employee_id}.json'
    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
