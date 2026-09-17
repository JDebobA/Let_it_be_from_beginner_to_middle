import os
import re

USER_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.txt")
TASK_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.txt")
USERNAME_RE = re.compile(r'^[A-Za-z0-9_]+$')
EMAIL_RE = re.compile(r'[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
FORBIDDEN_USERNAMES = frozenset({"admin", "root", "system"})
PRIORITIES = frozenset({"low", "medium", "high", "very high", "critical"})
STATUS = frozenset({"ready", "not ready"})