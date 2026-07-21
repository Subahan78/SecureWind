import json
import bcrypt
import os
import sys
from datetime import datetime

# Find the parent folder (SecureWind)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rbac import access_control
from security.ids import detect_attack


def write_log(username, status):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "logs",
        "security.log"
    )

    with open(log_path, "a") as log:
        log.write(f"{time} | {username} | {status}\n")


print("===================================")
print("   SecureWind Authentication")
print("===================================")

username = input("Enter Username: ")
password = input("Enter Password: ")

# IDS Check
if detect_attack(username, password):
    write_log(username, "ATTACK BLOCKED")
    exit()

# Find users.json automatically
users_file = os.path.join(
    os.path.dirname(__file__),
    "users.json"
)

with open(users_file, "r") as file:
    data = json.load(file)

login = False

for user in data["users"]:

    if (
        username == user["username"]
        and bcrypt.checkpw(
            password.encode(),
            user["password"].encode()
        )
    ):

        print("\nLogin Successful")
        print("Role:", user["role"])

        write_log(username, "SUCCESS")

        # Open RBAC Menu
        access_control(username, user["role"])

        login = True
        break

if not login:
    print("\nInvalid Username or Password")
    write_log(username, "FAILED")