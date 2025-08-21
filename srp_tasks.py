# srp_tasks.py
from abc import ABC, abstractmethod

class Task:
    def __init__(self, task_id, description, due_date=None, completed=False, priority="medium"):
        self.id = task_id
        self.description = description
        self.due_date = due_date
        self.completed = completed
        self.priority = priority

    def __str__(self):
        status = "✓" if self.completed else " "
        due = f" (Due: {self.due_date})" if self.due_date else ""
        pri = f" [prio: {self.priority}]"
        return f"[{status}] {self.id}. {self.description}{due}{pri}"

class TaskStorage(ABC):
    @abstractmethod
    def load_tasks(self):
        pass

    @abstractmethod
    def save_tasks(self, tasks):
        pass

class FileTaskStorage(TaskStorage):
    # ... (เหมือนเดิม)
    def load_tasks(self):
        loaded_tasks = []
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) >= 4:
                        task_id = int(parts[0])
                        description = parts[1]
                        due_date = parts[2] if parts[2] != 'None' else None
                        completed = parts[3] == 'True'
                        priority = parts[4] if len(parts) >= 5 else "medium"
                        loaded_tasks.append(Task(task_id, description, due_date, completed, priority))
        except FileNotFoundError:
            print(f"No existing task file '{self.filename}' found. Starting fresh.")
        return loaded_tasks

    def save_tasks(self, tasks):
        with open(self.filename, "w") as f:
            for task in tasks:
                f.write(f"{task.id},{task.description},{task.due_date},{task.completed},{task.priority}\n")
        print(f"Tasks saved to {self.filename}")


def add_task(self, description, due_date=None, priority="medium"):
    task = Task(self.next_id, description, due_date, False, priority)
    self.tasks.append(task)
    self.next_id += 1
    self.storage.save_tasks(self.tasks)
    print(f"Task '{description}' added.")
    return task


if __name__ == "__main__":
    file_storage = FileTaskStorage("my_tasks.txt")
    manager = TaskManager(file_storage)

    manager.list_tasks()
    manager.add_task("Review SOLID Principles", "2024-08-10")
    manager.add_task("Prepare for Final Exam", "2024-08-15")
    manager.list_tasks()
    manager.mark_task_completed(1)
    manager.list_tasks()
    manager.add_task("High impact bugfix", "2024-08-20", priority="high")
    manager.add_task("Refactor module", "2024-08-25", priority="low")
    manager.list_tasks()
