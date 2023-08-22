#!/user/bin/python3
"""Script that return info from an API"""
import requests
from sys import argv


def employee_task():
    """function that count amount of task completed"""
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    users_api = requests.get(url_users)
    todos_api = requests.get(url_todos)
    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    EMPLOYEE_NAME = ""
    id_employee = int(argv[1])

    if users_api.status_code == 200 and todos_api.status_code == 200:
        users = users_api.json()
        todos = todos_api.json()

    for user in users:
        if user['id'] == id_employee:
            EMPLOYEE_NAME = user['name']

            for task in todos:
                if task['userId'] == id_employee:
                    TOTAL_NUMBER_OF_TASKS += 1
                    if task['completed'] is True:
                        NUMBER_OF_DONE_TASKS += 1
                        TASK_TITLE.append(task['title'])

    print("Employee {} is done with task({}/{})"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task_printed in TASK_TITLE:
        print(f"\t {task_printed}")


if __name__ == '__main__':
    employee_task()
