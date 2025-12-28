import json
from task_list_service_data import (
    TODO_LIST_FILE_NAME,
    STATUSES,
    MESSAGES
)


def load_tasks():
    try:
        with open(TODO_LIST_FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_tasks(tasks: dict):
    with open(TODO_LIST_FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def get_next_task_id(tasks: dict) -> str:
    if not tasks:
        return "1"
    return str(max(map(int, tasks.keys())) + 1)


def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print(MESSAGES["no_tasks"])
        return

    for task_id, task_data in tasks.items():
        print(f'{task_id}. {task_data["name"]} [{task_data["status"]}]')


def add_task():
    print(MESSAGES["enter_task_name"])
    task_name = input().strip()

    if not task_name:
        print("Название задачи не может быть пустым.")
        return

    tasks = load_tasks()
    task_id = get_next_task_id(tasks)

    tasks[task_id] = {
        "name": task_name,
        "status": STATUSES["in_progress"]
    }

    save_tasks(tasks)

    print(
        f'{MESSAGES["task_added"]}: '
        f'ID = {task_id}, '
        f'Название = "{task_name}"'
    )


def delete_task():
    tasks = load_tasks()
    if not tasks:
        print(MESSAGES["no_tasks"])
        return

    show_tasks()
    print(MESSAGES["enter_task_id_delete"])
    task_id = input().strip()

    if task_id not in tasks:
        print(MESSAGES["task_not_found"])
        return

    task_name = tasks[task_id]["name"]

    print(f'{MESSAGES["delete_confirm_title"]} "{task_name}"')
    print(MESSAGES["delete_confirm_options"])
    choice = input("Введите номер действия: ").strip()

    if choice != "1":
        print(MESSAGES["delete_cancelled"])
        return

    tasks.pop(task_id)
    save_tasks(tasks)

    print(f'{MESSAGES["task_deleted"]}: "{task_name}"')


def mark_task_done():
    tasks = load_tasks()
    if not tasks:
        print(MESSAGES["no_tasks"])
        return

    show_tasks()
    print(MESSAGES["enter_task_id_done"])
    task_id = input().strip()

    if task_id not in tasks:
        print(MESSAGES["task_not_found"])
        return

    if tasks[task_id]["status"] == STATUSES["done"]:
        print(MESSAGES["task_already_completed"])
        return

    tasks[task_id]["status"] = STATUSES["done"]
    save_tasks(tasks)

    print(
        f'{MESSAGES["task_completed"]}: '
        f'"{tasks[task_id]["name"]}"'
    )
