import os

LOG_FILE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "logs",
    "security.log"
)


def read_logs():

    try:

        with open(LOG_FILE, "r") as file:
            return file.readlines()

    except FileNotFoundError:

        return []


def view_logs():

    logs = read_logs()

    print("\n========== SECURITY LOGS ==========\n")

    if not logs:
        print("No Logs Found.")
        return

    for log in logs:
        print(log.strip())


def login_summary():

    logs = read_logs()

    success = 0
    failed = 0
    attacks = 0

    for log in logs:

        if "SUCCESS" in log:
            success += 1

        elif "FAILED" in log:
            failed += 1

        elif "ATTACK BLOCKED" in log:
            attacks += 1

    print("\n========== LOGIN SUMMARY ==========")
    print("Successful Logins :", success)
    print("Failed Logins     :", failed)
    print("Blocked Attacks   :", attacks)
    print("Total Events      :", len(logs))


def search_user():

    logs = read_logs()

    username = input("\nEnter Username: ")

    found = False

    for log in logs:

        if username in log:

            print(log.strip())

            found = True

    if not found:

        print("No logs found for", username)