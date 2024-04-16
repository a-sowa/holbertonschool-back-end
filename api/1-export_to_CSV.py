#!/usr/bin/python3
"""
    Script using REST API that returns
    information about given employee ID
    and export data in the CSV format.
"""
import csv
import requests
import sys


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
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    user_response = requests.get(user_url)
    user_data = user_response.json()
    user_name = user_data.get('username')

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    csv_filename = f'{employee_id}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            task_completed_status = 'True' if task.get('completed')\
                                    else 'False'
            formatted_row = [employee_id,
                             user_name,
                             task_completed_status,
                             task.get('title')]
            csv_writer.writerow(formatted_row)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
