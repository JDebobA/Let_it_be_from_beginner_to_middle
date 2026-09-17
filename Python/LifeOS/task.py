import os
import auth
import constant
from collections import namedtuple
from datetime import date

Task = namedtuple('Task', ['id', 'user_id', 'title', 'description', 'category', 'priority', 'created_at', 'deadline', 'status'])

def load_tasks():
	tasks = []
	if not os.path.exists(constant.TASK_FILE):
		return tasks
	with open(constant.TASK_FILE, "r", encoding="utf-8") as f:
		for line in f:
			line = line.strip()
			if not line:
				continue
			parts = line.split("|")
			if len(parts) != 9:
				continue
			tid, user_id, title, description, category, priority, created_at, deadline, status = parts
			tasks.append(Task(int(tid), int(user_id), title, description, category, priority, created_at, deadline, bool(int(status))))
	return tasks

def next_id(tasks):
	if not tasks:
		return 1
	return max(t.id for t in tasks) + 1

def create_task():
	current_user = auth.get_current_user()
	if current_user is None:
			print("You must be logged in to create a task.")
			return None
	title = input("Enter task title: ")
	description = input("Enter task description: ")
	category = input("Enter task category: ")
	while True:
		priority = input("Enter task priority (low, medium, high, very high, critical): ")
		if priority in constant.PRIORITIES:
			break
		print("Invalid priority. Please enter a valid priority.")
	created_at = date.today()
	deadline = input("Enter task deadline in days: ")
	while True:
		status = input("Enter task status (ready or not ready): ")
		if status in constant.STATUS:
			break
		print("Invalid status. Please enter a valid status.")

if __name__ == "__main__":
	print(load_tasks())
