#!/usr/bin/python3
"""
    Script using REST API that returns
    information about given employee ID
    and export data in the CSV format.
"""
import sys
import requests
import csv


def get_employee_todo_progress(employee_id):
    """
        Fetches TODO list progress for a given employee ID from a REST API
        and exports the data to a CSV file.

        Args:
            employee_id (int): The ID of the employee whose TODO
            list progress is to be fetched.

        Returns:
            None
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    user_id = user_data['id']
    employee_name = user_data['name']

    # Fetch TODO list data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Write data to CSV file
    filename = f'{user_id}.csv'
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['USER_ID', 'USERNAME',
                             'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for todo in todos_data:
            csv_writer.writerow([user_id, employee_name,
                                 todo['completed'], todo['title']])

    print(f'Data exported to {filename}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
