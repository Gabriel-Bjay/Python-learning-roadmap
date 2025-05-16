"""
    This module contains functions to manage a to-do list.
    It allows users to add, view, delete, and mark tasks as completed.
    Each function is designed to handle specific operations related to task
    management."""


def add_tasks(tasks):
    task = input("Enter the task you want to add: ").title().strip()
    if task in tasks:
        print("Task already exists!")
        return tasks
    if task == "":
        print("Task cannot be empty!")
        return tasks
    if len(task) > 50:
        print("Task is too long! Please keep it under 50 characters.")
        return tasks
    if len(tasks) >= 10:
        print("Task list is full! Please delete a task before "
              "adding a new one.")
        return tasks
    tasks.append(task)
    print(f"Task '{task}' added successfully!")
    return tasks


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("Tasks:")
        for task in range(len(tasks)):
            print(f"{task + 1}. {tasks[task]}")


def delete_tasks(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        print("No tasks available to delete.")
        return tasks
    task_number = input("Enter the task number you want to delete: ")
    if (
        not task_number.isdigit()
        or int(task_number) < 1
        or int(task_number) > len(tasks)
    ):
        print("Invalid task number!")
        return tasks
    task_number = int(task_number) - 1
    deleted_task = tasks.pop(task_number)
    print(f"Task '{deleted_task}' deleted successfully!")
    return tasks


def mark_completed(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        print("No tasks available to mark as completed.")
        return tasks
    task_number = input(
        "Enter the task number you want to mark as completed: "
        )
    if (
        not task_number.isdigit()
        or int(task_number) < 1
        or int(task_number) > len(tasks)
    ):
        print("Invalid task number!")
        return tasks
    task_number = int(task_number) - 1
    completed_task = tasks[task_number]
    tasks[task_number] = f"{completed_task} (Completed)"
    print(f"Task '{completed_task}' marked as completed!")
    return tasks
