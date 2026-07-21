import os
from datetime import datetime

INCIDENT_LOG = os.path.join(
    os.path.dirname(__file__),
    "..",
    "logs",
    "incident.log"
)


def create_incident(username, incident_type):

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(INCIDENT_LOG, "a") as file:
        file.write(f"{time} | {username} | {incident_type}\n")

    print("\n===================================")
    print("      INCIDENT RESPONSE SYSTEM")
    print("===================================")
    print("Incident Created Successfully")
    print("User :", username)
    print("Type :", incident_type)
    print("SOC Team Notified")
    print("===================================")