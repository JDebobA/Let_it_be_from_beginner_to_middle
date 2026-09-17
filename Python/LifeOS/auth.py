from collections import namedtuple
import constant
import os
from datetime import date
import re
import hashlib

user = namedtuple('User', ['id','email', 'username', 'password', 'age', 'registration_date', 'role'])
CURRENT_USER = None

def save_user(user):
		with open(constant.USER_FILE, "a", encoding="utf-8") as f:
			f.write(f"{user.id}|{user.email}|{user.username}|{user.password}|{user.age}|{user.registration_date}|{user.role}\n")

def load_user():
	users = []
	with open(constant.USER_FILE, "r", encoding="utf-8") as f:
		for line in f:
			line = line.strip()
			if not line:
				continue
			parts = line.split("|")
			if len(parts) != 7:
				continue
			uid, email, username, password, age, registration_date, role = parts
			users.append(user(int(uid), email, username, password, age, registration_date, role))
	return users

def next_id(users):
	if not users:
		return 1
	return max(u.id for u in users) + 1

def hash_password(password):
	return hashlib.sha256(password.encode()).hexdigest()

def registration():
	users = load_user()
	used_email = {u.email for u in users}
	used_name = {u.username for u in users}
	while True:
		email = input("Enter your email: ")
		if constant.EMAIL_RE.fullmatch(email):
			if email not in used_email:
				break
			else:
				print("Данная почта уже задействованна")
		else:
			print("Неверно введенная почта")
	while True:
		username = input("Enter your username: ")
		if constant.USERNAME_RE.fullmatch(username):
			if username not in constant.FORBIDDEN_USERNAMES:
				if username not in used_name:
					break
				else:
					print("Данное имя уже используется")
					continue
			else:
				print("Данное имя запрещенно")
				continue
		else:
			print("Только буквы, цифры и _. Попробуйте снова.")
			continue
	password = input("Enter your password: ")
	age = int(input("Enter your age: "))
	today = date.today()
	hashed = hash_password(password)
	new_id = next_id(users)
	new_user = user(new_id, email, username, hashed, age, today, "user")
	save_user(new_user)
	print(f"Был создан юзер с id: {new_id}")
	return new_user


def login():
	global CURRENT_USER
	username = input("Enter your username: ")
	password = input("Enter your password: ")
	hashed = hash_password(password)
	for u in load_user():
		if u.username == username and u.password == hashed:
			print("Hello")
			CURRENT_USER = u
			return u
	print("Неверный логин или пароль.")
	return None

def get_current_user():
	return CURRENT_USER
	




if __name__ == "__main__":
	registration()
	login()
	login()
		