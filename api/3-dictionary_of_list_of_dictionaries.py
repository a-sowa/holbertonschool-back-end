#!/usr/bin/python3
"""
    Script using REST API that returns
    information about given employee ID
    and export data in the JSON format.
"""
import json
import requests


def get_employee_todo_list_progress():
    """
        Fetches TODO list data for all employees from a REST API
        and exports the data to a JSON file.

        Returns:
            None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    users_response = requests.get(f'{base_url}/users')
    users_data = users_response.json()

    all_tasks = {}

    for user in users_data:
        user_id = user.get('id')
        user_name = user.get('username')

        todos_return = requests.get(f'{base_url}/todos?userId={user_id}')
        todo_data = todos_return.json()

        task_list = []
        for task in todo_data:
            task_title = task.get('title')
            task_status = task.get('completed')
            task_dict = {"username": user_name,
                         "task": task_title,
                         "completed": task_status
                         }
            task_list.append(task_dict)

            all_tasks[str(user_id)] = task_list

    json_filename = 'todo_all_employees.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == '__main__':
    get_employee_todo_list_progress()
