#!/usr/bin/python3
"""
    Script using REST API that returns
    information about given employee ID
"""
import sys
import requests


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data['name']

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])

    print(f'Employee {employee_name} \
          is done with tasks({done_tasks}/{total_tasks}):')
    for todo in todos_data:
        if todo['completed']:
            print(f'\t{todo["title"]}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
