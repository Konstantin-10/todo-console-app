from task_function import (
    show_tasks,
    add_task,
    delete_task,
    mark_task_done
)
from task_list_service_data import ACTIONS, MESSAGES


def print_menu():
    print(MESSAGES["menu_title"])
    for action_id, action_name in ACTIONS.items():
        print(f"{action_id}. {action_name}")


def main():
    while True:
        print_menu()
        choice = input(MESSAGES["enter_action"]).strip()

        if not choice.isdigit():
            print(MESSAGES["invalid_action"])
            continue

        choice = int(choice)

        if choice == 1:
            show_tasks()
        elif choice == 2:
            add_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            mark_task_done()
        elif choice == 5:
            print(MESSAGES["goodbye"])
            break
        else:
            print(MESSAGES["invalid_action"])


if __name__ == "__main__":
    main()
