import os
import json
import hashlib
import base64
import secrets
import getpass
from typing import Dict, Any

USERS_FILE = "users.json"
SESSION_FILE = "session.json"


def _ensure_files() -> None:
	if not os.path.exists(USERS_FILE):
		with open(USERS_FILE, "w", encoding="utf-8") as f:
			json.dump({}, f)
	if not os.path.exists(SESSION_FILE):
		with open(SESSION_FILE, "w", encoding="utf-8") as f:
			json.dump({}, f)


def load_users() -> Dict[str, Any]:
	_ensure_files()
	with open(USERS_FILE, "r", encoding="utf-8") as f:
		return json.load(f)


def save_users(users: Dict[str, Any]) -> None:
	with open(USERS_FILE, "w", encoding="utf-8") as f:
		json.dump(users, f, indent=2)


def write_session(data: Dict[str, Any]) -> None:
	with open(SESSION_FILE, "w", encoding="utf-8") as f:
		json.dump(data, f)


def read_session() -> Dict[str, Any]:
	_ensure_files()
	with open(SESSION_FILE, "r", encoding="utf-8") as f:
		return json.load(f)


def hash_password(password: str, salt: bytes | None = None) -> Dict[str, str]:
	if salt is None:
		salt = secrets.token_bytes(16)
	dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
	return {
		"salt": base64.b64encode(salt).decode("ascii"),
		"hash": base64.b64encode(dk).decode("ascii"),
	}


def verify_password(stored: Dict[str, str], password: str) -> bool:
	salt = base64.b64decode(stored["salt"].encode("ascii"))
	expected = base64.b64decode(stored["hash"].encode("ascii"))
	dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
	return secrets.compare_digest(dk, expected)


def register(username: str) -> bool:
	username = username.strip()
	if not username:
		print("Invalid username")
		return False
	users = load_users()
	if username in users:
		print("User already exists")
		return False
	pw1 = getpass.getpass("Choose a password: ")
	pw2 = getpass.getpass("Confirm password: ")
	if pw1 != pw2:
		print("Passwords do not match")
		return False
	users[username] = hash_password(pw1)
	save_users(users)
	print("User registered")
	return True


def login(username: str) -> bool:
	username = username.strip()
	users = load_users()
	if username not in users:
		print("User not found")
		return False
	pw = getpass.getpass("Password: ")
	if verify_password(users[username], pw):
		write_session({"user": username})
		print("Login successful")
		return True
	else:
		print("Invalid credentials")
		return False


def logout() -> None:
	write_session({})
	print("Logged out")


def whoami() -> None:
	s = read_session()
	user = s.get("user")
	if user:
		print(f"Signed in as: {user}")
	else:
		print("Not signed in")


def menu() -> None:
	print("Simple CLI Login System")
	print("Commands: register, login, logout, whoami, exit")
	while True:
		cmd = input("cmd> ").strip().lower()
		if cmd == "register":
			u = input("username: ")
			register(u)
		elif cmd == "login":
			u = input("username: ")
			login(u)
		elif cmd == "logout":
			logout()
		elif cmd == "whoami":
			whoami()
		elif cmd in ("exit", "quit"):
			break
		elif cmd == "":
			continue
		else:
			print("Unknown command")


if __name__ == "__main__":
	_ensure_files()
	try:
		menu()
	except KeyboardInterrupt:
		print("\nExiting")

