import os

LOG_FILE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "logs",
    "security.log"
)


def security_dashboard():

    success = 0
    failed = 0
    attacks = 0

    if not os.path.exists(LOG_FILE):
        print("No security logs found.")
        return

    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    for line in logs:

        if "SUCCESS" in line:
            success += 1

        elif "FAILED" in line:
            failed += 1

        elif "ATTACK BLOCKED" in line:
            attacks += 1

    print("\n===================================")
    print("     SecureWind Security Dashboard")
    print("===================================")
    print("Successful Logins :", success)
    print("Failed Logins     :", failed)
    print("IDS Attacks       :", attacks)
    print("Total Events      :", len(logs))
    print("===================================")